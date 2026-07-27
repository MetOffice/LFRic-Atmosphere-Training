*********************************
Running a Regional LFRic Workflow
*********************************

Once your suite has been set up, you can run it using Cylc.

Navigate to your suite directory
----------------------------------------

Open a terminal and move to the suite directory, replacing ``<suite-id>`` with
the suite ID that ``rosie`` reported when you copied the workflow:

.. code-block:: bash

   cd ~/roses/<suite-id>

Run the workflow
-----------------------

Validate the workflow, install it to ``~/cylc-run``, and play it using:

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

   Unlike the global suite, the regional nesting suite takes its platform
   from the ``SITE`` and ``EX HOST`` settings you chose in the Rose GUI, so
   no ``--opt-conf-key`` is needed here. If your copy does ship optional
   configurations, they are in ``opt/`` and are selected with ``-O``, as
   described in the global practical.

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
