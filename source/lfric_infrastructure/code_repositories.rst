Code Repositories
=================

The LFRic codebase is distributed across several repositories:

`LFRic Core Repository`_:
  Essential building blocks such as function spaces, solvers,
  matrix operations, clock and calendar code, and diagnostics. 
`LFRic Apps Repository`_:
  The top-level repository for the LFRic Atmosphere model and other
  LFRic science applications. It includes:
  * The dynamical core `GungHo`_.
  * The main `Model Physics`_ of LFRic Atmosphere.
Large Science repositories:
  Which contain larger, modular components (e.g. land surface models).
  These are stored in their own repositories for modularity but are compiled
  with LFRic Atmosphere as one single executable. The versions of the codes
  from these repositories used in LFRic Atmosphere are defined in
  `LFRic dependencies`_ and LFRic Apps code provides `LFRic interfaces`_ to
  these science packages:

  .. list-table:: Science code included in LFRic Atmosphere with individual repositories.
    :header-rows: 1

    * - Science Code
      - Description
    * - `CASIM repository`_
      - Cloud and aerosol microphysics
    * - `JULES repository`_
      - Land surface model, including surface fluxes, hydrology, carbon
        cycle, and vegetation
    * - `SOCRATES repository`_
      - Radiative transfer scheme
    * - `UKCA repository`_
      - Chemistry and aerosols model
