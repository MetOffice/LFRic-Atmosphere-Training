Practical 2: Running the LFRic Apps Standard Suite
--------------------------------------------------

In :ref:`practical_3.1` you ran the LFRic atmosphere model from the
command line, this second practical will introduce how to run it as
part of a :external+cylc:term:`workflow`.
We will be using the LFRic Apps Standard Suite.

.. admonition:: Aims: You will learn how to:

   * Run the model in a simple Cylc workflow.
   * Locate model outputs and logs.
   * Make configuration changes.


Step 1: Check Out the Standard Suite
++++++++++++++++++++++++++++++++++++

.. TODO - this is a temporary fix - once the LFRic team have a more permenant
.. soultion we should ditch this workflow.

.. code-block:: console

   mkdir ${HOME}/cylc-src
   cd cylc-src

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

         git clone \
               git@github.com:MetOffice/momentum_user_training.example_lfric_workflow.git \
               lfric_apps_standard_suite

   .. tab-item:: Partner

      Consult your site's documentation for cloning git repositories,
      then
      clone:

      ``MetOffice/momentum_user_training.example_lfric_workflow.git``

Step 2: Explore the workflow
++++++++++++++++++++++++++++

1. Navigate to the workflow development (source) directory:

   .. code-block:: bash

      cd ${HOME}/cylc-src/lfric_apps_standard_suite

2. Open the workflow files in a text editor and explore its structure:

   * Examine the workflow's :external+cylc:term:`graph` and the
     :external+rose:term:`rose application`.
   * The standard suite performs the following tasks:

      * Extracts the model code
      * Builds the executable
      * Runs a global model simulation
      * Builds the mesh generator
      * Creates a low-resolution C12 mesh as input for the model

   .. admonition:: Task

      Can you match each task description above with a folder in the
      ``app`` directory?

   .. _fig-infra-standard-suite:

   .. graphviz::
      :caption: Graph of the LFRic Apps Standard Suite.

      digraph {
         graph [fontname="sans" fontsize="25"]
         node [fontname="sans"]
         rankdir="LR"
         "build_lfric_atm" -> "lfric_atm"
         "build_mesh" -> "generate_mesh"
         "extract" -> "build_lfric_atm"
         "extract" -> "build_mesh"
         "generate_mesh" -> "lfric_atm"
      }

   .. n.b. To regenerate the graph, use
   .. cylc graph . --transpose --output graph.dot

Step 3: Run the workflow
++++++++++++++++++++++++

Start the workflow with:

.. code-block:: bash

   cylc vip

While the workflow is running, open the Cylc GUI explore the model
output:

.. tab-set::

   .. tab-item:: Partner

      .. code-block:: console

         cylc gui

   .. tab-item:: Partner (Command Line)

      .. code-block:: console

         cylc tui

   .. tab-item:: Met Office

      Navigate to `Cylc Hub <https://cylchub>`_


Step 4: View the workflow running, logs and outputs
+++++++++++++++++++++++++++++++++++++++++++++++++++

View your logs:

.. tab-set::

   .. tab-item:: Cylc GUI

      Navigate to or open the Cylc GUI, and click on each task to
      view logs.

      On the command line ``cylc gui`` will open either a new gui or a
      window on your site's Cylc Hub.

      Task logs can be found by clicking on task icons.

   .. tab-item:: Cylc TUI

      On the command line type ``cylc tui``.

      Task logs can be found by clicking on task icons.

   .. tab-item:: Cylc Review

      * At the Met Office navigate to `Cylc Review
        <https://cylchub/services/cylc-review/>`_
      * Navigate to your site's Cylc Review instance.
      * Start Cylc Review with ``cylc review start``

   .. tab-item:: Command line

      For each task in the workflow:

      .. code-block:: console

         cat ~/cylc-run/lfric_apps_standard_suite/runN/log/job/1/<task_name>/job.out

.. admonition:: Task

   From the logs find out how many time steps were executed and locate
   the output files in NetCDF format.

Step 5: Modify the configuration
++++++++++++++++++++++++++++++++

To gain more experience with the LFRic Apps Standard Suite, make the
following configuration changes:

1. Reduce the number of iterated time steps in the workflow by 50%.
2. Reduce the length of the time step by 50%.

Then, re-run the workflow for each change (or combine them) and
compare:

* The number of produced NetCDF files
* The forecast duration

.. hint::
   :collapsible: closed

   In the workflow directory ``~/roses/lfric_apps_standard_suite``
   navigate to ``app/lfric_atm`` and edit the configuration
   ``rose-app.conf``.

   You need to modify the variables ``timestep_end`` and ``dt``.
   The NetCDF files can be found under the path
   ``~/cylc-run/lfric_apps_standard_suite/runN/work/1/lfric_atm/*nc``.

