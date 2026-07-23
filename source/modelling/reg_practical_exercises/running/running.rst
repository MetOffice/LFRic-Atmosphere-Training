*********************************
Running a Regional LFRic Workflow
*********************************

Once your suite has been set up, you can run it using Cylc.

Navigate to your suite directory
----------------------------------------

Open a terminal and move to the suite directory, replacing ``<suite-id>`` with
the suite ID that ``rosie`` reported when you copied the workflow:

.. code-block:: console

   cd ~/roses/<suite-id>

Run the workflow
-----------------------

Validate the workflow, install it to ``~/cylc-run``, and play it using:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         cylc vip --opt-conf-key=meto-exab

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: console

         cylc vip --opt-conf-key=monsoon

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: console

         cylc vip --opt-conf-key=<yoursite>

``cylc vip`` is short for ``cylc validate-install-play``, and performs three
actions:

- **Validate**: Checks the suite configuration for errors
- **Install**: Sets up the runtime environment
- **Play**: Starts executing the workflow

Site settings are stored as Rose :external+rose:ref:`optional configuration`
files, so a configuration file ``opt/rose-suite-yoursite.conf`` is selected
with ``-O yoursite``. This works the same way as in the global practical.

Monitor the workflow
----------------------------

Once the suite is running, you can monitor its progress using either of the
following commands:

.. include:: /include/cylc-gui.rst

These tools allow you to view task status, progress, and any failures.

For more details on Cylc commands, see :doc:`Running a Cylc Workflow
</modelling/gc_practical_exercises/running/running>` under *Exercises in
Global Configurations*.

After the workflow has completed successfully, navigate to the output directory
and try plotting the data.
