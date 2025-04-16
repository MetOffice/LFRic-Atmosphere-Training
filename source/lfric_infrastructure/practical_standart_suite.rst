
Practical 2: Standard Suite
---------------------------

This practical introduces the LFRic Apps Standard Suite to learn how to run the model in a simple workflow, find the output, read the logs, and make a simple configuration change.

LFRic Apps Standard Suites are available for several computers. Workflow IDs are documented on the `LFRic Apps wiki pages <https://code.metoffice.gov.uk/trac/lfric_apps#WorkingwithLFRicApps>`_. Assuming you want to run the exercise on the Met Office Azure Spice platform, you can checkout the standard suite with:

.. code-block:: bash
   
   rosie co u-dn674
   mv ~/roses/u-dn674 ~/cylc-src/lfric_apps_standard_suite

For other platforms, chose appropriate alternative workflow IDs.

Change to ``~/cylc-src/lfric_apps_standard_suite`` and explore the workflow in a text editor. Look at its `graph <https://cylc.github.io/cylc-doc/stable/html/glossary.html#term-graph>`_ and the `apps <https://metomi.github.io/rose/doc/html/tutorial/rose/applications.html>`_. The standard suite extracts the model code, builds the executable, and runs a global model. It also builds the mesh generator and creates a low resolution C12 mesh as an input for the model.


.. figure:: /_static/3/lfric_apps_standard_suite.svg
  :width: 400px

  Graph of the LFRic Apps Standard Suite, a toy model for testing, learning, and developing.

Start the workflow with:

.. code-block:: bash
   
   cd ~/cylc-src/lfric_apps_standard_suite
   cylc vip

Look at the workflow in the `Cylc UI <https://cylc.github.io/cylc-doc/latest/html/user-guide/running-workflows/tasks-jobs-ui.html>`_ (started with the command ``cylc gui``) while it is running and explore the model output in ``~/cylc-run/lfric_apps_standard_suite/``. View your logs in your site's central `Cylc Review <https://cylchub/services/cylc-review/>`_ pages or, if you do not have one, launch your own Cylc Review instance with ``cylc review start`` and navigate to the page in your browser. The logs are also stored under ``~/cylc-run/lfric_apps_standard_suite/run?//log//job/1/``. Find out from the logs how many time steps have been executed and locate the output files in NetCDF format.

**Configuration changes**

To gain more experience with the LFRic Apps Standard Suite, perform the following configuration changes:

1) Reduce the number of iterated time steps in the workflow by 50%. 
2) Reduce the length of the time step by 50%.

Re-run the workflow for both experiments individually (or on top of each other) and compare the number of produced NetCDF files. Did the forecast length change as expected?

.. hint:: In the workflow directory ``~/cylc-src/lfric_apps_standard_suite`` navigate to ``app/lfric_atm`` and edit the configuration ``rose-app.conf`` with ``rose edit`` (or a text editor). You need to modify the variables ``timestep_end`` and ``dt``. The NetCDF files can be found under the path ``~/cylc-run/lfric_apps_standard_suite/run?/work/1/lfric_atm/*nc``.
