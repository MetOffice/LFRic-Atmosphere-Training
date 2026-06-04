************************************
Editing a Regional Nesting Suite
************************************

Once you have copied the regional nesting suite (e.g. ``u-by395``), the next step is to navigate to the suite directory and open it using the Rose graphical user interface (GUI).

Step 1: Navigate to the suite directory
---------------------------------------

Open a terminal and move to the directory where your suite is located:

.. code-block:: bash

   cd ~/roses/<suite-id>

Step 2: Open the suite in the Rose GUI
--------------------------------------

Launch the Rose editor by running:

.. code-block:: bash

   rose edit &

- This command opens the suite in the Rose graphical user interface, allowing you to view and modify its configuration.
- The ``&`` at the end runs the GUI in the background, so your terminal remains available for other commands.

Step 3: Setting Up the Regional Nesting Suite
=============================================

Once the GUI is open, you can begin configuring the suite for your specific experiment or run by navigating through the tabs on the left side of the window .

General Run Options
~~~~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the ``General run options`` tab to define the key settings required to run your nesting suite.

.. _fig-general-run-options1:

.. figure:: /_static/1/general_run_options1.png
   :width: 650px
   :alt: General run options panel in the Rose configuration editor.


Site and Machine Selection
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **SITE**  
  Select the machine where the nesting suite will run (e.g. *Met Office EX "moex-cray"*).

- **EX HOST**  
  Choose the execution host group (e.g. *MONSOON3*, *EXA/EXB*, or *EXC/EXD* depending on availability).

Project Configuration
^^^^^^^^^^^^^^^^^^^^^^^

 **PROJECT_NAME**  
  Specify the project code used for accounting or charging the run (e.g. ``training``).

Model Run Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- **RUN_LFRIC_LAM_IN_DEV_MODE**  
  Enables additional graphing and debugging tasks for the LFRic LAM.  
  - ``true``: Run LFRic with development diagnostics  
  - ``false``: Skip LFRic development features

- **RUN_UM_LAM**  
  Determines whether the UM LAM is run alongside the LFRic LAM.  
  - ``true``: Run both UM and LFRic (useful for comparison)  
  - ``false``: Run only LFRic LAM

Post-processing Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

LFRic data is produced on an unstructured grid. If required, it can be post-processed onto a structured grid for analysis.

.. _fig-general-run-options2:

.. figure:: images/general_run_options2.png
   :width: 800px
   :align: center
   :alt: Post-processing configuration options.

- **RUN_LFRIC_POSTPROCESS**  
  Enables post-processing of LFRic output.  
  - ``true``: Convert output to a structured grid  
  - ``false``: Keep native unstructured output

.. admonition:: 💡 Tips
   :class: tip

   - Hover over the **hand icon** in the GUI or click the **settings icon** next to each option to view additional help.
   - Start with default values for training exercises before experimenting with custom configurations.
   - Running both UM and LFRic LAMs is recommended for validation and comparison during learning.

Cycling Options
~~~~~~~~~~~~~~~~~~~~~~~~~~
In this section, you will configure the  ``cycling options `` for your model experiment
using the rose GUI. These settings control how the model progresses from one cycle
to the next and define the start and end times for your run.

The interface shown below highlights the key options available.

.. figure:: cycling_options.png
   :alt: Cycling options configuration panel in the rose GUI
   :align: center
   :width: 85%

   Cycling options panel in the rose configuration GUI.

For this self-learning exercise, you can use the following configuration:

- Set **CASE_STUDIES** to ``false``
- Define a short experiment window using:
  
  - ``INITIAL_CYCLE_POINT`` = ``20250508T0000Z``
  - ``FINAL_CYCLE_POINT`` = ``20250509T0000Z``

- Keep **CYCLE_INT_HR** = ``24``
- Leave **FREE_RUN** = ``false``
- Leave **USE_OSTIA** = ``false``

This setup provides a simple, manageable configuration for training purposes.

Driving Model Set-up
~~~~~~~~~~~~~~~~~~~~~~~~~~
To run the Limited Area Model, you will have to use a driving model to obtain the initial data from. This can be set up in the driving model window. You can start the regional model from several options such as UM global model, ECMWF forecast fields, archived analysis files, etc. These options acan be chosen from the driving model window. You can also choose the resolution of the driving model, number of processors needed, etc, from this sections.

Nested Region 1 Set-UP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nested region set up help you to name the domain you are planning to run the limited area model for. You can slo choose the number of experiments you are planning with the model here (eg., if you are planning to run the limited area model at two different reolutions such as 4.4 and 1.5kms, then choose resolution as '2' here) 

Then move on to the ``Resolution 1`` set-up to set the horizontal and vertical resolutions of the inner limited area domain. You will also have to give the path to the ancillaries (in the machine where you are running the model) which will be used to run the limited area model. 

..note::
   The ancillaries can be generated using the regional ancillary suite or if the ancillaries for your specific domain and resolution are already available, you can then copy those ancillaries to the machine of your choice. Please get in touch with Momentum_Partnerships@metoffice.gov.uk or all enquiries regarding the ancillaries. 


..tip::
   When choosing a name for your nested region, resolution and configuration, you are free to enter anything you like as long as it does not contain spaces or periods. The idea is to choose names that are meaningful to you so that when you look back at your suite output directory in the future, you can remember what you did! For example, if you were setting up a 4.4 km resolution model over Exeter, with 70 vertical levels and using the RAL3 science configuration, appropriate names for the region, resolution and configuration would be something like “EXE”, “4p4_L70” and “ukv”, respectively. 

Editing a Regional LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Tracking the progress of your workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

