The Structured World
=====================

In a structured grid, we use 1-dimensional coordinate arrays that combine to form multi-dimensional spatial locations.
This method of organizing data allows for systematic and efficient storage of data across a spatial domain.

Consider a 2-dimensional array representing geographical data in a structured grid. 
In this context, the shape of the data in the array corresponds directly to the shape of the physical space we are modeling—in this case, Earth's surface. 
Each element in the array represents a distinct location in the physical world. 

The below image visualizes this concept:

* In this 2D array, the rows represent the West to East direction, and the columns represent the North to South direction.
* Neighboring data points in the array are also neighbors in the physical space. This spatial organization simplifies how we relate computational data to real-world positions.
  
.. image:: /_static/structured_world.svg
   :width: 650px

In this model, the data axes directly align with the array axes—rows and columns. 
This alignment provides a clear, intuitive structure that makes it easy to manipulate and analyze the data.

Key Characteristics of Structured Grids
----------------------------------------
1. Data Alignment with Physical Space:
   
   The 2D array's shape and arrangement directly correspond to physical space, useful for weather simulations and environmental modeling.

2. Neighboring Relationships:
   
   Adjacent points in the data array are also spatial neighbors, important for interpolation, integration, and modeling interactions.

3. Predictable Layout:
   
   The grid is arranged in a regular pattern (e.g., latitude-longitude or Cartesian coordinates), simplifying computational operations due to predictable relationships between data points.

Challenges with Structured Grids
---------------------------------
While structured grids work well in many cases, they do have some limitations:

1.	Singularities at the Poles: 

   One of the most well-known issues with structured grids, particularly in Earth-system modeling, is the singularity at the poles. At the North and South Poles, grid cells become excessively compressed, leading to inaccuracies and computational challenges. This is a direct result of representing a spherical Earth with a flat grid, which leads to distortion near the poles.

2.	Limited Flexibility: 

   The structured grid approach is less flexible in handling complex geometries and topologies. When trying to represent regions of interest that do not align well with the grid, or when working with more complex meshes, structured grids fall short.

The Cubed-Sphere Grids
----------------------
The cubed-sphere grid overcomes issues like singularities by dividing the Earth's surface into six square faces, which are then mapped onto a sphere. 
This approach removes polar singularities and provides an even distribution of data points, preventing excessive compression near the poles, leading to more accurate and stable computations.
However, it brings new challenges in efficiently organizing and representing the data, as assigning a 2-dimensional format can be difficult due to its non-standard layout. 
This is where the concept of meshes comes into play.