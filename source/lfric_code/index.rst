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

Code Repositories
-----------------
The model LFRic Atmosphere is an LFRic Science Application hosted in the `LFRic Apps <https://code.metoffice.gov.uk/trac/lfric_apps>`_ repository. LFRic Apps is the top level home for the model code of LFRic Atmosphere but also includes other `LFRic Science Applications <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications>`_, e.g. a linear model for data assimilation and an application for regridding to other LFRic meshes and creation of boundary conditions for regional model configurations. The dynamical core `GungHo <https://www.metoffice.gov.uk/research/news/2019/gungho-and-lfric>`_ of LFRic Atmosphere is part of the code in LFRic Apps.

Code for LFRic Atmosphere is not only found in LFRic Apps but also contained in the LFRic Infrastructure repository `LFRic Core <https://code.metoffice.gov.uk/trac/lfric>`_ and in repositories containing model physics. The file `dependencies.sh <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/dependencies.sh>`_ defines included science code versions from other repositories like `JULES <https://code.metoffice.gov.uk/trac/jules>`_ or `SOCRATES <https://code.metoffice.gov.uk/trac/socrates>`_.

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
