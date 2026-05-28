**********************
The unstructured world
**********************

Unstructured meshes and the UGRID format represent the future of scientific data delivery.
As computational models evolve, especially in the realm of climate and weather modelling, transitioning to these new formats will be crucial for effective data handling.

.. important::
    The unstructured world section will explore how unstructured data is transforming workflows, why it is important, and how scientists can adapt their practices to support these advancements.

Unstructured meshes offer greater flexibility and precision compared to structured grids, making them essential for data evaluation and verification.
The section will explore the challenges and benefits of unstructured data and the technical details of using the UGRID format.

Features of unstructured meshes in the LFRic Atmosphere model
-------------------------------------------------------------

Thanks to its use of an unstructured mesh, LFRic atmosphere offers greater flexibility, scalability, and precision. Some benefits of using an unstructured mesh instead of a structured grid are:

* **Improved Resolution**: Unstructured meshes provide more accurate representations of complex shapes and regions, allowing for higher-resolution simulations.

* **Flexibility**: Unstructured meshes can easily adapt to different features like coastlines and mountains without changing the grid.

* **Efficiency**: LFRic improves computational efficiency by optimizing resource use and supporting advanced parallelization.

* **Scalability**: Unstructured meshes enable higher-order methods, making it easier to scale models for larger, more detailed simulations.

To fully benefit from these features, working with unstructured data and understanding the UGRID format, which efficiently handles this type of data, is essential.
:numref:`fig-mesh-unstructured-examples` shows examples of unstructured meshes.

.. _fig-mesh-unstructured-examples:

.. figure:: /_static/unstructured_examples.png
   :width: 650px
   :alt: unstructured mesh examples

   Examples of unstructured meshes used in scientific computing.


UGRID description of unstructured data
--------------------------------------
.. _fig-mesh-ugrid-elements:

.. figure:: /_static/mesh1.png
   :align: right
   :width: 160px
   :alt: UGRID mesh elements

   UGRID mesh elements: nodes, edges, and faces

The UGRID format is more flexible than structured grids because the nodes, edges, and faces do not need to align with predefined grid lines, such as latitude or longitude.
Consequently, the spatial position of an element is independent of its position along the grid dimensions, offering a much more adaptable system.
Additionally, the UGRID format allows for mixing faces of different geometries, including 3-sided, 4-sided, 5-sided, and even n-sided faces.
This further increases the flexibility of the mesh, allowing for complex geometries that structured grids cannot accommodate.

In the context of our LFRic atmosphere unstructured mesh, all model data will be placed either on faces or edges, never on the nodes. For instance, data such as fluxes and vectors typically resides on edges, while other physical quantities are placed on faces.

Furthermore, each vertical layer shares the same horizontal coordinates, simplifying data handling across layers.

This unstructured mesh approach, which permits mixing different face geometries and the freedom to attach data to various mesh elements, demonstrates a level of flexibility that is difficult to achieve with structured grids.

To highlight the differences between unstructured and structured grids, let's consider how cells are described. In the structured grid approach, cells are described using points and bounds, defining the area between upper and lower bounds.

In the unstructured mesh approach, cells are described using a variety of elements, including faces, face centers, nodes, node centers, and edges. Each element is independently described, providing more flexibility and precision.

One key distinction is that in the mesh approach, each element is assigned its own description. In contrast, in structured grids, a single bound is used to describe the entire cell, which can lead to greater efficiency when describing certain elements (e.g., a line). However, this efficiency comes at the cost of flexibility, as the structured approach is less adaptable to complex geometries.

.. _fig-mesh-structured-vs-unstructured:

.. figure:: /_static/mesh2.png
   :width: 650px
   :alt: structured vs unstructured mesh elements

   Comparison of structured grid elements (points and bounds) versus unstructured mesh elements (faces, nodes, edges, etc.).


Managing unstructured data
--------------------------
When working with unstructured data, the amount of data to handle increases significantly. For example, imagine 5 million cells are arranged on a flat layer.
In the case of the Unified Model (UM) on the left, 13,400 data points (points and bounds) are needed to describe the entire space. However, in the unstructured case, because everything is described individually, around 40 million data points are required to represent the same space.


.. _fig-mesh-data-volume:

.. figure:: /_static/mesh3.png
   :width: 650px
   :alt: structured vs unstructured data volume

   Comparison of data volume between structured grid (right) and unstructured mesh (left) for representing the same space.

Flexibility vs. data volume
+++++++++++++++++++++++++++
To put this into perspective, imagine data is described by a newspaper. In the structured grid approach, it's like reading a pamphlet—simple and compact. In the unstructured case, however, it's like reading an entire novel. This illustrates an important concept:

.. important:: While unstructured data offers greater flexibility, it also comes with a higher data cost.

UGRID can support both 2D and 3D meshes. In the GungHo formulation, cells are 3D, and it's even possible to represent LFRic data on a 3D UGRID mesh using irregular cubes.
For example, fluxes could be represented on all six faces of a cube—four horizontal directions plus upward and downward directions. However, to minimize the amount of coordinate data and reduce processing time, we currently focus on 2D meshes for diagnostic data output, especially for typical use cases.

Complexity of operations
++++++++++++++++++++++++
Another consideration when working with unstructured data is the increased complexity of operations. In a structured grid, extracting data from a specific region is relatively simple.
For example, in :numref:`fig-mesh-data-extraction`, to extract data from rows 3 to 4 and columns 3 to 5, the array can easily be sliced to extract that data.

.. _fig-mesh-data-extraction:

.. figure:: /_static/data-extraction.png
   :width: 650px
   :alt: data extraction in structured grid

   Regional data extraction in a structured grid by slicing the array.

Extracting data in unstructured meshes
++++++++++++++++++++++++++++++++++++++
In unstructured meshes, the situation is more complex. Mesh data is one-dimensional, and there are no fixed latitude or longitude dimensions. Instead, the coordinates map to the mesh dimension. If you want to extract data from a specific region, such as a red box, the indices can be anywhere, making the operation less straightforward and requiring more computation.

Let's consider an example. To find the location of a specific element, such as a face, you need to examine its connectivity and perform an indexing operation to fetch the relevant data. This process has to be repeated for all 5 million faces in the mesh. The operation involves determining which faces are within the specified region and which are not. This is a computationally intensive task, requiring specialized libraries and powerful computing resources.

When dealing with Limited Area Models (LAMs), we focus on a smaller section of the LFRic cube-sphere. While the LFRic LAM grids may appear similar to a structured lat-lon grid on the surface (using rotated poles and grid boxes arranged into rows and columns), LFRic will output UGRID data. Therefore, the UGRID tools and operations are also applicable to LFRic LAMs.

Cubed sphere mesh
-----------------

LFRic Atmosphere uses a cubed sphere mesh. Meshes are named after the number of cells along one edge of the cube. :numref:`fig-mesh-cubed-sphere-animation` shows a C16 mesh, which represents the Earth's surface by 6 x 16 x 16 = 1536 cells ("squares") in each horizontal layer. Most cell corners have four neighbour cells but at the corners of the cube only three cells meet.

.. _fig-mesh-cubed-sphere-animation:

.. figure:: /_static/mesh_animation.gif
   :alt: C16 cubed sphere mesh projected onto a sphere

   Visualisation of a C16 mesh and how the mesh on a cube is projected to a sphere.

The projection used to map squares on a cube surface to a sphere causes mesh sizes to have different lengths in km. Representative length scales for mesh resolutions are given in the table below.

.. list-table:: Cubed Sphere Mesh Resolutions
   :header-rows: 1

   * - LFRic Mesh
     - ≈ dx [km]
   * - C48
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

As described in the previous sections, LFRic is using an unstructured cubed-sphere mesh in the UGRID format. Understanding how to effectively work with this data requires the use of specialized tools.

.. admonition:: Topic

      In this section, attention will be given to:
      the tooling available for handling UGRID data
      and how these tools fit into the broader ecosystem.

A suite of common tooling was developed within the Scientific Python ecosystem, which provides a foundation for managing and analysing complex scientific data. This toolkit includes a variety of libraries and resources designed to assist in the manipulation of unstructured data formats, such as UGRID.

.. _fig-mesh-unstructured-tools:

.. figure:: /_static/unstructured_tools.png
   :width: 650px
   :alt: unstructured data tools

   The Scientific Python Ecosystem and unstructured data tools

The main resources for the tools and standards shown in :numref:`fig-mesh-unstructured-tools` are:

* **Iris**: `Iris documentation <https://scitools-iris.readthedocs.io/>`_, `Iris on GitHub <https://github.com/SciTools/iris>`_
* **CF conventions**: `CF conventions project page <https://cfconventions.org/>`_
* **NumPy**: `NumPy documentation <https://numpy.org/doc/stable/>`_, `NumPy on GitHub <https://github.com/numpy/numpy>`_
* **Dask**: `Dask documentation <https://docs.dask.org/>`_, `Dask on GitHub <https://github.com/dask/dask>`_
* **Matplotlib**: `Matplotlib documentation <https://matplotlib.org/stable/>`_, `Matplotlib on GitHub <https://github.com/matplotlib/matplotlib>`_
* **Cartopy**: `Cartopy documentation <https://scitools.org.uk/cartopy/docs/latest/>`_, `Cartopy on GitHub <https://github.com/SciTools/cartopy>`_
* **ESMF and iris-esmf-regrid**: `ESMF project page <https://earthsystemmodeling.org/>`_, `ESMF on GitHub <https://github.com/esmf-org/esmf>`_, `iris-esmf-regrid documentation <https://iris-esmf-regrid.readthedocs.io/en/latest/>`_, `iris-esmf-regrid on GitHub <https://github.com/SciTools/iris-esmf-regrid>`_
* **PyVista**: `PyVista documentation <https://docs.pyvista.org/>`_, `PyVista on GitHub <https://github.com/pyvista/pyvista>`_
* **GeoVista**: `GeoVista documentation <https://geovista.readthedocs.io/>`_, `GeoVista on GitHub <https://github.com/bjlittle/geovista>`_
* **VTK**: `VTK project page <https://vtk.org/>`_, `VTK source repository <https://gitlab.kitware.com/vtk/vtk>`_

Despite the use of compiled languages such as Fortran and C++ in parts of the scientific Python stack, Python serves as the interface for data interaction with these tools during user workflows.

A widely used tool for handling scientific data is Iris. Iris is a powerful library that facilitates the analysis of meteorological and climate data, and it is specifically designed to work with both structured and unstructured grids. It offers a range of functions that simplify the manipulation and visualisation of data, making it a key component in many data processing workflows.

In this section, a brief overview of the basics of Iris will be provided, including its core features and functionalities.

.. _iris.basics:

Iris - basics and scope
+++++++++++++++++++++++

Iris is a Python-based ecosystem and package used for the manipulation of LFRic data during post-processing.
It is open-source and has been included in other tools, such as ESMValTool and MetPlus, which are based on it.
Iris offers a unified view of data as cubes and supports metadata-aware processing. It provides analysis capabilities in mathematics, statistics, large data handling, and regridding. For visualisation, Iris relies on Matplotlib and Cartopy.

The core of Iris is built around CF and NumPy. CF (Climate and Forecast) conventions allow Iris to work with the encoding of climate and forecast data stored in netCDF files. NumPy provides efficient array operations implemented in compiled code and linked numerical libraries, avoiding the performance limits of pure Python loops.

NumPy facilitates the mathematical operations required for large datasets. Operations involving substantial numerical processing are offloaded to efficient compiled implementations, while Python remains the user-facing interface.

Regridding unstructured data
++++++++++++++++++++++++++++

In the unstructured mesh context, `ESMF <https://earthsystemmodeling.org/>`_ (Earth System Modelling Framework) is utilised for regridding tasks. Regridding allows for comparison between datasets defined on different meshes, enabling analysis that requires data on specific local representations, such as OSGB (Ordnance Survey National Grid) in Britain, or requires computations suited to structured grids, like zonal means.

The regridding process in the unstructured world follows two primary steps: preparation and execution. During the preparation phase, the source and target grids are compared, and weights are calculated using ESMF. The preparation step is computationally intensive, particularly with unstructured grids. In the execution phase, the calculated weights are applied to the data, and a new cube is constructed. This phase typically involves Python libraries such as DASK and SciPy.

Different types of regridders are available depending on the source and target grid types. These include Mesh-to-Grid, Grid-to-Mesh, and Area-Weighted Regridders.

Each regridder offers various features, including the ability to read and write cubes, perform area-weighted regridding, and preserve metadata during operations. Additionally, the capability to load and save regridders is supported.

For datasets with masked data, the regridding process ensures that the mask is handled correctly. If the mask from the source grid covers more than a specified threshold of a target grid cell, that target cell is included in the mask. Otherwise, it is excluded from the target grid.

Key features of regridding include:

- flexibility in selecting regridders,
- the ability to preserve metadata, and
- efficient handling of masked data.

.. _fig-mesh-regrid:

.. figure:: /_static/regrid.png
   :width: 400px
   :alt: regridding data

   Regridding data from an unstructured mesh to a structured grid

The regridding tools discussed above are documented by the `ESMF user guide <https://earthsystemmodeling.org/docs/release/latest/ESMF_usrdoc/>`_, `ESMF source repository <https://github.com/esmf-org/esmf>`_, and `iris-esmf-regrid documentation <https://iris-esmf-regrid.readthedocs.io/en/latest/>`_.

Visualising unstructured data
+++++++++++++++++++++++++++++

In traditional structured grid systems, data is plotted in 2D using Matplotlib. Cartopy, a tool used for cartographic elements, assists in this process.

For unstructured grid visualisation, PyVista provides Python access to VTK's rendering and mesh-processing capabilities. VTK is a versatile toolkit implemented in C++ and can use GPU acceleration for interactive rendering. GeoVista adds geospatial and cartographic helpers on top of PyVista, performing a role similar to Cartopy for map-aware visualisation.

While Matplotlib and Cartopy have traditionally been used for structured data, these tools do not scale well and struggle to handle high-resolution unstructured meshes.

For instance, a C48 mesh has approximately 13,000 faces, and a C1048 mesh (approximately 9.55 km grid spacing at the equator) would require excessive computation and memory resources for Matplotlib and Cartopy. It would take them around 13.5s to render a C48 and 2h for a C1048! With PyVista, a C48 mesh can be rendered in 369 ms, while a C1048 mesh takes 3.87 seconds.

Unstructured visualisation tools include `VTK <https://vtk.org/>`_, a GPU-accelerated toolkit for visualisation and mesh processing, and `ParaView <https://www.paraview.org/>`_, a parallel visualisation application. PyVista provides a high-level Python interface for VTK, and GeoVista provides geospatial helpers for PyVista.

See the subsections below for detailed package summaries and links.

.. _pyvista.basics:

PyVista - basics and scope
^^^^^^^^^^^^^^^^^^^^^^^^^^

PyVista is an open-source Python library that provides a high-level interface to `VTK <https://vtk.org/>`_ (Visualization Toolkit), a powerful C++ library for 3D visualisation and mesh processing.
In the context of LFRic data, PyVista replaces Matplotlib for rendering unstructured meshes, delivering GPU-accelerated rendering that scales to high-resolution datasets.

PyVista exposes VTK's capabilities through a NumPy-friendly API, allowing scientific Python users to work with 3D geometry without writing low-level C++ code.
It supports interactive rendering in Jupyter notebooks as well as batch (off-screen) rendering for automated workflows.
PyVista also provides a rich set of mesh filters, such as slicing, contouring, and interpolation, making it suitable for both visualisation and computational geometry tasks.

The performance advantage of PyVista over Matplotlib becomes significant at LFRic resolutions: a C48 mesh (approximately 13,000 faces) renders in around 370 ms with PyVista, compared to approximately 13.5 seconds with Matplotlib, and a C1048 mesh renders in under 4 seconds rather than the roughly 2 hours Matplotlib would require.

.. _geovista.basics:

GeoVista - basics and scope
^^^^^^^^^^^^^^^^^^^^^^^^^^^

GeoVista is an open-source Python package that adds cartographic capabilities to PyVista, fulfilling a role analogous to Cartopy in the structured-grid world.
It helps transform geospatial data into PyVista meshes for interactive 3D rendering, including unstructured meshes such as cubed-sphere LFRic output.

GeoVista supports longitude-latitude data, unstructured meshes, coastline overlays, texture mapping, and regional extraction (e.g. cropping a cubed-sphere dataset to a specific geographic region).
Its current projection support is more limited than Cartopy's but includes common geographic rendering workflows and selected projected outputs.
Because GeoVista renders through PyVista and VTK, it benefits from the same rendering stack when displaying the high face-counts associated with operational LFRic resolutions.
