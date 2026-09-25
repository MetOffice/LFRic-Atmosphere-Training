.. Momentum-LFRic documentation master file, created by
   sphinx-quickstart on Wed Apr 10 13:40:47 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Momentum Training - LFRic Atmosphere
====================================

**Momentum**:sup:`®` is a software framework for modelling Earth's environment,
developed and used by the Momentum Partnership. The framework includes
rigorously evaluated Science Configurations, which define how to configure
components of the framework to build prediction and projection systems, both
regional and global.

.. image:: /_static/momentum_logo.png
   :alt: Momentum: The Unified Earth Environment Prediction Framework
   :align: center
   :width: 400px

Momentum follows a seamless modelling approach, using the same model components
across temporal and spatial scales, similar to the Unified Model. The framework
includes model components for the atmosphere, land surface, ocean, sea-ice, and
other parts of the Earth system. It contains software for data assimilation,
verification, and technical tasks like workflow management.

**LFRic Atmosphere** is the atmospheric model component of Momentum. It is the successor to the Unified Model. See the `Momentum website <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ for information about the other components of the modelling framework.

Who this course is for
----------------------

This course is designed for new users of LFRic Atmosphere who have a general
background in weather or climate science. You should be comfortable working in
a Linux terminal and have some experience of Python.

The course also uses Cylc, Rose, version control (FCM and Git) and Jupyter
notebooks. You do not need to know these in advance. Where a section relies on
one of them, we explain what you need and suggest where to find out more.
Links to introductory material are listed under :ref:`further-reading` at
the end of this page.

.. tip::

   For help, questions, or feedback on the training, please use
   `GitHub Discussions
   <https://github.com/MetOffice/LFRic-Atmosphere-Training/discussions>`_.
   You are welcome to start a discussion without opening an issue or
   preparing a pull request.

.. _platform-tabs:

--------------------------
Choosing your platform
--------------------------

Many of the practical pages give instructions that depend on the computer you
are working on. Those instructions are presented in tabs. Pick the tab that
matches your platform once, and the rest of the site follows your choice.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Tab
     - Use it when
   * - **Met Office**
     - You are working on a Met Office system, using the managed LFRic
       environment and the Met Office module stack.
   * - **Monsoon**
     - You are working on Monsoon3, the collaborative HPC service shared with
       Momentum partners. Monsoon3 splits access, interactive workflow
       management, and HPC work across separate services, so some commands
       must be run from a particular service. See :ref:`monsoon3-where-to-run-commands`.
   * - **Other**
     - You are working on your own machine, or on a system run by another
       institution. You provide the environment yourself.

.. important::

   Support for the **Other** route is limited. It is enough for the
   visualisation and analysis material, where you only need Python, Iris, and
   the training repository. It is **not** enough for the exercises that build
   and run the model: those need a supported LFRic build environment, Met
   Office repository access, shared ancillary data, and HPC batch queues. Where
   an exercise cannot be completed on your own machine, the **Other** tab says
   so.

-------------------------------
Contents of the training course
-------------------------------

.. toctree::
   :maxdepth: 2

   introduction/index.rst
   mesh_overview/index.rst
   lfric_infrastructure/index.rst
   modelling/index.rst
   glossary
   appendices/index.rst
   references.rst

.. _further-reading:

---------------
Further reading
---------------

.. seealso::

   Introductory material for tools used in the course:

   - :external+cylc:doc:`Cylc Tutorial <tutorial/index>`
     Cylc is a workflow engine that runs tasks according to schedules and
     dependencies.
   - :external+rose:doc:`Rose Tutorial <tutorial/rose/index>`
     Rose is a toolkit for writing, editing, and running application
     configurations.
   - `FCM user guide <https://metomi.github.io/fcm/doc/user_guide/>`_ and
     `Git novice lesson <https://metoffice.github.io/git-novice/>`_: tools for
     tracking and managing changes in code.
   - :ref:`using-jupyter-notebooks`: how to launch JupyterLab, choose the
     correct kernel, run notebook cells, and find beginner-friendly Python
     resources.

   Background on Momentum:

   - `Momentum Partnership <https://www.metoffice.gov.uk/research/approach/collaboration/momentum-partnership>`_
   - `Unified Model <https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model>`_
