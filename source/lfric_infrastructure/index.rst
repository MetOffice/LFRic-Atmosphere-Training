**************************
3. LFRic code and software
**************************

In this section, LFRic is introduced from a software perspective,
focusing on the LFRic Atmosphere model and its underlying
components.

.. admonition:: In this module you will learn about...

   * how LFRic Atmosphere fits within the wider LFRic software stack
     and the Momentum Framework;
   * how the LFRic codebase is split across LFRic Core, LFRic Apps,
     and larger science component repositories;
   * how the PSyKAl architecture and PSyclone separate scientific
     code from parallelisation, data movement, and performance
     concerns;
   * which development tools and repositories you need to work with
     LFRic source code, configurations, and tests;
   * where the LFRic working practices are documented, including
     guidance on issues, branches, testing, reviews, and
     multi-repository development;
   * where to find support when you are unsure how to apply the
     working practices;
   * how model output is controlled through XIOS and the
     ``iodef.xml`` configuration file.

.. admonition:: At the end of this module you should be able to...

   * describe the main LFRic code repositories and identify which
     parts of the model they contain;
   * recognise the role of LFRic Apps, LFRic Core, science component
     repositories, dependencies, and interfaces in a model build;
   * explain, at a high level, how the algorithm, kernel, and PSy
     layers fit together in the PSyKAl approach;
   * find the appropriate working-practice guidance before creating
     issues, branches, tests, reviews, or multi-repository changes;
   * identify the support routes for questions about LFRic
     development and working practices;
   * follow the practical workflow for checking out code, compiling,
     running a simple configuration, making a small change, and using
     tests as evidence;
   * locate and modify ``iodef.xml`` to control which fields are
     written, at what frequency, and to which output files.

.. _LFRic Development Environment: https://code.metoffice.gov.uk/trac/lfric/wiki/DevelopmentEnvironment

.. _lfric-platform-prerequisites:

Platform and prerequisites
==========================

The practical pages in this module assume access to a prepared Unix-like
development platform that can build and run LFRic Atmosphere. They are not a
from-a-clean-operating-system installation guide.

At the Met Office, use the managed LFRic training environment and load the
supported module stack as shown in :ref:`practical_3.1`:

.. code-block:: console

   ml use ~lfricadmin/lmod
   ml lfric

That module stack selects the compiler, MPI implementation, Python tools,
PSyclone, and supporting scientific libraries used by the practicals.
Where a course uses Azure Spice, treat it as this prepared Met Office platform
route rather than as a portable installation requirement.

On partner or external platforms, follow your site's `LFRic Development Environment`_
documentation to provide an equivalent environment before starting the
practicals. The exact compiler and library versions are platform-specific and
are owned by the supported LFRic build environment and repository dependency
files rather than by this training course. The ``Partner`` tabs in the
practicals identify where local site instructions are expected.

.. list-table:: Tools and access expected by this module
   :header-rows: 1

   * - Requirement
     - Used for
     - How to obtain it
   * - Unix-like shell environment
     - Checking out code, running commands, inspecting logs, and launching
       workflows.
     - Use the Met Office managed LFRic environment or an equivalent
       site-supported Linux or HPC environment.
   * - Git and GitHub repository access
     - Cloning LFRic Apps, the example workflow, and any training branches.
     - Follow your site's GitHub access guidance. Met Office and partner tabs
       give the repository URLs used by each practical.
   * - Fortran/C/C++ build toolchain, MPI, NetCDF/HDF5, and build utilities
     - Compiling the atmosphere executable and linked science components.
     - Use the ``lfric`` module stack at the Met Office, or the toolchain
       documented for your supported LFRic platform.
   * - Python and PSyclone
     - Running build scripts and generating PSy-layer Fortran from LFRic
       source.
     - Use the supported LFRic build environment for your platform.
   * - Rose, Cylc, and FCM
     - Running workflows, managing configurations, and running stem tests.
     - Use the Met Office module stack or your site's workflow tooling
       installation.
   * - MOSRS and, where required, SVN access
     - Working with shared Met Office repositories and legacy repository
       workflows used by some development practices.
     - Request access through your Met Office or partner support route before
       attempting those exercises.

.. important::

   The development environment in this repository's README is for building
   these training pages with Sphinx. It does not provide the full compiler,
   workflow, and runtime stack needed to build or run LFRic Atmosphere.

Before starting the practical exercises, check that your platform can clone the
required repositories, load the LFRic build environment, and run ``git``,
``python``, ``rose``, ``cylc``, ``fcm``, and the required compiler commands. If
one of those checks fails, use your local platform documentation or support
route before continuing.


.. toctree::
   :maxdepth: 1
   :caption: Contents

   code_repositories.rst
   psykal_infrastructure.rst
   working_practices.rst
   output_control.rst
   practical_exercises.rst

