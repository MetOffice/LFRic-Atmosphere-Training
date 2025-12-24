.. _practical_3_2-caption:

Practical 2: Running the LFRic Apps Standard Suite
--------------------------------------------------

Now that you ran the LFRic atmosphere model from the command line, this second practical will introduce how to run it as part of a Cylc workflow. For that we will be using the LFRic Apps Standard Suite. You will learn how to:

* Run the model in a simple workflow
* Locate model outputs and logs
* Make basic configuration changes

**Step 1: Check Out the Standard Suite**

LFRic Apps Standard Suites are available for several computing platforms. Workflow IDs are documented on the `LFRic Apps wiki pages <https://code.metoffice.gov.uk/trac/lfric_apps#WorkingwithLFRicApps>`_. 


Instructions to checkout the Standard Suite depend on your platform. For Met Office Azure Spice, use:
   .. collapse:: Met Office Azure Spice
                 .. code-block:: text
                                 rosie co u-dn674
                                 mv ~/roses/u-dn674 ~/cylc-src/lfric_apps_standard_suite

.. code-block:: bash
   
   rosie co u-dn674
   mv ~/roses/u-dn674 ~/cylc-src/lfric_apps_standard_suite

For other platforms, chose appropriate alternative workflow IDs.

**Step 2: Explore the workflow**

1.	Navigate to the suite directory:

 .. code-block:: bash
   
    cd ~/cylc-src/lfric_apps_standard_suite

2. Open the workflow files in a text editor and explore its structure:

 * Examin the `graph <https://cylc.github.io/cylc-doc/stable/html/glossary.html#term-graph>`_ and the `apps <https://metomi.github.io/rose/doc/html/tutorial/rose/applications.html>`_ it defines. 
 * The standard suite performs the following automatically:

   * Extracts the model code
   * Builds the executable
   * Runs a global model simulation
   * Builds the mesh generator
   * Creates a low-resolution C12 mesh as input for the model


.. figure:: /_static/3/lfric_apps_standard_suite.svg
  :width: 400px

  Graph of the LFRic Apps Standard Suite, a toy model for testing, learning, and developing - visualised with cylc graph.


**Step 3: Run the workflow**

Start the workflow with:

.. code-block:: bash
   
   cd ~/cylc-src/lfric_apps_standard_suite
   cylc vip

While the workflow is running, open the `Cylc UI <https://cylc.github.io/cylc-doc/latest/html/user-guide/running-workflows/tasks-jobs-ui.html>`_ (with the command ``cylc gui``) while it is running and explore the model output in ``~/cylc-run/lfric_apps_standard_suite/``. 

**Step 4: View logs and outputs**

View your logs in your site's central `Cylc Review <https://cylchub/services/cylc-review/>`_ pages or, if you do not have one, launch your own Cylc Review instance with ``cylc review start`` and 
navigate to the page in your browser. The logs are also stored under ``~/cylc-run/lfric_apps_standard_suite/run?//log//job/1/``. 
From the logs Find out how many time steps were executed and locate the output files in NetCDF format.

**Step 5: Modify the configuration**

To gain more experience with the LFRic Apps Standard Suite, make the following configuration changes:

1) Reduce the number of iterated time steps in the workflow by 50%. 
2) Reduce the length of the time step by 50%.

Then, re-run the workflow for each change (or combine them) and compare:

* The number of produced NetCDF files 
* The forecast duration

.. hint:: In the workflow directory ``~/cylc-src/lfric_apps_standard_suite`` navigate to ``app/lfric_atm`` and edit the configuration ``rose-app.conf`` with ``rose edit`` (or a text editor). You need to modify the variables ``timestep_end`` and ``dt``. The NetCDF files can be found under the path ``~/cylc-run/lfric_apps_standard_suite/run?/work/1/lfric_atm/*nc``.
