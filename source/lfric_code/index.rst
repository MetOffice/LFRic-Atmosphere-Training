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
LFRic Atmosphere is an LFRic Science Application hosted in the `LFRic Apps <https://code.metoffice.gov.uk/trac/lfric_apps>`_ repository. The LFRic Apps repository is the top level home for the model code of LFRic Atmosphere but also includes other `LFRic Science Applications <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications>`_. Code for LFRic Atmosphere is not only found in LFRic Apps but also contained in the LFRic Infrastructure repository `LFRic Core <https://code.metoffice.gov.uk/trac/lfric>`_ and other related repositories. The file `dependencies.sh <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/dependencies.sh>`_ defines included science code version from other repositories like `JULES <https://code.metoffice.gov.uk/trac/jules>`_ or `SOCRATES <https://code.metoffice.gov.uk/trac/socrates>`_.

PSyKAl and PSyclone
-------------------

LFRic uses a domain specific language to separate computational science from natural science in the programming. The software architecture to do this is called `PSyKAl <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html>`_, which stands for `Parallel System <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#psy-layer>`_, `Kernel <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#kernel-layer>`_, and `Algorithm <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#algorithm-layer>`_.

Scientific operations on full field are implemented in the Algorithm layer. Kernels specify operations for vertical columns. Parallelism is implemented in the Parallel System layer which is auto generated with a tool called `PSyclone <https://psyclone.readthedocs.io/en/stable/>`_.

.. figure:: /_static/psykal.png
  :width: 650px

  Separation of Natural and Computational Science in the PSyKAl architecture.

Practical 1: Model Build
------------------------


Practical 2: Code Change
------------------------
