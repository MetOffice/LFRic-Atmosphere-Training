*****************************
Running an Idealised Workflow
*****************************

Once your suite has been set up, you can run it using Cylc:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         cylc vip

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: console

         cylc vip

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: console

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
</modelling/gc_practical_exercises/running/running>` under *Exercises in
Global Configurations*.

After the workflow has completed successfully, navigate to the output directory
and try plotting the data.
