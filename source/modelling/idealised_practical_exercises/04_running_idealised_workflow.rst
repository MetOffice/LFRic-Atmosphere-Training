*****************************
Running an Idealised Workflow
*****************************

Once your suite has been set up, you can run it using Cylc:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         cylc vip

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         cylc vip

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. include:: /include/isambard3-help.rst

      .. code-block:: bash

         bash "$SCRATCHDIR/lfric-env-isambard/examples/science-suites/run-suite.sh" \
               u-dz791

      This adapts your checkout in ``~/roses/u-dz791`` to Isambard 3 the
      first time, then runs ``cylc vip`` on it. Run it on a login node; Cylc
      submits the tasks to Slurm. The build takes about ten minutes once its
      job starts, then each of the two 30-minute cycles takes about two
      minutes.

      To run an experiment after changing the configuration, run the same
      command again. It keeps your changes and starts a new run,
      ``u-dz791/runN``, which builds the model again.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: bash

         cylc vip

``cylc vip`` is short for ``cylc validate-install-play``, and performs three
actions:

- **Validate**: Checks the suite configuration for errors
- **Install**: Sets up the runtime environment
- **Play**: Starts executing the workflow

.. note::

   Unlike the global and regional suites, the idealised suite selects its
   platform from the ``EX_HOST`` template variable you set in the Rose GUI, so
   no ``--opt-conf-key`` is needed here.

Monitor the workflow
--------------------

Once the suite is running, you can monitor its progress using either of the
following commands:

.. include:: /include/cylc-gui.rst

These tools allow you to view task status, progress, and any failures.

For more details on Cylc commands, see :doc:`Running a Cylc Workflow
<../gc_practical_exercises/03_running_global_workflow>` under *Exercises in
Global Configurations*.

After the workflow has completed successfully, navigate to the output directory
and try plotting the data.

.. note:: Isambard 3

   The model output is in the work directory of each cycle, one file every
   10 minutes of model time:
   ``~/cylc-run/u-dz791/runN/work/<cycle>/lfric_atm/lfric_crm_diag_*.nc``.

