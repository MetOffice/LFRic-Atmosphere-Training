Plotting your data
==================

Once you have run your workflow, you will likely want to visualise the output data.
There are several ways you can do this. Here we cover two methods: using terminal
GUI tools and using Python with the Iris library.

Using GUI tools
---------------

For quick visualisation of NetCDF data files, you can use terminal-based GUI tools
such as ``xconv`` and ``ncview``. These tools allow you to inspect data quickly
without writing any code.

Using Python
------------

The output files are in NetCDF format, which can be read using a variety of
software packages. Python provides more flexibility and allows for more complex
visualisations. Below is an example of how to read and plot NetCDF data using
the Iris and Matplotlib libraries.

.. code-block:: python

   import os
   from pathlib import Path

   import iris
   import iris.quickplot as qplt
   import matplotlib.pyplot as plt

   # Set the path to the data.
   path_to_data = Path("path/to/your/data")

   # List what that path contains (up to 10 files).
   print(os.listdir(path_to_data)[:10])

   # Load one output file to inspect available cubes.
   print(iris.load(path_to_data / "data_file.pp"))

   # Load a cube from a NetCDF file.
   surface_temperature_cube = iris.load_cube(
	   path_to_data / "output_file.nc", "surface_temperature"
   )

   # Change the units from Kelvin to Celsius.
   surface_temperature_cube.convert_units("celsius")

   # Choose the time slice to plot (e.g. the first time slice).
   time_slice = 0

   # Plot the data.
   qplt.contourf(surface_temperature_cube[time_slice, :, :])
   plt.gca().coastlines()
   plt.show()

The resulting plot can be seen below.

.. image:: /_static/iris_quickplot_example.png
   :alt: Example plot generated using Iris quickplot

