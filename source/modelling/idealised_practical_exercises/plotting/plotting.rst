****************************
Plotting and Analysis
****************************

After running your idealised CRM workflow, you will want to visualise and analyse the output data.
This section provides guidance on loading, processing, and visualising 3D atmospheric fields from LFRic idealised simulations using Python and the Iris library.

.. contents::
   :local:
   :depth: 2

Setup and Data Loading
======================

Setting up your Python environment
----------------------------------

To follow along with this guide, you will need the following Python packages:

- ``iris``: For loading and manipulating NetCDF data
- ``numpy``: For numerical operations
- ``matplotlib``: For creating visualisations

Once your environment is set up, begin by importing the necessary packages and setting up plotting preferences:

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   import matplotlib.colors as mcolors
   from matplotlib.gridspec import GridSpec
   import warnings
   warnings.filterwarnings('ignore')

   import iris
   import iris.coords
   import iris.util
   from iris.coords import DimCoord, AuxCoord
   
   iris.FUTURE.date_microseconds = True

   %matplotlib inline
   %config InlineBackend.figure_format = 'retina'
   # ToDo

Loading Model Output
--------------------

The output from your idealised CRM simulation will be in NetCDF format. You can load this data
using Iris:

.. code-block:: python

   # Define paths to model output files
   path = 'path/to/your/lfric_diag.nc'

   # Load all cubes from the file as a CubeList
   cubelist = iris.load(path)

   # Print cubelist info
   print(f"Loaded {len(cubelist)} fields from {path}\n")
   print(cubelist)

This will display all the available fields in your output file.

Computing Derived Diagnostics
==============================

Overview
--------

A small number of LFRic diagnostics are not fully generalised and will be incorrect when making unorthodox changes to background gas constants, planet radius, etc. Additionally, some diagnostics may not be available to output from the model directly and must therefore be calculated manually. This guide provides functions to calculate the following derived quantities:

- **Virtual Temperature** (:math:`T_v`): Temperature adjusted for the presence of water vapour
- **Virtual Potential Temperature** (:math:`\theta_v`): Potential temperature adjusted for moisture

These diagnostics can be calculated on a cell-by-cell basis and therefore do not require regridding before calculation.

Helper Functions
----------------

Below are helper functions for calculating :math:`\theta_v` and :math:`T_v`. You can copy these into your analysis script or Jupyter notebook.

.. raw:: html

   <details>
   <summary><b>Click to expand: Diagnostic Functions</b></summary>

.. code-block:: python

   def add_virtual_temperature(cubelist, rd, rv=461.5):
       """Calculates virtual temperature and adds as a new cube to the CubeList

       Args:
           cubelist (CubeList): CubeList containing at least "air_temperature" and 
                                "vapour_mixing_ratio" cubes
           rd (float): Specific gas constant for dry air (J kg^-1 K^-1)
           rv (float, optional): Specific gas constant for water vapor. Defaults to 461.5.

       Returns:
           CubeList: CubeList with the virtual temperature cube added
       """
       # Check to make sure virtual temperature is not already in the CubeList
       if "virtual_temperature" in [cube.name() for cube in cubelist]:
           print("Virtual temperature cube already exists in the CubeList. Skipping.")
           return cubelist

       try:
           T = cubelist.extract_cube("air_temperature")
       except iris.exceptions.ConstraintMismatchError as e:
           print(
               f"Error: {e}\n"
               "Virtual temperature cannot be calculated without the 'air_temperature' cube."
           )
           raise

       try:
           qv = cubelist.extract_cube("vapour_mixing_ratio")
       except iris.exceptions.ConstraintMismatchError:
           try:
               qv = cubelist.extract_cube("humidity_mixing_ratio")
           except iris.exceptions.ConstraintMismatchError as e:
               print(
                   f"Error: {e}\n"
                   "Virtual temperature cannot be calculated without the 'vapour_mixing_ratio' "
                   "or 'humidity_mixing_ratio' cube."
               )
               raise

       T_data = T.core_data()
       qv_data = qv.core_data()

       assert T.shape == qv.shape, (
           f"Temperature and vapour mixing ratio cubes must have same shape, "
           f"but got {T.shape} and {qv.shape}"
       )

       epsilon = rd / rv
       Tv_data = T_data * (1 + qv_data / epsilon) / (1 + qv_data)

       Tv = T.copy(data=Tv_data)
       Tv.rename("virtual_temperature")
       Tv.units = "K"

       cubelist.append(Tv)
       print("Virtual temperature cube added.")

       return cubelist


   def add_virtual_potential_temperature(cubelist, rd, cp, p0=1e5, rv=461.5):
       """Calculates virtual potential temperature and adds as a new cube to the CubeList

       Args:
           cubelist (CubeList): CubeList containing at least "air_temperature", 
                                "air_pressure", and "vapour_mixing_ratio"/"humidity_mixing_ratio" cubes
           rd (float): Specific gas constant for dry air (J kg^-1 K^-1)
           cp (float): Specific heat capacity at constant pressure (J kg^-1 K^-1)
           p0 (float, optional): Reference pressure in Pa. Defaults to 1e5.
           rv (float, optional): Specific gas constant for water vapor. Defaults to 461.5.

       Returns:
           CubeList: CubeList with the virtual potential temperature cube added
       """

       # Check to make sure virtual potential temperature is not already in the CubeList
       if "virtual_potential_temperature" in [cube.name() for cube in cubelist]:
           print("Virtual potential temperature cube already exists in the CubeList. Skipping.")
           return cubelist

       try:
           T = cubelist.extract_cube("air_temperature")
           p = cubelist.extract_cube("air_pressure")
       except iris.exceptions.ConstraintMismatchError as e:
           print(
               f"Error: {e}\n"
               "Virtual potential temperature cannot be calculated without the 'air_temperature' "
               "and 'air_pressure' cubes."
           )
           raise

       try:
           qv = cubelist.extract_cube("vapour_mixing_ratio")
       except iris.exceptions.ConstraintMismatchError:
           try:
               qv = cubelist.extract_cube("humidity_mixing_ratio")
           except iris.exceptions.ConstraintMismatchError as e:
               print(
                   f"Error: {e}\n"
                   "Virtual potential temperature cannot be calculated without the 'vapour_mixing_ratio' "
                   "or 'humidity_mixing_ratio' cube."
               )
               raise

       T_data = T.core_data()
       p_data = p.core_data()
       qv_data = qv.core_data()

       assert T.shape == p.shape == qv.shape, (
           f"Temperature, pressure, and vapour mixing ratio cubes must have same shape, "
           f"but got {T.shape}, {p.shape}, and {qv.shape}"
       )
       
       epsilon = rd / rv
       theta_v_data = T_data * (p0 / p_data) ** (rd / cp) * (1 + qv_data / epsilon) / (1 + qv_data)

       theta_v = T.copy(data=theta_v_data)
       theta_v.rename("virtual_potential_temperature")
       theta_v.units = "K"

       cubelist.append(theta_v)
       print("Virtual potential temperature cube added.")

       return cubelist

.. raw:: html

   </details>

Using the diagnostic functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use these functions with your loaded data, first define the gas constants appropriate for your simulation (note: these are example values and should match your model configuration):

.. code-block:: python

   # Gas constants (change based on your background gas)
   rd = 4124      # Specific gas constant for dry air (J kg^-1 K^-1)
   cp = 14300     # Specific heat capacity at constant pressure (J kg^-1 K^-1)

   # Add derived diagnostics to your cubelist
   cubelist = add_virtual_temperature(cubelist, rd)
   cubelist = add_virtual_potential_temperature(cubelist, rd, cp)

   # Check that the new cubes have been added
   print(cubelist)

Regridding from UGRID to X/Y Grid
==================================

Overview
--------

LFRic outputs diagnostics on an unstructured grid (UGRID). To work with familiar structured X/Y grids for plotting and analysis, you must regrid the data. This section provides an example function to reshape UGRID cubes onto a structured X/Y grid.

.. note::

   ToDo!

Helper Functions
----------------

Below is a helper function for regridding from UGRID to X/Y coordinates:

.. raw:: html

   <details>
   <summary><b>Click to expand: Regridding Function</b></summary>

.. code-block:: python

   def reshape_ugrid_cube_to_xy_grid(cube, nx, ny, delta_x, delta_y):
       """
       Reshape an iris cube on a UGRID into a cube with defined x/y distance coordinates.
       
       Originally written by Denis Sergeev (Bristol). See https://github.com/exoclim/aeolus/

       Parameters
       ----------
       cube : iris.cube.Cube
           Input cube to reshape
       nx : int
           Number of grid points in x direction
       ny : int
           Number of grid points in y direction
       delta_x : float
           Grid spacing in x direction in metres
       delta_y : float
           Grid spacing in y direction in metres

       Returns
       -------
       iris.cube.Cube
           Reshaped cube with x/y coordinates
       """
       import dask.array as da
       
       # Promote auxiliary time coordinate to dimension coordinate if necessary
       try:
           iris.util.promote_aux_coord_to_dim_coord(cube, "time")
       except iris.exceptions.CoordinateNotFoundError:
           pass

       # Calculate domain sizes
       domain_size_x = nx * delta_x
       domain_size_y = ny * delta_y

       # Define new shape
       new_shape = cube.shape[:-1] + (ny, nx)

       # Create spatial coordinates
       x_coord = iris.coords.DimCoord(
           np.linspace(-domain_size_x / 2, domain_size_x / 2, nx + 1)[:-1],
           standard_name="projection_x_coordinate",
           units="m",
       )
       y_coord = iris.coords.DimCoord(
           np.linspace(-domain_size_y / 2, domain_size_y / 2, ny + 1)[:-1],
           standard_name="projection_y_coordinate",
           units="m",
       )
       x_coord.guess_bounds()
       y_coord.guess_bounds()

       # Reshape data (supports both numpy and dask arrays)
       data = cube.core_data()

       if isinstance(data, da.Array):
           reshaped = da.reshape(data, new_shape)
       elif isinstance(data, (np.ndarray, np.ma.MaskedArray)):
           reshaped = np.reshape(data, new_shape)
       else:
           raise TypeError(f"Unsupported data type for cube core data: {type(data)}")
       
       # Create new cube with reshaped data
       new_cube = iris.cube.Cube(
           iris.util.reverse(reshaped, new_shape.index(y_coord.shape[0])),
           dim_coords_and_dims=[(c, cube.coord_dims(c)[0]) for c in cube.dim_coords]
           + [
               (y_coord, len(new_shape) - 2),
               (x_coord, len(new_shape) - 1),
           ],
       )

       # Copy metadata from original cube
       new_cube.metadata = iris.common.metadata.CubeMetadata(**cube.metadata._asdict())

       return new_cube

.. raw:: html

   </details>

Using the regridding function (ToDo!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To reshape your UGRID cubes to a regular X/Y grid, you need to know the domain dimensions
and grid spacing of your simulation. There are two ways to do this:

1. Use the `projection_x_coordinate` and `projection_y_coordinate` mesh coordinates directly (generally preferred)
2. Regrid manually by defining the mesh coordinates yourself

Generally, method 1 is preferred here, but sometimes the mesh coordinates don't always give you what you expect! So, for completeness, we'll outline both methods below. 

.. code-block:: python

   # Define your domain parameters (adjust these to match your simulation)
   nx = 128        # Number of grid points in x direction
   ny = 128        # Number of grid points in y direction
   delta_x = 50.0  # Grid spacing in x direction (metres)
   delta_y = 50.0  # Grid spacing in y direction (metres)

   # Extract a cube to regrid (e.g., air temperature)
   air_temp_cube = cubelist.extract_cube("air_temperature")

   # Regrid to X/Y coordinates
   air_temp_xy = reshape_ugrid_cube_to_xy_grid(air_temp_cube, nx, ny, delta_x, delta_y)

   print(air_temp_xy)

Visualisations—ToDo!
====================

Horizontal Slices
------------------

To visualise horizontal slices of your data (e.g., at a specific height level), you can extract a single level and plot it using Iris's quickplot functionality:

.. code-block:: python

   import iris.quickplot as qplt

   # Extract air temperature cube and regrid
   air_temp_cube = cubelist.extract_cube("air_temperature")
   air_temp_xy = reshape_ugrid_cube_to_xy_grid(air_temp_cube, nx, ny, delta_x, delta_y)

   # Choose a time step and height level to plot
   time_step = 0
   height_level = 30

   # Create the plot
   fig, ax = plt.subplots(figsize=(10, 8))
   qplt.contourf(air_temp_xy[time_step, height_level, :, :], cmap='RdYlBu_r', levels=20)
   plt.colorbar(ax=ax, label='Temperature (K)')
   plt.title(f'Air Temperature at t={time_step}, z={height_level}')
   plt.show()

You can also create subplots to compare multiple time steps or levels:

.. code-block:: python

   fig, axes = plt.subplots(2, 2, figsize=(14, 12))
   axes = axes.flatten()

   time_steps = [0, 100, 200, 300]
   height_level = 30

   for i, t in enumerate(time_steps):
       qplt.contourf(air_temp_xy[t, height_level, :, :], axes=axes[i], cmap='RdYlBu_r')
       axes[i].set_title(f'Temperature at t={t}')
       plt.colorbar(ax=axes[i], label='K')

   plt.tight_layout()
   plt.show()

Vertical Cross-Sections
------------------------

To visualise vertical cross-sections through your domain, you can slice the data along a
line (e.g., through the domain centre):

.. code-block:: python

   import iris.plot as iplt

   # Extract a cube and regrid
   air_temp_cube = cubelist.extract_cube("air_temperature")
   air_temp_xy = reshape_ugrid_cube_to_xy_grid(air_temp_cube, nx, ny, delta_x, delta_y)

   # Choose a time step and extract a cross-section
   time_step = 100
   y_index = ny // 2  # Middle of domain in y direction

   # Extract the cross-section (x-z plane)
   cross_section = air_temp_xy[time_step, :, y_index, :]

   # Plot the cross-section
   fig, ax = plt.subplots(figsize=(12, 6))
   cf = iplt.contourf(cross_section, cmap='RdYlBu_r', levels=20)
   plt.colorbar(cf, ax=ax, label='Temperature (K)')
   plt.title(f'Vertical Cross-Section (X-Z) at t={time_step}')
   plt.xlabel('X Distance (m)')
   plt.ylabel('Height (m)')
   plt.show()

Vertical Profiles
------------------

To examine how fields vary with height at a specific location, you can extract and plot vertical profiles:

.. code-block:: python

   # Extract air temperature cube and regrid
   air_temp_cube = cubelist.extract_cube("air_temperature")
   air_temp_xy = reshape_ugrid_cube_to_xy_grid(air_temp_cube, nx, ny, delta_x, delta_y)

   # Define location and time step
   time_step = 0
   x_index = nx // 2  # Centre of domain in x direction
   y_index = ny // 2  # Centre of domain in y direction

   # Extract vertical profile at the centre of the domain
   profile_initial = air_temp_xy[0, :, y_index, x_index]
   profile_final = air_temp_xy[-1, :, y_index, x_index]

   # Get height coordinate for plotting
   height = profile_initial.coord("height")

   # Create the plot
   fig, ax = plt.subplots(figsize=(10, 8))
   plt.plot(profile_initial.data, height.points, 'b-', label='Initial', linewidth=2)
   plt.plot(profile_final.data, height.points, 'r-', label='Final', linewidth=2)
   plt.xlabel('Temperature (K)')
   plt.ylabel('Height (m)')
   plt.title('Vertical Temperature Profile at Domain Centre')
   plt.legend()
   plt.grid(True, alpha=0.3)
   plt.show()

Domain-Average Profiles
~~~~~~~~~~~~~~~~~~~~~~~~

You can also compute and plot domain-averaged vertical profiles to see the overall evolution
of the atmosphere:

.. code-block:: python

   # Compute domain-averaged profiles
   profile_initial_avg = air_temp_xy[0].collapsed(['projection_x_coordinate', 'projection_y_coordinate'], iris.analysis.MEAN)
   profile_final_avg = air_temp_xy[-1].collapsed(['projection_x_coordinate', 'projection_y_coordinate'], iris.analysis.MEAN)

   # Get height coordinate
   height = profile_initial_avg.coord("height")

   # Plot
   fig, ax = plt.subplots(figsize=(10, 8))
   plt.plot(profile_initial_avg.data, height.points, 'b-', label='Initial (domain average)', linewidth=2)
   plt.plot(profile_final_avg.data, height.points, 'r-', label='Final (domain average)', linewidth=2)
   plt.xlabel('Temperature (K)')
   plt.ylabel('Height (m)')
   plt.title('Domain-Averaged Vertical Temperature Profiles')
   plt.legend()
   plt.grid(True, alpha=0.3)
   plt.show()

Animations
----------

To visualise how fields evolve over time, you can create animations. Below is an example of animating horizontal slices at a fixed height level:

.. code-block:: python

   import iris.plot as iplt
   import iris.quickplot as qplt
   from matplotlib.animation import FuncAnimation
   from IPython.display import HTML

   # Extract and regrid velocity data
   upward_velocity_cube = cubelist.extract_cube("upward_air_velocity")
   upward_velocity_xy = reshape_ugrid_cube_to_xy_grid(upward_velocity_cube, nx, ny, delta_x, delta_y)

   # Select a height level to animate
   height_level = 30
   data_to_animate = upward_velocity_xy[:, height_level, :, :]

   # Create animation
   fig, ax = plt.subplots(figsize=(10, 8))

   def update(frame):
       ax.clear()
       cf = ax.contourf(data_to_animate[frame].data, cmap='RdBu_r', levels=20)
       ax.set_title(f'Upward Velocity at t={frame}')
       ax.set_xlabel('X Distance (m)')
       ax.set_ylabel('Y Distance (m)')
       plt.colorbar(cf, ax=ax, label='Upward Velocity (m/s)')

   ani = FuncAnimation(fig, update, frames=data_to_animate.shape[0], repeat=True)

   # Display inline in notebook
   plt.close()
   HTML(ani.to_jshtml(fps=5))

Summary
=======

This section has provided:

1. Methods for loading and exploring LFRic idealised model output using Iris
2. Functions for calculating derived diagnostics (virtual temperature, virtual potential temperature)
3. Techniques for regridding from UGRID to regular X/Y coordinates
4. Examples of visualising data through:

   - Horizontal slices at fixed heights
   - Vertical cross-sections
   - Vertical profiles (both point-specific and domain-averaged)
   - Time-evolving animations
