**********************************
The structured world - review quiz
**********************************

The following quiz reviews key concepts introduced in this chapter. Each question is designed to assess comprehension of the material in a focused and practical manner.

.. hint::
    Unless otherwise specified, each question has only one correct answer.

.. quizdown::

   ---
   shuffleQuestions: true
   shuffleAnswers: true
   ---

   ## What is a structured grid?
   1. [x] A grid where 1D coordinate arrays are combined to form multi-dimensional spatial locations
       > Correct!
   1. [ ] A random arrangement of spatial data with no pattern
       > A structured grid, by definition, has an ordered and predictable pattern—not a random arrangement.
   1. [ ] A grid where each point represents time instead of space
       > Structured grids represent spatial—not temporal—locations.
   1. [ ] A grid based on unstructured data relationships
       > This describes an unstructured grid, not a structured one.

   ## In a structured 2D grid representing Earth's surface, what direction do rows typically represent?
   1. [ ] South to North
       > Columns represent longitude, while rows represent latitude.
   1. [ ] North to South
       > This might seem logical, but in many datasets, rows increase from top to bottom—West to East.
   1. [x] West to East
       > Correct! In structured 2D Earth grids, rows span from West to East.
   1. [ ] East to West
       > Rows increase from West to East, so this is incorrect.

   ## Why are structured grids considered intuitive for modelling physical space?
   1. [x] The physical location on Earth relates directly to the location within the data array on
       > Correct! This is what makes structured grids easy to use.
   1. [ ] They use random placement to approximate locations
       > Random placement is a characteristic of unstructured grids.
   1. [ ] They rely on machine learning to guess spatial relationships
       > Structured grids don't need ML—they use clear spatial indexing.
   1. [ ] They avoid spatial mapping for simpler performance
       > Spatial mapping is central to the design of structured grids, not something to be avoided.

   ## Which of the following is NOT a key characteristic of structured grids?
   1. [ ] Predictable layout
       > This is a defining feature of structured grids.
   1. [ ] Neighbouring data points are spatial neighbours
       > This is true for structured grids—they follow consistent spatial relationships.
   1. [x] Arbitrary placement of grid cells
       > Correct! Arbitrary placement defines unstructured grids.
   1. [ ] Alignment with physical space
       > Structured grids mirror physical layouts.

   ## What major issue occurs with structured grids near the Earth's poles?
   1. [ ] The grid becomes non-deterministic
       > No, they remain deterministic but suffer from distortion.
   1. [x] Grid cells compress, leading to singularities and inaccuracies
       > Correct! This compression leads to problematic singularities in structured grids.
   1. [ ] The grid becomes too sparse for accurate modelling
       > The opposite happens—points become too close together.
   1. [ ] Latitudes disappear near the poles
       > Incorrect! grids suffer from distortion.

   ## What are some solutions to the problem of polar singularities in structured grids? (select all that apply)
   - [ ] Using larger grid cells near the poles
      > This doesn't solve the singularity problem.
   - [x] Switching to an unstructured mesh like the cubed-sphere
      > Correct! Cubed-sphere meshes eliminate pole singularities.
   - [ ] Ignoring data near the poles
      > Not a viable solution—this just discards valuable data.
   - [ ] Replacing grid points with 3D coordinates
      > Changing coordinate representation doesn't remove pole distortion.
   - [x] Describing a reduced (or thinned) Gaussian grid as used at European Centre for Medium-Range Weather Forecasts  (ECMWF)
      > Correct! Thinned grids reduce grid point density near the poles to manage singularities.
   - [x] Rotating the pole
      > Correct! Pole rotation can shift singularities away from important analysis areas.

   ## What is a challenge of using cubed-sphere unstructured meshes?
   1. [ ] They reintroduce polar singularities
       > Incorrect. Cubed-sphere grids solve the polar singularity problem.
   1. [x] Organising data in a 2D format becomes more difficult
       > Correct! The face-based structure complicates 2D array representation.
   1. [ ] They increase distortion near the equator
       > Distortion is relatively minimal near the equator.
   1. [ ] They are less accurate than structured grids
       > This is not generally true—unstructured grids can be highly accurate.
