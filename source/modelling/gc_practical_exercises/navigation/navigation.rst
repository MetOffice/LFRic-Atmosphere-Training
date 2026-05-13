******************************
Navigating a GC-LFRic workflow
******************************

In this practical you will explore the Met Office Science Repository Service, checkout a workflow and explore the  workflow.

Exercise 1: Find the appropriate workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting on the Met Office Science Repository Service homepage, navigate to the correct page to find the workflow  for the practical. Spend time looking at the pages.

Look for the workflow which fulfils these criteria **C64 coupled climate standard experiment @ LFRic r44221**

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
   - [ ] University of Exeter
   - [ ] IBM

   ## Which templating languages are available to add logic and automation to suite.rc files?

   - [x] jinja2
   - [ ] C++
   - [x] EmPy
   - [ ] JavaScript

  ## What tool would you used to change from structured to unstructured data?

   - [x] esmf_regrid
   - [ ] iris.unstructured
   - [ ] cdo tools
   - [ ] geovista
