Tools for running GC model configurations
=========================================

NWP and climate models have a large numbers of jobs which are executed at regular intervals to process new data and generate new forecasts. Dependence between these forecast cycles creates a single never-ending workflow, which NWP workflow schedulers have traditionally ignored. Met Office science configurations are built on **Rose** and **Cylc (“Silk”)** to manage infinite cycling workflows efficiently even after delays in real-time operation, or in historical runs, when cycles can typically interleave for much-increased throughput.

Rose - managing model configurations
------------------------------------

.. image:: /_static/rose.png
   :align: right
   :width: 200px

* Rose is a tool for writing, editing, updating, and running configurations of applications
* Rose allows top-level configuration of applications for workflows used for LFRic and UM model experiments
* Developed by the Met Office, but not LFRic specific (i.e. used for NEMO as well)

**Rose configurations** are directories containing a Rose configuration file along with other optional assets which define behaviours such as execution, file installation, and environment variables.

Rose configurations may be used standalone or in combination with the Cylc workflow engine.

**Why Use Rose Configurations?**

With Rose configurations, the inputs and environment required for a particular purpose can be encapsulated in a simple human-readable configuration. Configuration settings can have metadata associated with them which may be    used for multiple purposes including automatic checking and transforming. Rose configurations can be edited either using a text editor or with the rose config-edit GUI which makes use of metadata for display and on-the-fly validation purposes.


.. note:: More information and training material: https://metomi.github.io/rose/doc/html/tutorial/rose/metadata.html

Cylc - workflow engine
----------------------

* Cylc is a general-purpose workflow engine used to automate running groups of tasks in a specified order on computers.
* Cylc workflows can be organized running tasks at specific clock cycles.
* Cylc workflows represent the highest-level programming layer for organising the execution of our models, pre- and postprocessors.

.. image:: /_static/cylc.gif
   :width: 700px

.. note::
   * Comprehensive guides and training for cylc can be found here: https://cylc.github.io/cylc-doc.
   * The cylc GitHub discourse can be used for discussions: https://cylc.discourse.group.

.. quizdown::

    ---
    primary_color: orange
    secondary_color: lightgray
    text_color: black
    shuffle_questions: false
    ---

   ## Drag and drop the directory structure of a GC workflow to locate the namcouple file.

    > namcouple is last.

    1. roses/
    2. suite-ID/
    3. app/
    4. coupled/
    5. file/
    6. namcouple

   ## What is the correct definition for a cylc workflow?

   - [ ] a system for managing repetitive processes and tasks which occur in a particular order
   - [x] a general-purpose workflow engine that also orchestrates cycling systems very efficiently
   - [ ] a system for delivering climate data to customers

   ## In what file would you find the owner of the workflow you are using?

   - [ ] rose-suite.conf
   - [x] rose-suite.info
   - [ ] rose-info.conf
   - [ ] READ.ME


.. note:: On Version Control -
