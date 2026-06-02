************************************
Editing a Regional Nesting Suite
************************************

Once you have copied the regional nesting suite (e.g. ``u-by395``), the next step is to navigate to the suite directory and open it using the Rose graphical user interface (GUI).

Step 1: Navigate to the suite directory
---------------------------------------

pen a terminal and move to the directory where your suite is located:

.. code-block:: bash

   cd ~/roses/u-by395

Step 2: Open the suite in the Rose GUI
--------------------------------------

Launch the Rose editor by running:

.. code-block:: bash

   rose edit &

- This command opens the suite in a graphical interface, allowing you to view and modify its configuration.
- The ``&`` at the end runs the GUI in the background, so your terminal remains available for other commands.

Step 3: Setting Up the Regional Nesting Suite
=============================================

Once the GUI is open, you can begin configuring the suite for your specific experiment or run.

General Run Options
-------------------

Navigate to the **General run options** tab to define the key settings required to run your nesting suite.

.. figure:: images/general_run_options1.png
   :width: 800px
   :align: center

   General run options panel in the Rose configuration editor.

Site and Machine Selection
~~~~~~~~~~~~~~~~~~~~~~~~~~

- **SITE**  
  Select the machine where the nesting suite will run (e.g. *Met Office EX "moex-cray"*).

- **EX HOST**  
  Choose the execution host group (e.g. *MONSOON3*, *EXA/EXB*, or *EXC/EXD* depending on availability).

Project Configuration
~~~~~~~~~~~~~~~~~~~~~

- **PROJECT_NAME**  
  Specify the project code used for accounting or charging the run (e.g. ``training``).

Model Run Options
~~~~~~~~~~~~~~~~~

- **RUN_LFRIC_LAM_IN_DEV_MODE**  
  Enables additional graphing and debugging tasks for the LFRic LAM.  
  - ``true``: Run LFRic with development diagnostics  
  - ``false``: Skip LFRic development features

- **RUN_UM_LAM**  
  Determines whether the UM LAM is run alongside the LFRic LAM.  
  - ``true``: Run both UM and LFRic (useful for comparison)  
  - ``false``: Run only LFRic LAM

Post-processing Options
~~~~~~~~~~~~~~~~~~~~~~

LFRic data is produced on an unstructured grid. If required, it can be post-processed onto a structured grid for analysis.

.. figure:: images/general_run_options2.png
   :width: 800px
   :align: center

   Post-processing configuration options.

- **RUN_LFRIC_POSTPROCESS**  
  Enables post-processing of LFRic output.  
  - ``true``: Convert output to a structured grid  
  - ``false``: Keep native unstructured output

- **POSTPROCESS_UMIFY**  
  Produces UMD-style output alongside SLAM/LFRic-only data when enabled.

- **POSTPROCESS_ARCHIVE**  
  Archives the processed LFRic output to MASS storage.

- **POSTPROCESS_MEMORY**  
  Specifies the memory allocated for post-processing tasks (e.g. ``40``).

- **POSTPROCESS_NPROCS**  
  Defines the number of processors used for post-processing (e.g. ``1``).

Tips
~~~~

- Hover over the **hand icon** in the GUI or click the **settings icon** next to each option to view additional help.
- Start with default values for training exercises before experimenting with custom configurations.
- Running both UM and LFRic LAMs is recommended for validation and comparison during learning.


Exercise 2: Explore tasks in a Regional LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inputs and outputs for a Regional LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Editing a Regional LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tracking the progress of your workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

