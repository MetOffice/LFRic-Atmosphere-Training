The unstructured world
======================

Unstructured meshes and the UGRID format represent the future of scientific data delivery.
As computational models evolve, especially in the realm of climate and weather modelling, transitioning to these new formats will be crucial for effective data handling. 
The unstructured world section will explore how unstructured data is transforming workflows, why it is important, and how scientists can adapt their practices to support these advancements.

Unstructured meshes offer greater flexibility and precision compared to structured grids, making them essential for data evaluation and verification. 
The section will explore the challenges and benefits of unstructured data and the technical details of using the UGRID format.

Features of unstructured meshes in LFRic atmosphere model
--------------------------------------------------

Thanks to its use of an unstructured mesh, LFRic atmosphere offers greater flexibility, scalability, and precision. Some benefits of using an unstructured mesh instead of a structured grid are: 

* **Improved Resolution**: Unstructured meshes provide more accurate representations of complex shapes and regions, allowing for higher-resolution simulations.

* **Flexibility**: Unstructured meshes can easily adapt to different features like coastlines and mountains without changing the grid.

* **Efficiency**: LFRic improves computational efficiency by optimizing resource use and supporting advanced parallelization.

* **Scalability**: Unstructured meshes enable higher-order methods, making it easier to scale models for larger, more detailed simulations.

To fully benefit from these features, working with unstructured data and understanding the UGRID format, which efficiently handles this type of data, is essential.
The figure below shows examples of unstructured meshes.

.. image:: /_static/unstructured_examples.png
   :width: 650px


UGRID description of unstructured data
---------------------------------------
.. image:: /_static/mesh1.png
   :align: right
   :width: 160px

This UGRID format is more flexible than structured grids because the nodes, edges, and faces do not need to align with predefined grid lines, such as latitude or longitude. 
Consequently, the spatial position of an element is independent of its position along the grid dimensions, offering a much more adaptable system. 
Additionally, the UGRID format allows for mixing faces of different geometries, including 3-sided, 4-sided, 5-sided, and even n-sided faces. 
This further increases the flexibility of the mesh, allowing for complex geometries that structured grids cannot accommodate.

In the context of our LFRic atmosphere unstructured mesh, all model data will be placed either on faces or edges, never on the nodes. For instance, data such as fluxes and vectors typically resides on edges, while other physical quantities are placed on faces. 
Furthermore, each vertical layer shares the same horizontal coordinates, simplifying data handling across layers.

This unstructured mesh approach, which permits mixing different face geometries and the freedom to attach data to various mesh elements, demonstrates a level of flexibility that is difficult to achieve with structured grids.

To highlight the differences between unstructured and structured grids, let's consider how cells are described. In the structured grid approach, cells are described using points and bounds, defining the area between upper and lower bounds.

In the unstructured mesh approach, cells are described using a variety of elements, including faces, face centers, nodes, node centers, and edges. Each element is independently described, providing more flexibility and precision.

One key distinction is that in the mesh approach, each element is assigned its own description. In contrast, in structured grids, a single bound is used to describe the entire cell, which can lead to greater efficiency when describing certain elements (e.g., a line). However, this efficiency comes at the cost of flexibility, as the structured approach is less adaptable to complex geometries.

.. image:: /_static/mesh2.png
   :width: 650px

Managing unstructured data
---------------------------
When working with unstructured data, the amount of data to handle increases significantly. For example, imagine 5 million cells are arranged on a flat layer,
in the case of the Unified Model (UM) on the left, 13,400 data points (points and bounds) are needed to describe the entire space. However, in the unstructured case, because everything is described individually, around 40 million data points are required to represent the same space.


.. image:: /_static/mesh3.png
   :width: 650px

Flexibility vs. data volume
++++++++++++++++++++++++++++
To put this into perspective, imagine data is described by a newspaper. In the structured grid approach, it's like reading a pamphlet—simple and compact. In the unstructured case, however, it's like reading an entire novel. 
This illustrates that while unstructured data offers greater flexibility, it also comes with a higher data cost.

UGRID can support both 2D and 3D meshes. In the GungHo formulation, cells are 3D, and it's even possible to represent LFRic data on a 3D UGRID mesh using irregular cubes. 
For example, fluxes could be represented on all six faces of a cube—four horizontal directions plus upward and downward directions. However, to minimize the amount of coordinate data and reduce processing time, we currently focus on 2D meshes for diagnostic data output, especially for typical use cases.

Complexity of operations
+++++++++++++++++++++++++
Another consideration when working with unstructured data is the increased complexity of operations. In a structured grid, extracting data from a specific region is relatively simple. 
For example in the below figure, to extract data from rows 3 to 4 and columns 3 to 5, the array can easily be sliced to extract that data.

.. image:: /_static/data-extraction.png
   :width: 650px

Extracting data in unstructured meshes
+++++++++++++++++++++++++++++++++++++++
In unstructured meshes, the situation is more complex. Mesh data is one-dimensional, and there are no fixed latitude or longitude dimensions. I
nstead, the coordinates map to the mesh dimension. If you want to extract data from a specific region, such as a red box, the indices can be anywhere, making the operation less straightforward and requiring more computation.

Let’s consider an example. To find the location of a specific element, such as a face, you need to examine its connectivity and perform an indexing operation to fetch the relevant data. This process has to be repeated for all 5 million faces in the mesh. The operation involves determining which faces are within the specified region and which are not. This is a computationally intensive task, requiring specialized libraries and powerful computing resources.

When dealing with Limited Area Models (LAMs), we focus on a smaller section of the LFRic cube-sphere. While the LFRic LAM grids may appear similar to a structured lat-lon grid on the surface (using rotated poles and grid boxes arranged into rows and columns), LFRic will output UGRID data. Therefore, the UGRID tools and operations are also applicable to LFRic LAMs.

Cubed sphere mesh
-----------------

LFRic Atmosphere uses a cubed sphere mesh. Meshes are named after the number cells along one edge of the cube. The visualisation shows an C16 mesh, which represents the Earth surface by 6 x 16 x 16 = 1536 cells ("squares") in each horizontal layer. Most cell corners have four neighbour cells but at the corners of the cube only three cells meet.

.. video:: /_static/mesh_animation.mp4
   :loop:
   :align: center
   :caption: Visualisation of a C16 mesh and how the mesh on a cube is projected to a sphere.

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

As described in the previous sections, LFRic is using an unstructured mesh - cubed-sphere mesh - in the UGRID format. Understanding how to effectively work with this data requires the use of specialized tools. In this section, attention will be given to the tooling available for handling UGRID data and how these tools fit into the broader ecosystem.

A suite of common tooling was developed within the Scientific Python ecosystem, which provides a foundation for managing and analysing complex scientific data. This toolkit includes a variety of libraries and resources designed to assist in the manipulation of unstructured data formats, such as UGRID.

A widely used tool for handling scientific data is Iris. Iris is a powerful library that facilitates the analysis of meteorological and climate data, and it is specifically designed to work with both structured and unstructured grids. It offers a range of functions that simplify the manipulation and visualization of data, making it a key component in many data processing workflows.

In this session, a brief overview of the basics of Iris will be provided, including its core features and functionalities. 


.. image:: /_static/unstructured_tools.png
   :width: 650px

Regridding unstructured data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /_static/regrid.png
   :width: 400px

Visualising unstructured data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
