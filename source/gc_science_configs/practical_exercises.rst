Practical Exercises
===================

Practical 1 - Navigating a GC-LFRic workflow
--------------------------------------------

In this practical you will explore the Met Office Science Repository Service, checkout a workflow and explore the  workflow.

Exercise 1: Find the appropriate workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting on the Met Office Science Repository Service homepage, navigate to the correct page to find the workflow  for the practical. Spend time looking at the pages.

Look for the workflow which fulfills these criteria **C64 coupled climate standard experiment @ LFRic r44221**

  * What is the missing physics from r44221 @ #638.1.1
  * Is there an atmosphere only equivalent?
  * Explore the #638 ticket recording the science developments

.. note:: Workflows are documented on the GMED wiki. The GC5-LFRic workflows are currently under development, and  so its science is changing and incomplete.

Exercise 2: Explore tasks in a GC-LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Checkout the global coupled workflow - ``rosie checkout <suite-id>``

Move to directory containing the workflow and explore the files inside- ``cd ~/roses/<suite-id>``

Start workflow in hold mode to explore cylc gui - ``rose suite-run -- --hold``

Q - How do you change views from 1 to 2 to 3?

Q - Which task is where the forecast runs?


Inputs and outputs for GC-LFRic workflows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Editing a GC-LFRic workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^


Tracking the progress of your workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. quizdown::

    ---
    primary_color: orange
    secondary_color: lightgray
    text_color: black
    shuffle_questions: false
    ---

   ## What command would you use to ensure your running workflow picks up new changes?

   - [ ] rose suite-run -- --hold
   - [x] rose suite-run -- --reload
   - [ ] rose -- --update
   - [ ] You can't update a workflow which is running. You need to restart it for it to pick up the new changes.

   ## In what file is the lfric source code specified??

   - [x] fcm_make_lfric/rose-app.conf
   - [ ] fcm_make_um/rose-app.conf
   - [ ] suite.rc
   - [ ] rose-suite.conf

    ## Where was cylc originally developed?

   - [ ] Met Office
   - [x] NIWA
   - [ ] University of Cambridge
   - [ ] IBM

   ## What is the equivalent UM resolution of C64 and its real world value?

   - [ ] n96 and 200km
   - [ ] n216 and 60km
   - [ ] n48 and 115km
   - [x] n96 and 135km

   ## Which templating languages are available to add logics and automation to suite.rc files?

   - [x] jinja2
   - [ ] C++
   - [x] EmPy
   - [ ] JavaScript

  ## What tool would you used to change from structured to unstructured data?

   - [x] esmf_regrid
   - [ ] iris.unstructured
   - [ ] cdo tools
   - [ ] geovista


Practical 2 - Running a GC-LFRic Workflow
-----------------------------------------

Aims and objectives
^^^^^^^^^^^^^^^^^^^

The aim of this practical is to gain experience in running and analysing climate models.<200b> You will:

* Copy the GC5-LFRic workflow <200b>
* Add extra diagnostics to the ocean, atmosphere and sea-ice <200b>
* Run the climate workflow for 1 month on an HPC <200b>
* Set up a range of other climate models where various parameters are changed to generate interesting results.     <200b>
* Visualise these results using Python/Iris.


.. admonition:: Thought experiment: How would you design your experiment?

   As scientists we want to explore how climate models perform and respond to changes. How sensitive are they to   CO2 or what impact does an eddy parametrisation have on ocean circulation. **Think** about what parameters you    would want to test within a global model? Once you have an idea, think about the next questions. <200b>

   * Where you might change this - is it in the **configuration namelist** settings within the workflow or in a ** source code**?<200b>

   * Browse the source code and workflow to look see how you might make this change. <200b>

   * What **diagnostic** would you plot to see the change?<200b>

.. Caution:: If you decide to test your own experiment with a code or configuration change, be ready to do lots of debugging! If you want an example which is tried and tested, use the given examples below.

Main Practical
^^^^^^^^^^^^^^
* Run a simulation a with different experimental setup<200b>

* Either use an existing experiment or your previous hypothesis<200b>

* Create a branch for each new experiment (to limit the new workflow IDs created)<200b>

* Plot the data and look for evidence of changes

.. note:: Feel free to enlarge the size of these changes (e.g. 20x CO2) if your analysis is not detecting much of  an impact. Copy the output files (files explained at the end of the last section) to your local Linux workstation  and analyse the files using <200b>Python/<200b>Iris. Try to plot differences between the experiments and the       control in the fields that you think will be most strongly affected. If possible make a prediction at what these   differences might show before you do the plots. Were your predictions right?


Adding a new diagnostic
^^^^^^^^^^^^^^^^^^^^^^^

The atmospheric diagnostic “v component of wind on pressure levels" is missing from this model. Use the following  instructions to add it back to the configuration.

* cd into ``app/lfric_atm/file``
* open ``file_def_diags_user_temp.xml<200b>``
* find ``lfric_pressure_level_tdaym``
* add in a new field for ``v_in_w3``

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
   :emphasize-lines: 3

   <field field_ref="processed__pressure_in_w3"/>
   <field field_ref="u_in_w3"/>
   <field field_ref="v_in_w3"/>
   <field field_ref="w_in_w3"/>
   </field_group>

Experiment 1 - CO2 x 10
^^^^^^^^^^^^^^^^^^^^^^^
* cd into ``app/lfric_atm``
* open the ``rose-app.conf``
* search for ``co2_mix_ratio``
* change this value from 5.60353e-04 to 5.60353e-03

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/rose-app.conf
   :emphasize-lines: 6

   [namelist:well_mixed_gases]
    cfc113_mix_ratio=0.0
    cfc11_mix_ratio=0.0
    cfc12_mix_ratio=4.3919e-09
    ch4_mix_ratio=9.8200e-07
    co2_mix_ratio=5.6062e-03
    hcfc22_mix_ratio=0.0
    hfc134a_mix_ratio=3.6811e-10
    n2_mix_ratio=0.7553
    n2o_mix_ratio=4.7957e-07
    o2_mix_ratio=0.2314
    so2_mix_ratio=0.0


Experiment 2 - Reduce the rotation of the earth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* cd ``app/lfric_atm``
* open ``rose-app-conf``
* change ``omega``

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/rose-app.conf
   :emphasize-lines: 4

   [namelist:planet]
    cp=1005.0
    gravity=9.80665
    omega=7.292116E-5
    p_zero=100000.0
    radius=6371229.0
    rd=287.05
    scaling_factor=1.0

Experiment 3 - coupling remove influence of evaporation from ocean
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
* cd ``app/coupled/file``
* open ``namcouple``
* Observe namcouple file - what is it setting?
* adjust definition of coupling for ``lf_evap``

.. code-block:: text
   :caption: trunk/app/coupled/file/namcouple
   :emphasize-lines: 1, 8

   lf_evap OTotEvap 466 3600 2 atmos_restart.nc   EXPORTED
    24576 1 1442 1207 lfric tor1 SEQ=+2
    P  0  P  2
    #
    MAPPING
    ##
    rmp_lfric_to_tor1_nomask_CONSERVE_DSTAREA.nc
    0.0 0
    #

.. note:: Note on the namcouple file......

Experiment 4 - make sea ice black
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* create JULES branch - See: Working Practices: Create a ticket, Working Practices: Create a branch

* adjust hard coded values for the albedo in ``src/control/shared/jules_sea_seaice_mod.F90``
  (set ``calbicev_cice``, ``albicei_cice``, ``albsnowv_cice``, ``albsnowi_cice``, ``albpondv_cice``,               ``albpondi_cice``, ``dalb_mlt_cice``, ``dalb_mlts_v_cice`` and ``dalb_mlts_i_cice`` to 0.0)

* point your LFRic build setup in ``paramerts.sh`` to you JULES branch and adjust your workflow to use your        adjusted model build

* build the model and run your experiment

.. code-block:: fortran
   :caption: src/control/shared/jules_sea_seaice_mod.F90
   :emphasize-lines: 2, 4, 6, 8, 10, 12

   ! Parameters for 4-band CICE albedo scheme used within JULES:
        albicev_cice = 0.00,                                                       &
          ! Sea ice albedo (visible)
        albicei_cice = 0.00,                                                       &
          ! Sea ice albedo (near-infrared)
        albsnowv_cice = 0.00,                                                      &
          ! Snow albedo (visible)
        albsnowi_cice = 0.00,                                                      &
          ! Snow albedo (near-infrared)
        albpondv_cice = 0.00,                                                      &
          ! Meltpond albedo (visible)
        albpondi_cice = 0.00,                                                      &
          ! Meltpond albedo (near-infrared)
        ahmax = 0.3,                                                               &
          ! Sea ice albedo in CICE multi-band scheme is constant above this
          ! thickness (metres)
        dalb_mlt_cice = -0.075,                                                    &

Plotting your data
^^^^^^^^^^^^^^^^^^

* Script:/home/h02/lroberts/ngux/lfric_exercise/iris_ngux_module3.py

* Select data for your control and experimental setups

* Choose the diagnostic to plot

* Run the script


.. image:: /_static/plotting.png
   :width: 650px
