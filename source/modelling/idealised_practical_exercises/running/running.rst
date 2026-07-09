*****************************
Running an Idealised Workflow
*****************************

Once your suite has been set up, you can run it using cylc:

.. code-block:: bash

   cylc vip

As a reminder, this command performs three actions:

- **Verify**: Checks the suite configuration for errors
- **Install**: Sets up the runtime environment
- **Play**: Starts executing the workflow

Monitor the workflow
--------------------

Once the suite is running, you can monitor its progress using either of the following commands:

- Graphical interface:

  .. code-block:: bash

     cylc gui

- Terminal-based interface:

  .. code-block:: bash

     cylc tui

These tools allow you to view task status, progress, and any failures.

For more details on Cylc commands, see the section *"Running a Rose workflow"* under *"Exercises in Global Configurations"* in this tutorial.

After the workflow has completed successfully, navigate to the output directory and try plotting the data.
