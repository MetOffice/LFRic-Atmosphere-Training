LFRic Atmosphere features and history
=====================================

LFRic Atmosphere has been `developed <https://www.metoffice.gov.uk/research/news/2019/gungho-and-lfric>`_ by the   Met Office and partners to replace the Unified Model. LFRic Atmosphere inherited its physics parameterisations     from the Unified Model. It uses the land surface model `JULES <https://jules.jchmr.org/about>`_, radiative         transfer code `SOCRATES <https://code.metoffice.gov.uk/trac/socrates>`_, Cloud and Aerosol Interacting             Microphysics `CASIM <https://code.metoffice.gov.uk/trac/monc/wiki/CASIMDocStart>`_ and the chemistry and aerosols  model `UKCA <https://www.metoffice.gov.uk/research/approach/collaboration/jwcrp/ukca>`_.

LFRic Atmosphere uses same the terrain following vertical coordinates as the Unified Model but has a cubed sphere  mesh, a new mixed finite-element dynamical core GungHo and a new coding infrastructure structure. The cubed sphere mesh avoids the pole singularity problem of lon/lat grids which prohibits scaling the Unified Model to km scale    global grids. The coding infrastructure seperates details of code parallelisation from the mathematical            formulation of physical representation of the atmosphere. This separation of concerns allows for easier            optimisation of the same model code for different compute platforms.

.. figure:: /_static/lfric_mesh_and_vertical_grid.png
   :width: 650px
   :alt: lfric mesh and vertical grid

   Cubed sphere mesh and terrain following vertical coordinates used by LFRic Atmosphere.

