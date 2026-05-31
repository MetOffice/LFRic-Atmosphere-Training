LFRic Atmosphere features and history
=====================================

LFRic Atmosphere has been `developed <https://www.metoffice.gov.uk/research/news/2019/gungho-and-lfric>`_ by the Met Office and partners to replace the Unified Model. 
While LFRic Atmosphere inherited its physics parameterisations from the Unified Model, it also introduces major advances in grid structure, numerical methods, and software design.

LFRic Atmosphere incorporates several established scientific components, including:

* `JULES <https://jules.jchmr.org/about>`_ - the land surface model,
* `SOCRATES repository`_ - the radiative transfer scheme,
* `CASIM <https://code.metoffice.gov.uk/trac/monc/wiki/CASIMDocStart>`_ - the cloud and aerosol microphysics scheme,
* `UKCA <https://www.metoffice.gov.uk/research/approach/collaboration/jwcrp/ukca>`_ - the atmospheric chemistry and aerosol model.

Like the Unified Model, LFRic Atmosphere uses terrain-following vertical coordinates, which allow the model grid to represent the Earth’s surface more accurately. However, LFRic Atmosphere also introduces several important innovations:

* A **cubed-sphere mesh**, a grid structure designed to avoid numerical problems near the poles that occur in traditional latitude–longitude grids,
* The **GungHo** mixed finite-element dynamical core,
* A modern software infrastructure designed for future high-performance computing architectures.

The new software infrastructure separates the scientific description of the atmosphere from the technical details of parallel 
computing and hardware optimisation. This makes the model easier to maintain, improves portability across different computing platforms, and supports efficient scaling to future exascale supercomputers.

.. _fig-intro-mesh-vertical:

.. figure:: /_static/1/lfric_mesh_and_vertical_grid.png
   :width: 650px
   :alt: lfric mesh and vertical grid

   Cubed sphere mesh and terrain-following vertical coordinates used by LFRic Atmosphere.

