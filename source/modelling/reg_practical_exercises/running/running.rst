*********************************
Running a Regional LFRic Workflow
*********************************

Once your suite has been set up, you can run it using Cylc.

Navigate to your suite directory
----------------------------------------

Open a terminal and move to the suite directory:

.. tab-set::

    .. tab-item:: Met Office

        .. code-block:: bash

            cd ~/roses/u-by395

    .. tab-item:: Monsoon

        .. include:: /include/monsoon3-help.rst

        .. code-block:: bash

            cd ~/roses/u-by395/u-by395_lfric_monsoon3


Run the workflow
-----------------------

Start the workflow using:

.. code-block:: bash

   cylc vip

This command performs three actions:

- **Verify**: Checks the suite configuration for errors
- **Install**: Sets up the runtime environment
- **Play**: Starts executing the workflow

Monitor the workflow
----------------------------

Once the suite is running, you can monitor its progress using either of the following commands:

.. include:: /include/x11-forwarding.rst

- Graphical interface:

  .. code-block:: bash

     cylc gui

- Terminal-based interface:

  .. code-block:: bash

     cylc tui

These tools allow you to view task status, progress, and any failures.

For more details on Cylc commands, see the section *"Running a Rose workflow"* under *"Exercises in Global Configurations"* in this tutorial.

After the workflow has completed successfully, navigate to the output directory and try plotting the data.
