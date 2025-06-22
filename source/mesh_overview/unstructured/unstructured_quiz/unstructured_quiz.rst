*************************************
The unstructured world - review quiz
*************************************

This quiz reviews the main ideas from the chapter and tests understanding of the content through multiple choice questions.

.. hint::
    Each question has only one correct answer.

.. quizdown::

   ---
   shuffleQuestions: true
   shuffleAnswers: true
   ---

   ## What is the main reason for moving from structured to unstructured meshes in climate and weather models?
   1. [ ] Simpler array indexing
       > No. Unstructured meshes complicate indexing compared to structured ones.
   1. [ ] Compatibility with Excel
       > Excel compatibility is irrelevant in this context.
   1. [x] Increased flexibility and precision
       > Correct! They offer adaptive resolution and better fit for irregular domains.
   1. [ ] Reduced data storage size
       > No. Unstructured grids often require more metadata, not less.
   1. [ ] Compatibility with point data in Geographic information System
       > While relevant, it’s not the primary reason for the transition.

   ## Is this sentence true or false: The UGRID format forces data to align with predefined latitude-longitude grid lines.
   1. [ ] true
       > Incorrect! UGRID supports flexible, irregular grid representations.
   1. [x] false
       > Correct! UGRID supports flexible, irregular grid representations.

   ## In LFRic, where is model data placed in the unstructured mesh?
   1. [ ] Only on nodes
       > LFRic uses more than just nodes for data placement.
   1. [ ] Only on edges
       > Edges alone don’t provide enough flexibility or resolution.
   1. [x] On faces and edges
       > Correct! Data is placed on both faces and edges.
   1. [ ] Randomly assigned
       > Incorrect! Placement is carefully structured even in unstructured meshes.

   ## What does each element in an unstructured mesh (e.g., node, edge, face) have that differs from structured grids?
   1. [x] Each element has its own independent description of geographic location
       > Correct! Unlike structured grids, unstructured grids explicitly define each element’s location.
   1. [ ] All of them have the same size
       > Incorrect! Unstructured grids support variable cell sizes.
   1. [ ] All of them the same shapes
       > No, they can vary in shape depending on geometry needs.
   
   ## In an unstructured mesh with 5 million cells, approximately how many data points are required to describe the domain?
   1. [ ] 5 million
       > This underestimates the complexity—more elements are needed. Think about vertices, edges, and faces. A reasonable estimate is that around 8 data points per cell are needed, which includes: ~3–4 for edges, ~1–2 for coordinates, ~2–3 for additional metadata or spatial relationships: 5 million × 8 = 40 million data points.
   1. [ ] 13400
       > Far too low—this wouldn't even cover vertices. Think about vertices, edges, and faces. A reasonable estimate is that around 8 data points per cell are needed, which includes: ~3–4 for edges, ~1–2 for coordinates, ~2–3 for additional metadata or spatial relationships: 5 million × 8 = 40 million data points.
   1. [x] 40 million
       > Correct! Describing all nodes, edges, faces, and connectivity inflates data.
   1. [ ] 10 million
       > Incorrect! Is this enough to capture edges and faces too? Think about vertices, edges, and faces. A reasonable estimate is that around 8 data points per cell are needed, which includes: ~3–4 for edges, ~1–2 for coordinates, ~2–3 for additional metadata or spatial relationships: 5 million × 8 = 40 million data points.

   ## Is the following sentence true or false: Unstructured meshes reduce the amount of coordinate data needed compared to structured grids.
   1. [x] false
       > Correct! More coordinate data is needed for flexibility and accuracy.
   1. [ ] true
       > Incorrect! More coordinate data is needed for flexibility and accuracy.

   ## Describe the “newspaper” analogy used to compare structured and unstructured data.
   1. [x] Structured data is like a pamphlet (compact and simple), while unstructured data is like a novel (detailed and complex).
       > Correct! A pamphlet is compact and ordered, just like structured data.
   1. [ ] Structured data is like a handwritten journal, while unstructured data is like a spreadsheet with labeled rows.
       > Hint: Does this clarify complexity and structure?
   1. [ ] Structured data is like a comic book with speech bubbles, while unstructured data is like a dictionary.
       > This analogy doesn’t meaningfully reflect mesh types.
   1. [ ] Structured data is like a calendar (organized and dated), while unstructured data is like a stack of letters with no order.
       > While plausible, it’s not the analogy used here.

   ## In a C16 mesh, how many cells exist per horizontal layer?
   1. [x] 1536
       > Correct! C16 meshes have 1536 horizontal cells.
   1. [ ] 256
       > Incorrect! C16 implies higher density than 256 cells. The “C” in C16 refers to cubed-sphere grids. These grids map the surface of a sphere (like Earth) into six faces. Each face is then subdivided into a structured grid of N × N cells, where N is the resolution parameter. For a C16 mesh, this means each face has 16 × 16 = 256 cells. Since there are 6 faces, the total number of horizontal cells is: 6x16x16 = 1536.
   1. [ ] 16
       > No.This refers to resolution tier, not literal cell count. The “C” in C16 refers to cubed-sphere grids. These grids map the surface of a sphere (like Earth) into six faces. Each face is then subdivided into a structured grid of N × N cells, where N is the resolution parameter. For a C16 mesh, this means each face has 16 × 16 = 256 cells. Since there are 6 faces, the total number of horizontal cells is: 6x16x16 = 1536.
   1. [ ] 6
       > Far too low for any realistic mesh resolution. The “C” in C16 refers to cubed-sphere grids. These grids map the surface of a sphere (like Earth) into six faces. Each face is then subdivided into a structured grid of N × N cells, where N is the resolution parameter. For a C16 mesh, this means each face has 16 × 16 = 256 cells. Since there are 6 faces, the total number of horizontal cells is: 6x16x16 = 1536.

   ## Fill in the Blank: A C448 mesh has an approximate horizontal resolution of _______ km.
   1. [ ] 26.6
       > Incorrect! C448 implies higher resolution. The horizontal resolution of a C448 mesh can be approximated using the following relationship: Resolution (km)≈Earth’s circumference (km)/Total number of grid points around the equator
         Earth's circumference: Approximately 40,000 km,      
         Cubed-sphere structure: There are 6 faces of a cube, each face has N × N grid cells, where N = 448 for C448.
         These faces are arranged so that there are effectively 4N grid points wrapping around the equator.
         Number of grid cells around the equator: 4×𝑁=4×448=1792.          
         Resolution estimate: 40,000 km/1792 ≈ 22.3 km.  
         However, due to projection effects, the effective resolution is often slightly better than this estimate, so a C448 mesh has an approximate horizontal resolution of 20.6 km. 
   1. [ ] 16.2
       > Too fine for C448. The horizontal resolution of a C448 mesh can be approximated using the following relationship: Resolution (km)≈Earth’s circumference (km)/Total number of grid points around the equator
         Earth's circumference: Approximately 40,000 km,      
         Cubed-sphere structure: There are 6 faces of a cube, each face has N × N grid cells, where N = 448 for C448.
         These faces are arranged so that there are effectively 4N grid points wrapping around the equator.
         Number of grid cells around the equator: 4×𝑁=4×448=1792.          
         Resolution estimate: 40,000 km/1792 ≈ 22.3 km.  
         However, due to projection effects, the effective resolution is often slightly better than this estimate, so a C448 mesh has an approximate horizontal resolution of 20.6 km. 
   1. [ ] 36.2
       > Incorrect! C448 implies higher resolution. The horizontal resolution of a C448 mesh can be approximated using the following relationship: Resolution (km)≈Earth’s circumference (km)/Total number of grid points around the equator
         Earth's circumference: Approximately 40,000 km,      
         Cubed-sphere structure: There are 6 faces of a cube, each face has N × N grid cells, where N = 448 for C448.
         These faces are arranged so that there are effectively 4N grid points wrapping around the equator.
         Number of grid cells around the equator: 4×𝑁=4×448=1792.          
         Resolution estimate: 40,000 km/1792 ≈ 22.3 km.  
         However, due to projection effects, the effective resolution is often slightly better than this estimate, so a C448 mesh has an approximate horizontal resolution of 20.6 km. 
   1. [x] 20.6
       > Correct! C448 approximates 20.6 km horizontal resolution.

   ## What is the role of Iris in the context of UGRID data?
   1. [ ] GPU rendering
       > No. This is not Iris’s function.
   1. [x] Mathematical and statistical analysis
       > Correct! Iris is a Python library for analyzing Earth science data.
   1. [ ] File compression
       > Iris is not a compression utility.
   1. [ ] Cloud storage
       > Cloud storage is unrelated to Iris’s core functionality.

   ## Is the following sentence true or false: PyVista and GeoVista are preferred over Matplotlib for high-resolution unstructured mesh visualisation.
   1. [x] true
       > Correct! PyVista and GeoVista handle complex mesh geometry better.
   1. [ ] false
       > Matplotlib lacks native support for unstructured 3D mesh visualization.

   ## What is Iris used for?
   1. [ ] Cartographic visualisation for unstructured data
       > No. Iris focuses more on analysis than mapping.
   1. [x] Earth Science data processing
       > Correct! Iris helps process, analyze, and transform scientific datasets. 
   1. [ ] 3D mesh visualisation and GPU acceleration
       > These are handled by tools like PyVista, not Iris.
   1. [ ] Low-level mesh and visualisation backend
       > Incorrect—this refers to libraries like VTK or GeoVista.

   ## What tool is used to compute regirding weights in the unstructured world?
   1. [ ] NumPy
       > NumPy is general-purpose and doesn’t support regridding directly.
   1. [ ] Cartopy
       > Cartopy is used for maps, not computing interpolation weights.
   1. [x] ESMF
       > Correct! ESMF (Earth System Modeling Framework) handles regridding, especially for unstructured grids.
   1. [ ] Matplotlib
       > Matplotlib only handles plotting—not weight generation.

   ## Why is regirding more computationally expensive in unstructured grids?
   1. [ ] Because each element must be described individually
       > Partially correct, but there's more.
   1. [ ] Because weights must be computed for non-aligned, irregular shapes
       > Also true, but not the full answer.
   1. [x] Both of them
       > Correct! Describing each element and computing complex weights both increase the cost.
   1. [ ] None of them
       > Incorrect! Both factors are key challenges.

   ## Is the following sentence true or false: During regirding, metadata can be preserved using appropriate tools and configurations.
   1. [x] true
       > Correct! Libraries like Iris and xESMF preserve metadata when properly configured.
   1. [ ] false
       > Not necessarily, correct tools retain it.

