The unstructured world
======================

In an unstructured mesh world:
one convention can describe any layout, even fully irregular layouts

better collaboration
better software support

LFRic cubesphere: output as ‘UGRID’ unstructured mesh

.. image:: /_static/unstructured_examples.png
   :width: 650px


.. image:: /_static/mesh1.png
   :align: right
   :width: 160px

UGRID description of unstructured data includes:

* **nodes** from individual coordinates
* **edges/faces** from node **connectivity** (using indices)
* data on each node / edge / face

* nodes / edges / faces need not align
* can mix 3- / 4- / 5- / n-sided faces

* All model data will be either on faces or edges
* Each vertical layer has the same horizontal coordinates



.. image:: /_static/mesh2.png
   :width: 650px

.. image:: /_static/mesh3.png
   :width: 650px

Cubed sphere mesh
-----------------

LFRic Atmosphere uses a cubed sphere mesh. Meshes are named after the number cells along one edge of the cube. The visualisation shows an C16 mesh, which represents the Earth surface by 6 x 16 x 16 = 1536 cells ("squares") in each horizontal layer. Most cell corners have four neighbour cells but at the corners of the cube only three cells meet.

.. video:: /_static/mesh_animation.mp4
   :loop:

*Visualisation of a C16 mesh and how the mesh on a cube is projected to a sphere.*

The used projection of squares on a cube surface to a sphere causes that mesh sizes have different lengths in km. Representative length scales for mesh resolutions are given in the table below.

.. list-table:: Cubed Sphere Mesh Resolutions
   :header-rows: 1

   * - LFRic Mesh
     - ≈ dx [km]
   * - C48​
     - 192.1
   * - C128
     - 72.0
   * - C448
     - 20.6
   * - C896
     - 10.3
   * - C1808
     - 5.1
   * - C9216
     - 1.0


Tools for unstructured data
---------------------------

.. image:: /_static/unstructured_tools.png
   :width: 650px

Regridding unstructured data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the unstructured mesh context, [ESMF ](https://earthsystemmodeling.org/)(Earth System Modelling Framework) is utilised for regridding tasks. Regridding allows for comparison between datasets defined on different meshes, enabling analysis that requires data on specific local representations, such as OSGB (Ordnance Survey National Grid) in Britain, or requires computations suited to structured grids, like zonal means.

The regridding process in the unstructured world follows two primary steps: preparation and execution. During the preparation phase, the source and target grids are compared, and weights are calculated using ESMF. The preparation step is computationally intensive, particularly with unstructured grids. In the execution phase, the calculated weights are applied to the data, and a new cube is constructed. This phase typically involves Python libraries such as DASK and SciPy.

Different types of regridders are available depending on the source and target grid types. These include Mesh-to-Grid, Grid-to-Mesh, and Area-Weighted Regridders.

Each regridder offers various features, including the ability to read and write cubes, perform area-weighted regridding, and preserve metadata during operations. Additionally, the capability to load and save regridders is supported.

For datasets with masked data, the regridding process ensures that the mask is handled correctly. If the mask from the source grid covers more than a specified threshold of a target grid cell, that target cell is included in the mask. Otherwise, it is excluded from the target grid.

Key features of regridding include:

- flexibility in selecting regridders, 
- the ability to preserve metadata, and 
- efficient handling of masked data.




.. image:: /_static/regrid.png
   :width: 400px

Visualising unstructured data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
For unstructured data visualisation, PyVista and GeoVista are the primary tools used. While Matplotlib and Cartopy have traditionally been used for structured data, these tools do not scale well and struggle to handle high-resolution unstructured meshes.

Traditional tools such as Matplotlib and Cartopy struggle to handle high-resolution unstructured grids. For instance, a C48 mesh has approximately 13,000 faces, and a C1048 mesh (approximately 9.55 km grid spacing at the equator) would require excessive computation and memory resources. With PyVista, a C48 mesh can be rendered in 369 ms, while a C1048 mesh takes 3.87 seconds.

Unstructured visualization tools include VTK, a GPU-accelerated toolkit for visualization and mesh processing, and Paraview, a parallel visualization application. PyVista provides a high-level interface for 3D visualization, and GeoVista manages cartographic elements. The combination of these tools offers a paradigm shift by enabling efficient GPU-powered visualization and interactive user experiences.

PyVista is a 3D visualization engine that leverages GPU power for scalable rendering. It offers both visualization and computational capabilities, including a high-level API and filters. PyVista integrates seamlessly with modern scientific workflows, such as Jupyter notebooks.

GeoVista provides cartographic capabilities for PyVista, supporting various map projections, coastlines, texture mapping, and regional extraction. It is compatible with Iris, as well as other scientific libraries like NumPy and Xarray.
