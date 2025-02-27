.. Momentum-LFRic documentation master file, created by
   sphinx-quickstart on Wed Apr 10 13:40:47 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Momentum Training - LFRic Atmosphere
====================================

**Momentum**:sup:`®` is a software framework for modelling Earth’s environment, developed and used by the `Momentum Partnership <https://www.metoffice.gov.uk/research/approach/collaboration/momentum-partnership>`_. The framework includes rigorously evaluated Science Configurations, which define how to configure components of the framework to build prediction and projection systems, both regional and global.

.. image:: /_static/momentum_logo.png
   :width: 700px

`Momentum <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ follows a seamless modelling approach, using the same model components across temporal and spatial scales, similar to the `Unified Model <https://www.metoffice.gov.uk/research/approach/modelling-systems/unified-model>`_. The framework includes model components for the atmosphere, land surface, ocean, sea-ice, and other parts of the Earth system. It contains software for data assimilation, verification, and technical tasks like workflow management.

**LFRic Atmosphere** is the atmospheric model component of Momentum. It is the successor to the Unified Model. This course is designed for new users of LFRic Atmosphere. See the `Momentum website <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ for information about the other components of the modelling framework.

.. note:: 
   **Target users and prior knowledge**: This course is designed for new users of LFRic who have a general background in climate science. It is assumed you will have experience in working in linux terminal and have basic understanding of python and other coding languages. Throughout the course there will be notes on where to refresh skills needed for each section.

   Before diving into this course, it’s helpful to have some foundational knowledge in the following areas:

   - Workflow engine `Cylk <https://cylc.github.io/cylc-doc/stable/html/tutorial/index.html>`_:  A system that automatically executes tasks according to schedules and dependencies.
   - Configuration management system `Rose <https://metomi.github.io/rose/doc/html/tutorial/rose/index.html>`_: A toolkit for writing, editing, and running application configurations.
   - Version control with `FCM <https://metomi.github.io/fcm/doc/user_guide/>`_ and `Git <https://www.astropython.com/git-novice/>`_: Tools for tracking and managing changes in code.
---------

Contents of the training course
-------------------------------

.. toctree::
   :maxdepth: 1

   intro/index
   mesh/index
   lfric_code/index
   global/index
   regional/index


