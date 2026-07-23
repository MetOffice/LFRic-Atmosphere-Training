.. Momentum-LFRic documentation master file, created by
   sphinx-quickstart on Wed Apr 10 13:40:47 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Momentum Training - LFRic Atmosphere
====================================

**Momentum**:sup:`®` is a software framework for modelling Earth's environment, developed and used by the `Momentum Partnership <https://www.metoffice.gov.uk/research/approach/collaboration/momentum-partnership>`_. The framework includes rigorously evaluated Science Configurations, which define how to configure components of the framework to build prediction and projection systems, both regional and global.

.. image:: /_static/momentum_logo.png
   :align: center
   :width: 400px

`Momentum <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ follows a seamless modelling approach, using the same model components across temporal and spatial scales, similar to the `Unified Model <https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model>`_. The framework includes model components for the atmosphere, land surface, ocean, sea-ice, and other parts of the Earth system. It contains software for data assimilation, verification, and technical tasks like workflow management.

**LFRic Atmosphere** is the atmospheric model component of Momentum. It is the successor to the Unified Model. This course is designed for new users of LFRic Atmosphere. See the `Momentum website <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ for information about the other components of the modelling framework.

.. note::
   **Target users and prior knowledge**: This course is designed for new users of LFRic who have a general background in climate science. It is assumed you will have experience in working in Linux terminal and have basic understanding of python and other coding languages. Throughout the course there will be notes on where to refresh skills needed for each section.

   Before diving into this course, it's helpful to have some foundational knowledge in the following areas:

   - Workflow engine `Cylc <https://cylc.github.io/cylc-doc/stable/html/tutorial/index.html>`_:  A system that automatically executes tasks according to schedules and dependencies.
   - Configuration management system `Rose <https://metomi.github.io/rose/doc/html/tutorial/rose/index.html>`_: A toolkit for writing, editing, and running application configurations.
   - Version control with `FCM <https://metomi.github.io/fcm/doc/user_guide/>`_ and `Git <https://www.astropython.com/git-novice/>`_: Tools for tracking and managing changes in code.
   - Python and Jupyter notebooks: The :ref:`using-jupyter-notebooks` page explains how to launch JupyterLab, choose the correct kernel, run notebook cells, and find beginner-friendly Python resources.

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
