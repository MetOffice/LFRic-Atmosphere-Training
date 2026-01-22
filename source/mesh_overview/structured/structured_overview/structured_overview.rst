********************
The structured world
********************

In a structured grid, 1-dimensional coordinate arrays are combined to form multi-dimensional spatial locations.
Organising data in this manner allows for systematic and efficient storage of data across a spatial domain.

Consider a 2-dimensional array representing geographical data in a structured grid.
In this context, the shape of the data in the array corresponds directly to the shape of the physical space we are modelling—in this case, Earth's surface.
Each element in the array represents a distinct location in the physical world.

The figure below visualises this concept:

* In the 2D array below, the rows represent the West to East direction, and the columns represent the South to North direction.
* Neighbouring data points in the array are also neighbours in the physical space. This spatial organisation simplifies how we relate computational data to real-world positions.
* The alignment between data points and physical space provides a clear, intuitive structure that makes it easy to manipulate and analyse the data.

.. figure:: /_static/structured_world.svg
   :width: 650px
   :alt: structured world
   
   Representation of a structured grid illustrating the direct correspondence between array indices and physical space.


Key characteristics of structured grids
---------------------------------------
1. Data alignment with physical space:

   The 2D array's shape and arrangement directly correspond to physical space, useful for weather simulations and environmental modelling.

2. Neighbouring relationships:

   Adjacent points in the data array are also spatial neighbours, important for interpolation, integration, and modelling interactions.

3. Predictable layout:

   The grid is arranged in a regular pattern (e.g., latitude-longitude or Cartesian coordinates), simplifying computational operations due to predictable relationships between data points.

Challenges with structured grids
--------------------------------
While structured grids work well in many cases, they do have some limitations:

1. Singularities at the poles:

   One of the most well-known issues with structured grids, particularly in Earth-system modelling, is the singularity at the poles. At the North and South Poles, grid cells become excessively compressed, leading to inaccuracies and computational challenges. This is a direct result of representing a spherical Earth with a flat grid, which leads to distortion near the poles.
   The figure below demonstrates singularities at the poles.

.. figure:: /_static/singularities.png
   :width: 300px
   :align: center
   :alt: singularities at poles
   
   Singularities occurring at the poles in structured grids due to grid cell compression.


2. Limited flexibility:

   The structured grid approach is less flexible in handling complex geometries and topologies. When trying to represent regions of interest that do not align well with the grid, or when working with more complex meshes, structured grids fall short.

How to address these challenges?
--------------------------------
Unstructured meshes overcome issues like these singularities. One example is the cubed-sphere which consists of dividing the Earth's surface into six square faces that are then mapped onto a sphere.
This approach removes polar singularities and provides an even distribution of data points, preventing excessive compression near the poles and leading to more accurate and stable computations.
However, it brings new challenges in efficiently organising and representing the data, as assigning a 2-dimensional format can be difficult due to its non-standard layout.
Let's learn more about unstructured meshes in the next section!
