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

- ``iris``: For loading and manipulating NetCDF data (and plotting via iris.plot + iris.quickplot)
- ``numpy``: For numerical operations
- ``dask``: For handling large datasets
- ``matplotlib``: For creating visualisations

Once your environment is set up, begin by importing the necessary packages:

.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt
    import iris
    import iris.plot as iplt
    import iris.quickplot as qplt
    import dask.array as da
    import cf_units

    # Suppress repeated NumPy masked-array casting warnings from sample data loading
    import warnings
    warnings.filterwarnings('ignore')

    # Use microsecond date precision to align with upcoming Iris default behaviour
    iris.FUTURE.date_microseconds = True

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
    print(f"Time coordinate: {cubelist[0].coord('time').points[0]} s to {cubelist[0].coord('time').points[-1]} s\n")
    print(cubelist)

This will display all the available fields in your output file.

Computing Derived Diagnostics
==============================

Overview
--------

A small number of LFRic diagnostics are not fully generalised and will be incorrect when making unorthodox changes to background gas constants, planet radius, etc. Additionally, some diagnostics may not be available to output from the model directly and must therefore be calculated manually. This guide provides functions to calculate the following derived quantities:

- **Virtual Temperature** (:math:`T_v`): Temperature adjusted for the presence of water vapour
- **Virtual Potential Temperature** (:math:`\theta_v`): Potential temperature adjusted for moisture.

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
            rd (float): Specific gas constant (J kg^-1 K^-1)
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
            rd (float): Specific gas constant (J kg^-1 K^-1)
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

To use these functions with your loaded data, first define the gas constants appropriate for your simulation (note: these are example values and should match your model configuration):

.. code-block:: python

    # Gas constants (change based on the background gas)
    rd = 4124      # Specific gas constant (J kg^-1 K^-1)
    cp = 14300     # Specific heat capacity at constant pressure (J kg^-1 K^-1)

    # Add derived diagnostics to your cubelist
    cubelist = add_virtual_temperature(cubelist, rd)
    cubelist = add_virtual_potential_temperature(cubelist, rd, cp)

    # Check that the new cubes have been added
    print(cubelist)

Converting from UGRID to X/Y Grid
==================================

Overview
--------

LFRic outputs diagnostics on an unstructured grid (UGRID). To work with familiar structured X/Y grids for plotting and analysis, you must regrid/reshape the data. This section provides an example function to reshape UGRID cubes onto a structured X/Y grid.

.. note::

    Reshaping the data in this way does not perform any interpolation or regridding in the traditional sense (e.g., with ESMF). Currently, ESMF regridders work with lat/lon coordinates and thus cannot generally be used for the cartesian domain. Instead, we can simply reshape the data array and define new X/Y coordinates based on the known grid spacing and domain size. This is sufficient for cartesian-domain CRMs where the grid is regular and uniform, but it is not fully generalised—reshaping in this way assumes the 1D UGRID data is already perfectly ordered.


Helper Functions
----------------

Below is a helper function for converting from UGRID to X/Y:

.. raw:: html

    <details>
    <summary><b>Click to expand: Reshaping Function</b></summary>

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

To reshape your UGRID cubes to a regular X/Y grid, you need to provide the domain dimensions
and grid spacing of your simulation. You can either define this yourself (see example below)
or use the existing ``projection_x_coordinate`` and ``projection_y_coordinate`` mesh
coordinates directly. Generally, the latter is preferred, but sometimes the mesh coordinates
don't always give you what you expect! So, for the purposes of this tutorial, we'll simply
define our grid parameters manually.


.. code-block:: python

    # Define your domain parameters (adjust these to match your simulation)
    nx = 128        # Number of grid points in x direction
    ny = 128        # Number of grid points in y direction
    delta_x = 2000  # Grid spacing in x direction (metres)
    delta_y = 2000  # Grid spacing in y direction (metres)

    # Extract a cube to regrid (e.g., air temperature)
    air_temp_cube = cubelist.extract_cube("air_temperature")

    # Regrid to X/Y coordinates
    air_temp_xy = reshape_ugrid_cube_to_xy_grid(air_temp_cube, nx, ny, delta_x, delta_y)

    print(air_temp_xy)

Visualisations
====================

Vertical Cross-Sections
------------------------

To visualise vertical cross-sections through your domain, you can slice the data along a surface (e.g., through the domain centre):

.. code-block:: python

    # Cube to plot
    cube = cubelist.extract_cube('air_temperature')

    # Choose a time step and x slice index to plot
    time_step = 30
    y_index = 64 # Centre of the domain

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 8))
    qplt.pcolormesh(cube[time_step, :, y_index, :], cmap='RdBu_r')
    plt.title(f'Air Temperature slice at timestep {time_step}')
    plt.show()

This will give you a vertical cross-section of air temperature through the domain centre at the specified time step. You can adjust the time step and slice index to explore different parts of the domain and different times in the simulation.

Vertical Profiles
------------------

To examine how fields vary with height at a specific location, you can extract and plot vertical profiles as follows (e.g., for virtual potential temperature):

.. code-block:: python

    cube = cubelist.extract_cube("virtual_potential_temperature")
    z = cube.coords('full_levels')[0].points

    # Define location and time steps
    num_timesteps = cube.shape[0]
    timesteps = [0, num_timesteps//2, -1] # Define time steps to plot
    x_index = nx // 2  # Centre of domain in x direction
    y_index = ny // 2  # Centre of domain in y direction

    # Get height coordinate for plotting
    time = cube.coord("time").points

    # Create the plot
    fig, ax = plt.subplots(figsize=(5, 5))
    for i in timesteps:
        plt.plot(cube.data[i, :100, y_index, x_index], z[:100], label=f'{time[i]} s')
    plt.xlabel('Virtual potential temperature (K)')
    plt.ylabel('Vertical level')
    plt.title('Virtual potential temperature profile at domain centre')
    plt.legend()
    plt.show()

This will give you vertical profiles of virtual potential temperature at the domain centre for the initial, middle, and final time steps of the simulation.

Domain-Average Profiles
------------------------

You can also compute and plot domain-averaged vertical profiles using the function below.
This function takes the cubelist, computes the horizontal mean for each cube, and plots the initial and final state in a grid layout.

.. code-block:: python

    def plot_initial_final_profiles(cubelist: iris.cube.CubeList, col_lim: int = 3) -> None:
        """
        Plots horizontally-averaged initial and final vertical profiles for all cubes in the cubelist.

        Parameters
        ----------
        cubelist : iris.cube.CubeList
            Iris cubes containing data of shape (t, z, y, x)
        col_lim : int, default 3
            The maximum number of columns allowed in the subplot grid layout.
        """
        n = len(cubelist)
        rows = int(np.ceil(n / col_lim))
        fig, axs = plt.subplots(rows, col_lim, figsize=(col_lim * 3, rows * 3), squeeze=False)
        axs = axs.flatten()

        for ax, cube in zip(axs, cubelist):

            # Take horizontal means
            cube = cube.collapsed(['projection_x_coordinate', 'projection_y_coordinate'], iris.analysis.MEAN)

            # Extract the first (initial) and last (final) time steps
            initial_data = cube.core_data()[0]
            final_data = cube.core_data()[-1]

            # Trigger Dask array computation into memory if the data is lazily loaded
            initial_data = initial_data.compute() if isinstance(initial_data, da.Array) else initial_data
            final_data = final_data.compute() if isinstance(final_data, da.Array) else final_data

            name = cube.name()
            unit = cube.units
            time_coord = cube.coord("time").points

            # Extract vertical coordinate
            z = (cube.coords('full_levels') or cube.coords('half_levels'))[0].points

            ax.plot(initial_data, z, label=f"t={time_coord[0]} s", linewidth=1)
            ax.plot(final_data, z, label=f"t={time_coord[-1]} s", linewidth=1)

            # Handle formatting for mixing ratio units to avoid stripping down to "1"
            if cube.name() not in ['vapour_mixing_ratio', 'cloud_liquid_water_mixing_ratio']:
                xlabel_unit = unit.format(cf_units.UT_UTF8)
            else:
                xlabel_unit = "kg/kg"

            ax.set_xlabel(f'{name} ({xlabel_unit})')
            ax.set_ylabel("Vertical level")

            # Use a logarithmic scale for profiles that span orders of magnitude
            if cube.name() in ['air_density', 'air_pressure']:
                ax.set_xscale('log')

        axs[0].legend(fontsize="small", loc="best")

        # Remove any remaining empty axes
        for ax in axs[len(cubelist):]:
            fig.delaxes(ax)

        fig.suptitle('Initial & final profiles (domain-averaged)')

        fig.tight_layout()
        plt.show()

Animations
----------

It is also fairly straightforward to create an animation using `iris.plot`. The below example shows how to do this for vertical slices in a interactive Jupyter notebook:

.. code-block:: python

    # Ensure inline animation rendering in Jupyter
    plt.rcParams['animation.html'] = 'html5'

    upward_air_velocity_cube = cubelist.extract_cube('upward_air_velocity')
    cube_iter = upward_air_velocity_cube[:,:110,64,:].slices_over('time') # Crop to 0:110 vertical levels
    ani = iplt.animate(cube_iter, qplt.pcolormesh)

    # Display inline in notebook
    HTML(ani.to_jshtml(fps=10))

This will create an animation of vertical slices of upward air velocity through the domain centre between vertical levels 0—110 over time.
Try experimenting with different fields, slice indices, and animation settings to explore the temporal evolution of your simulation!
