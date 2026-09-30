.. _practical_3.2:

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

.. code-block:: bash

   mkdir ${HOME}/cylc-src
   cd ${HOME}/cylc-src

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         git clone \
               git@github.com:MetOffice/momentum_user_training.example_lfric_workflow.git \
               lfric_apps_standard_suite

   .. tab-item:: Monsoon
      :sync: monsoon

      Clone over HTTPS on Monsoon3, authenticating with a personal access
      token as described in `Git on Monsoon3`_:

      .. code-block:: bash

         git clone \
               https://github.com/MetOffice/momentum_user_training.example_lfric_workflow.git \
               lfric_apps_standard_suite

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. include:: /include/isambard3-help.rst

      The repository above is not available outside the Met Office. On
      Isambard 3, use the Met Office workflow ``u-dn704`` instead. It has the
      same tasks, and runs a global model on a C12 mesh. Check it out from
      MOSRS (see :ref:`isambard3-mosrs`), at the revision that has been
      tested on Isambard 3:

      .. code-block:: bash

         mosrs-cache-password
         rosie checkout u-dn704
         svn update -r 361458 ~/roses/u-dn704

      Then get the scripts that adapt and launch it on Isambard 3:

      .. code-block:: bash

         git clone https://github.com/ickc/lfric-env-isambard.git \
               "$SCRATCHDIR/lfric-env-isambard"

      In the rest of this practical, use ``~/roses/u-dn704`` wherever the
      text says ``~/cylc-src/lfric_apps_standard_suite``, and ``u-dn704``
      wherever it uses ``lfric_apps_standard_suite`` as the workflow name.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      Consult your site's documentation for cloning git repositories, then
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

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         cylc vip

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: bash

         cylc vip

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. code-block:: bash

         bash "$SCRATCHDIR/lfric-env-isambard/examples/science-suites/run-suite.sh" \
               u-dn704

      This adds the Isambard 3 settings to your copy of the workflow, then
      runs ``cylc vip`` on it. Run it on a login node; Cylc submits the tasks
      to Slurm. The build takes about ten minutes once its job starts.

   .. tab-item:: Other
      :sync: other

      .. code-block:: bash

         cylc vip

While the workflow is running, open the Cylc interface to explore the model
output:

.. include:: /include/x11-forwarding.rst

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      Navigate to `Cylc Hub <https://cylchub>`_ and open the workflow there.

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      Use the terminal interface:

      .. code-block:: bash

         cylc tui

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. include:: /include/isambard3-help.rst

      Use the terminal interface:

      .. code-block:: bash

         cylc tui

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      Use the Cylc interface supported by your site:

      .. code-block:: bash

         cylc gui

      If a graphical interface is not available, use the terminal interface:

      .. code-block:: bash

         cylc tui


Step 4: View the workflow running, logs and outputs
+++++++++++++++++++++++++++++++++++++++++++++++++++

View your logs:

.. tab-set::

   .. tab-item:: Cylc GUI

      Navigate to or open the Cylc GUI, and click on each task to view logs.

      On the command line ``cylc gui`` will open either a new gui or a
      window on your site's Cylc Hub.

      Task logs can be found by clicking on task icons.

   .. tab-item:: Cylc TUI

      On the command line type ``cylc tui``.

      Task logs can be found by clicking on task icons.

   .. tab-item:: Cylc Review

      * At the Met Office navigate to `Cylc Review <https://cylchub/services/cylc-review/>`_
      * Navigate to your site's Cylc Review instance.
      * Start Cylc Review with ``cylc review start``

   .. tab-item:: Command line

      For each task in the workflow:

      .. code-block:: bash

         cat ~/cylc-run/lfric_apps_standard_suite/runN/log/job/1/<task_name>/job.out

.. admonition:: Task

   From the logs find out how many time steps were executed and locate
   the output files in NetCDF format.

.. note:: Isambard 3

   The model runs on several MPI ranks, and each writes its own log. Look in
   ``~/cylc-run/u-dn704/runN/work/1/lfric_atm/PET00.lfric_atm.Log``.

Step 5: Modify the configuration
++++++++++++++++++++++++++++++++

To gain more experience with the LFRic Apps Standard Suite, make the
following configuration changes:

1. Reduce the number of iterated time steps in the workflow by 50%.
2. Reduce the length of the time step by 50%.

Then, re-run the workflow for each change (or combine them) and compare:

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

.. note:: Isambard 3

   Edit ``~/roses/u-dn704/app/lfric_atm/rose-app.conf``. You do not need to
   rebuild the model to re-run it. Remove the previous output, then reinstall
   the workflow and run only the model task again:

   .. code-block:: bash

      rm ~/cylc-run/u-dn704/runN/work/1/lfric_atm/*.nc
      cd ~/roses/u-dn704
      cylc vr u-dn704
      cylc trigger u-dn704//1/lfric_atm
