3. LFRic code and software
==========================

.. toctree::
   :name: lfric_code
   :maxdepth: 2

In this section LFRic Atmosphere is introduced from a software perspective.

.. admonition:: Aims and objectives

   * To understand where to find the code for the model.
   * To learn how to compile the model and be aware of involved steps.
   * To become familiar with working practises required for model development.


LFRic Science Applications 
---------------------------
The LFRic Atmosphere model is a `LFRic Science Applications <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications>`_ build on top of the LFRic Infrastructure. There are also other LFRic Science Applications build with the same infrastructure code, e.g. a linear model for data assimilation and an application for regridding and creating boundary conditions.

Code Repositories
-----------------
Code is distributed across several repositories: The LFRic Infrastructure repository `LFRic Core <https://code.metoffice.gov.uk/trac/lfric>`_ contains function spaces, solvers, matrix operations, clock and calendar code, and diagnostics. The top-level repository for the model LFRic Atmosphere is the `LFRic Apps <https://code.metoffice.gov.uk/trac/lfric_apps>`_ repository, which also includes other LFRic Science Applications. It contains the dynamical core `GungHo <https://www.metoffice.gov.uk/research/news/2019/gungho-and-lfric>`_ and the main model physics of LFRic Atmosphere. Larger science packages, such as the land surface model, are stored in their own repositories for modularity but compiled with LFRic Atmosphere as one single executable. The versions of the codes from theses repositories used in LFRic Atmosphere are defined in `dependencies.sh <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/dependencies.sh>`_.

.. list-table:: Science codes included in LFRic Atmosphere with individual repositories.
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
   
PSyKAl and PSyclone
-------------------
LFRic uses a domain specific language to separate computational science from natural science in the programming. The software architecture to do this is called `PSyKAl <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html>`_, which stands for `Parallel System <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#psy-layer>`_, `Kernel <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#kernel-layer>`_, and `Algorithm <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#algorithm-layer>`_.

Scientific operations on full field are implemented in the Algorithm layer. Kernels specify operations for vertical columns. Parallelism is implemented in the Parallel System layer which is auto generated with a tool called `PSyclone <https://psyclone.readthedocs.io/en/stable/>`_.

.. figure:: /_static/psykal.png
  :width: 650px

  Separation of Natural and Computational Science in the PSyKAl architecture.

Practical 1: Model Build
------------------------

Check out the source code and run lfric_atm_developer `rose stem test <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html>`_ and the related `Cylc <https://cylc.github.io/cylc-doc/latest/html/index.html>`_ workflow to compile the model:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 4,5
   
   fcm co fcm:lfric_apps.x_tr lfric_apps_tr
   cd lfric_apps_tr
   export CYLC_VERSION=8
   rose stem --group=lfric_atm_developer
   cylc play <working copy name>
   cylc gui




Practical 2: Code Change
------------------------
