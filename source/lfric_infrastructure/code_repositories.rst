Code Repositories
=================

LFRic Atmosphere is built from several GitHub repositories. The
`LFRic Apps Repository`_ is the home for LFRic-based science applications and
libraries, including the Momentum Atmosphere model application and the GungHo
dynamical core. Those applications are based on infrastructure provided by
`LFRic Core Repository`_. Larger science packages are kept in their own
repositories and are pulled into an atmosphere build through the versions
recorded in `LFRic dependencies`_.

Repository map
--------------

.. list-table::
   :header-rows: 1

   * - Repository or area
     - What it contains
     - When you are likely to use it
   * - `LFRic Apps Repository`_
     - The home for LFRic-based science applications and libraries, including
       the Momentum Atmosphere model application and the GungHo dynamical core.
       These applications use the infrastructure developed in
       `LFRic Core Repository`_.
     - Start here when working with the atmosphere model, science application
       configurations, or practical examples in this training.
   * - `LFRic Core Repository`_
     - The underlying infrastructure for the Momentum Atmosphere model and
       associated applications.
     - Use this when a change belongs in the shared LFRic infrastructure rather
       than in the atmosphere model or another science application.
   * - Science component repositories
     - Larger science packages such as CASIM, JULES, SOCRATES, and UKCA. These
       are versioned independently and connected to LFRic Atmosphere through
       dependencies and interfaces.
     - Check these when a change is in a separately maintained science package
       rather than in LFRic Apps or LFRic Core.

LFRic Apps and science applications
-----------------------------------

The `LFRic Apps Repository`_ is the GitHub home for LFRic-based science
applications and libraries. Its README identifies the Momentum Atmosphere model
application and the GungHo dynamical core as examples of the applications and
libraries it contains. These are built on the infrastructure developed in
`LFRic Core Repository`_.

.. list-table:: Useful LFRic Apps areas
   :header-rows: 1

   * - Link
     - What it points to
   * - `LFRic Apps applications`_
     - The application directories in LFRic Apps.
   * - `LFRic Atmosphere application`_
     - The Momentum Atmosphere model application area, including source,
       examples, metadata, build files, and optimisation material.
   * - `GungHo`_
     - The GungHo dynamical core application area, identified by the LFRic Apps
       README as one of the key LFRic-based applications.
   * - `Linear model`_
     - The linear model application area, including source, examples,
       rose-meta, and optimisation material.
   * - `LFRic to LFRic`_
     - The Lfric2Lfric miniapp area. Its documentation describes regridding
       and boundary-condition creation capabilities for LFRic meshes.
   * - `LFRic inputs`_
     - The LFRic inputs application area, including source and supporting
       scripts.
   * - `LFRic Apps science code`_
     - Science code maintained directly in LFRic Apps, including adjoint,
       GungHo, linear, physics schemes, and shared science areas.
   * - `Model Physics`_
     - The LFRic Apps physics schemes area.
   * - `LFRic interfaces`_
     - Interface code connecting LFRic Apps to coupled, JEDI LFRic, JULES,
       physics schemes, and SOCRATES interface areas.
   * - `LFRic dependencies`_
     - The dependency file that records the selected versions of external
       repositories used by a particular LFRic Apps checkout.

.. note::
   For most practical work in this training, clone and work in
   `LFRic Apps Repository`_. Move to `LFRic Core Repository`_ or a science
   component repository only when the change clearly belongs there.

Science component repositories
------------------------------

Some science packages are large enough, or shared enough, to live in their own
repositories. They are still compiled with LFRic Atmosphere into a single
executable. The versions used by a particular LFRic Apps checkout are defined
in `LFRic dependencies`_.

.. list-table:: Science code included in LFRic Atmosphere with individual repositories
   :header-rows: 1

   * - Science code
     - Description
     - Repository
   * - CASIM
     - Cloud and AeroSol Interacting Microphysics, described by its README as
       a component of the Met Office - NERC Cloud Model (MONC)
     - `CASIM repository`_
   * - JULES
     - Joint UK Land Environment Simulator: the land surface model used for
       surface fluxes, hydrology, carbon cycle, and vegetation
     - `JULES repository`_
   * - SOCRATES
     - Suite Of Community RAdiative Transfer codes based on Edwards and Slingo
     - `SOCRATES repository`_
   * - UKCA
     - United Kingdom Chemistry and Aerosols Project: a UK community
       atmospheric chemistry-aerosol model for climate and environmental
       change research
     - `UKCA repository`_

Choosing the right repository
-----------------------------

If you are unsure where a change belongs, start by asking what owns the code
you need to edit:

* model applications, atmosphere examples, LFRic science code, interfaces, and
  dependency versions usually belong in `LFRic Apps Repository`_;
* reusable infrastructure that is shared by LFRic applications usually belongs
  in `LFRic Core Repository`_;
* standalone science packages such as CASIM, JULES, SOCRATES, and UKCA usually
  belong in their own repositories, with LFRic Apps updated only where an
  interface or dependency version also needs to change.
