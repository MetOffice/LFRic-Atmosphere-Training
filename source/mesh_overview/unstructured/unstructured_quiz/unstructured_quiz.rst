*************************************
The unstructured world - review quiz
*************************************

This quiz reviews the main ideas from the chapter.

.. hint::
    Each question has only one correct answer.

.. quizdown::

   ---
   shuffleQuestions: true
   shuffleAnswers: true
   ---

   ## What is the main reason for moving from structured to
   unstructured meshes in climate and weather models?
   1. [ ] Simpler array indexing
       > No. Unstructured meshes complicate indexing compared to
       structured ones.
   1. [ ] Compatibility with Excel
       > Excel compatibility is irrelevant in this context.
   1. [x] Increased flexibility and precision
       > Correct! They offer adaptive resolution and better fit for
       irregular domains.
   1. [ ] Reduced data storage size
       > No. Unstructured grids often require more metadata, not less.
   1. [ ] Compatibility with point data in Geographic information
      System
       > While relevant, it’s not the primary reason for the
       transition.

   ## Is this sentence true or false: The UGRID format forces data to
   align with predefined latitude-longitude grid lines.
   1. [ ] true
       > Incorrect! UGRID supports flexible, irregular grid
       representations.
   1. [x] false
       > Correct! UGRID supports flexible, irregular grid
       representations.

   ## In LFRic, where is model data placed in the unstructured mesh?
   1. [ ] Only on nodes
       > LFRic uses more than just nodes for data placement.
   1. [ ] Only on edges
       > Edges alone don’t provide enough flexibility or resolution.
   1. [x] On faces and edges
       > Correct! Data is placed on both faces and edges.
   1. [ ] Randomly assigned
       > Incorrect! Placement is carefully structured even in
       unstructured meshes.

   ## What does each element in an unstructured mesh (e.g., node,
   edge, face) have that differs from structured grids?
   1. [x] Each element has its own independent description of
      geographic location
       > Correct! Unlike structured grids, unstructured grids
       explicitly define each element’s location.
   1. [ ] All of them have the same size
       > Incorrect! Unstructured grids support variable cell sizes.
   1. [ ] All of them have the same shapes
       > No, they can vary in shape depending on geometry needs.

   ## Why does an unstructured mesh usually require more coordinate
   and connectivity data than a structured grid for the same domain?
   1. [ ] The mesh is forced to align with latitude-longitude grid
      lines
       > Incorrect. UGRID removes that fixed alignment, which is one
       reason the mesh needs explicit geometry and connectivity.
   1. [x] Each mesh element and its relationships must be described
      explicitly
       > Correct! The flexibility comes from storing the locations of
       mesh elements and how they connect, rather than deriving
       positions from regular array indices.
   1. [ ] The same bounds can be reused for every cell
       > No. Reusing regular bounds is closer to the structured-grid
       case.
   1. [ ] Unstructured meshes avoid storing edges and faces
       > Incorrect. Nodes, edges, faces, and connectivity are central
       to describing UGRID meshes.

   ## Is the following sentence true or false: Unstructured meshes
   reduce the amount of coordinate data needed compared to structured
   grids.
   1. [x] false
       > Correct! More coordinate data is needed for flexibility and
       accuracy.
   1. [ ] true
       > Incorrect! More coordinate data is needed for flexibility
       and accuracy.

   ## What does the newspaper analogy illustrate about structured and
   unstructured data?
   1. [x] Unstructured data can describe the domain in more detail,
      but that detail comes with a higher data cost.
       > Correct! The comparison is about the trade-off between
       compact regular structure and richer explicit description.
   1. [ ] Unstructured data is always smaller because it avoids
      metadata.
       > Incorrect. Unstructured data usually needs additional
       geometry and connectivity information.
   1. [ ] Structured data is more flexible because every element is
      described independently.
       > No. Independent element descriptions are a feature of the
       unstructured approach.
   1. [ ] Structured and unstructured data have the same storage and
      processing costs.
       > Incorrect. The chapter highlights important differences in
       data volume and processing complexity.

   ## A cubed-sphere Cn mesh has 6 x n x n horizontal cells. What
   happens to the horizontal cell count when n is doubled from C16 to
   C32?
   1. [ ] It stays the same because there are still six cube faces
       > Incorrect. The number of cube faces stays the same, but each
       face is subdivided into more cells.
   1. [ ] It doubles
       > Not quite. The cell count depends on n squared, so doubling
       n has a larger effect than doubling the count.
   1. [x] It becomes four times larger
       > Correct! The count depends on n squared: 6 x 32 x 32 is four
       times 6 x 16 x 16.
   1. [ ] It becomes six times larger
       > Incorrect. The factor of six is already present in both
       meshes because both have six cube faces.

   ## The cubed-sphere resolution table shows that larger C numbers
   have smaller representative length scales. What is the practical
   implication of moving to a larger C number?
   1. [ ] The mesh becomes coarser, so there are fewer elements to
      process.
       > Incorrect. Larger C numbers represent finer meshes, not
       coarser ones.
   1. [x] The mesh becomes finer, so post-processing and
      visualisation usually handle more elements.
       > Correct! Finer meshes provide more spatial detail, but they
       also increase the amount of data and computational work.
   1. [ ] The mesh stops being unstructured and becomes a
      latitude-longitude grid.
       > Incorrect. Increasing the C number changes the mesh
       resolution, not the underlying mesh type.
   1. [ ] Regridding is no longer required because all datasets use
      the same mesh.
       > No. Different datasets can still be defined on different
       meshes or grids.

   ## What is the role of Iris in the context of UGRID data?
   1. [ ] GPU rendering
       > No. This is not Iris’s function.
   1. [x] Mathematical and statistical analysis
       > Correct! Iris is a Python library for analyzing Earth
       science data.
   1. [ ] File compression
       > Iris is not a compression utility.
   1. [ ] Cloud storage
       > Cloud storage is unrelated to Iris’s core functionality.

   ## Is the following sentence true or false: PyVista and GeoVista
   are preferred over Matplotlib for high-resolution unstructured
   mesh visualisation.
   1. [x] true
       > Correct! PyVista and GeoVista handle complex mesh geometry
       better.
   1. [ ] false
       > Matplotlib lacks native support for unstructured 3D mesh
       visualization.

   ## What is Iris used for?
   1. [ ] Cartographic visualisation for unstructured data
       > No. Iris focuses more on analysis than mapping.
   1. [x] Earth Science data processing
       > Correct! Iris helps process, analyze, and transform
       scientific datasets.
   1. [ ] 3D mesh visualisation and GPU acceleration
       > These are handled by tools like PyVista, not Iris.
   1. [ ] Low-level mesh and visualisation backend
       > Incorrect—this refers to libraries like VTK or GeoVista.

   ## What tool is used to compute regridding weights in the
   unstructured world?
   1. [ ] NumPy
       > NumPy is general-purpose and doesn’t support regridding
       directly.
   1. [ ] Cartopy
       > Cartopy is used for maps, not computing interpolation
       weights.
   1. [x] ESMF
       > Correct! ESMF (Earth System Modelling Framework) handles
       regridding, especially for unstructured grids.
   1. [ ] Matplotlib
       > Matplotlib only handles plotting—not weight generation.

   ## Why is regridding more computationally expensive in
   unstructured grids?
   1. [ ] Because each element must be described individually
       > Partially correct, but there's more.
   1. [ ] Because weights must be computed for non-aligned, irregular
      shapes
       > Also true, but not the full answer.
   1. [x] Both of them
       > Correct! Describing each element and computing complex
       weights both increase the cost.
   1. [ ] None of them
       > Incorrect! Both factors are key challenges.

   ## Is the following sentence true or false: During regridding,
   metadata can be preserved using appropriate tools and
   configurations.
   1. [x] true
       > Correct! Libraries like Iris and xESMF preserve metadata
       when properly configured.
   1. [ ] false
       > Not necessarily, correct tools retain it.

