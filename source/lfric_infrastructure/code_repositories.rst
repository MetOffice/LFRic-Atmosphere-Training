Code Repositories
=================

Code is distributed across several repositories. The LFRic Infrastructure repository `LFRic Core <https://code.metoffice.gov.uk/trac/lfric>`_ contains function spaces, solvers, matrix operations, clock and calendar code, and diagnostics. The top-level repository for the model LFRic Atmosphere is the `LFRic Apps <https://code.metoffice.gov.uk/trac/lfric_apps>`_ repository, which also includes other LFRic Science Applications. It contains the dynamical core `GungHo <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/science/gungho/source>`_ and the main model `physics <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/science/physics_schemes/source>`_ of LFRic Atmosphere. Larger science packages, such as the land surface model, are stored in their own repositories for modularity but are compiled with LFRic Atmosphere as one single executable. The versions of the codes from these repositories used in LFRic Atmosphere are defined in `dependencies.sh <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/dependencies.sh>`_. LFRic Apps code includes `interfaces <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/interfaces>`_ to these science packages.


.. list-table:: Science code included in LFRic Atmosphere with individual repositories.
   :header-rows: 1

   * - Science Code
     - Description
   * - `CASIM <https://code.metoffice.gov.uk/trac/monc/wiki/CASIMDocStart>`_
     - Cloud and aerosol microphysics
   * - `JULES <https://code.metoffice.gov.uk/trac/jules>`_
     - Land surface model, including surface fluxes, hydrology, carbon cycle, and vegetation
   * - `SOCRATES <https://code.metoffice.gov.uk/trac/socrates>`_
     - Radiative transfer scheme
   * - `UKCA <https://code.metoffice.gov.uk/trac/ukca>`_
     - Chemistry and aerosols model

