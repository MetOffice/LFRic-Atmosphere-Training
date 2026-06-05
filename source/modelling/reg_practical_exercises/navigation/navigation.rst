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

.. figure:: /_static/general_run_options1.png
   :width: 650px
   :alt: Screenshot of the 'General run options' panel in the Rose configuration editor.


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

This section allows you to define the **nested domain** for your limited area model (LAM).
You will specify both the **region name** and the **number of resolutions (experiments)** you want to run  (eg., if you are planning to run the limited area model at two different reolutions such as 4.4 and 1.5kms, then choose resolution as '2' here) 

*See figure below: Nested region 1 setup*

.. image:: _static/1/nested_region1_setup.png
   :alt: Nested region 1 setup interface
   :align: center
   :width: 80%

Once this is set, move to **Resolution 1 setup** to configure each experiment.


Resolution 1 Set-Up
~~~~~~~~~~~~~~~~~~

This section defines the **horizontal and vertical resolution** and links the required **ancillary data**.

*See figure below: Resolution 1 setup*

.. image:: _static/1/resolution1_setup.png
   :alt: Resolution 1 setup interface
   :align: center
   :width: 80%

.. note:: Ancillary data

   The ancillaries can be generated using the regional ancillary suite.  
   If the ancillaries for your specific domain and resolution are already available,  
   you can copy those ancillaries to the machine of your choice.

   Please get in touch with ``Momentum_Partnerships@metoffice.gov.uk``  
   for all enquiries regarding the ancillaries.


Config 1 Set-Up (Science Configuration)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This section allows you to configure the **science options** and **model behaviour** 
for your limited area model experiment.

*See figure below: Config 1 setup*

.. image:: config1_setup.png
   :alt: Config 1 setup interface
   :align: center
   :width: 80%

🔍 In this panel, you will define the key scientific settings for your model run.


.. tip:: 💡 Naming Your Region, Resolution & Configuration

   When choosing a name for your nested region, resolution, and configuration,  
   you are free to enter anything you like as long as it does not contain spaces or periods.

   The idea is to choose names that are meaningful to you so that when you look 
   back at your suite output directory in the future, you can remember what you did!

   **Example:**

   - Region: ``UK``
   - Resolution: ``4p4_L70``
   - Configuration: ``RAL3P2``

   This corresponds to a 4.4 km resolution model over the UK with 70 vertical levels 
   using the RAL3.2 science configuration.

Once the limited area model is all set up, you can go ahead and run the model. 

.. Note:: You can also edit the suite by editing the corrsponding .conf file in the suite directory, if you do not wish to use the Rose grahical user interface. 


Tracking the progress of your workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

