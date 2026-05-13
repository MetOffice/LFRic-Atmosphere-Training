.. _create a branch: https://metoffice.github.io/simulation-systems/WorkingPractices/gh_dev_init.html#create-a-branch
.. _example issue: https://github.com/MetOffice/momentum_user_training.example_lfric_workflow/issues/2

.. _practical_3.3:

Practical 3: Run integration tests
----------------------------------

.. admonition:: Aims

   * Run the LFRic :external+rose:doc:`tutorial/rose/furthertopics/rose-stem`
     tests.
   * Break a test, and explore the output of the test workflow.

In earlier exercises, you learned how to check out the model,
modify the source, and run it from the command line
(:ref:`practical_3.1`) and using a Cylc Workflow (:ref:`practical_3.3`).

This practical introduces integration testing using
:ref:`rose stem`, which helps test your changes.
These tests are essential for contributing code in line with model
development :ref:`working-practices-caption`.

In the command line practical, you modified the source code file
:ref:`gungho_step_mod.x90 <practical_3.1.hint.code>`.
Here, you can test whether this change is compliant with the automated
rose stem tests.

Step 1: Document and version control your code changes
++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. important::

   This document uses Git following a basic branching working pattern,
   but changes to LFRic require use of the more robust
   :external+simulation_systems:doc:`WorkingPractices/forking` approach.

Before running integration tests, it's important to document your changes
and manage them using version control. This ensures traceability and
compliance with LFRic model development practices.

1. Create an issue on GitHub (similar to an "ticket" in Trac)

   LFRic working practices documentation describes how to
   :external+simulation_systems:ref:`create_issue` to document
   your model experiment.

   This issue will provide a reference number to associate with your
   development branch.

   For the purposes of this tutorial we shall pretend to have created issue
   number ``2`` (`example issue`_).

2. Create and checkout a branch

   Use ``git switch`` to :external+simulation_systems:ref:`create_branch`:

   .. code-block:: bash

      git switch -c 2.meaningful_description
      # -c short for --create

3. Apply and commit your changes

   Copy the modified source file from the earlier
   command line practical into your branch.

   Then commit the change to version control:

   .. code-block:: bash

      # Check you diff
      git diff           # difftool if you have a graphical diff program

      # Commit your change to version control.
      git commit -a -m "Add log output to gungho_step"
      # -a short for --add
      # -m short for --message

   .. note::

      Git is a distrubuted version control system, so you would normally
      have to use ``git push`` to your changes to GitHub.

Step 2: Run the rose stem tests
+++++++++++++++++++++++++++++++

Rose stem tests are organised into
:external+simulation_systems:doc:`groups <Development/TestSuites/lfric_apps>`
allowing you to run only a subset of tests relevant to your changes.
Here we want to run the ``scripts`` group:

.. note::

   Normally you should run the ``developer`` group. ``scripts`` is a subset
   of developer which runs faster.

.. tab-set::

   .. tab-item:: Faster Style Checks

      .. code-block:: console

         cylc vip -z group=scripts -n myfeature.style ./rose-stem

   .. tab-item:: Full Developer Tests

      .. code-block:: console

         cylc vip -z group=developer -n myfeature.developer ./rose-stem

.. note:: what the arguments to Cylc mean
   :collapsible: closed

   * ``vip`` is short for ``validate-install-play``.
   * ``-z`` is short for ``--set-list`` [of template variables].
   * ``-n`` is short for ``--workflow-name``.

Then open Cylc GUI or TUI again.

All tasks in the rose stem test workflow should complete successfully.
Adding a few lines to the log output should not break any tests.

A summary of the rose stem test results can be found in the file
``~/cylc-run/lfric_apps_standard_suite/runN/trac.log``, as explained in the
:external+simulation_systems:doc:`testing your changes <Development/testing>`

This is a wiki-formatted file intended to serve as test evidence for
model development tickets. Use the file to determine how many tasks
in the test workflow succeeded.

.. hint::

   Given the benign nature of the model change, we expect all tasks in
   the rose stem test suite to pass. However, this depends on how the change
   was implemented. If you copied the code from the hint in Practical 1
   into ``gungho_step_mod.x90`` everything should work as intended.

Step 3: Break the stem test
+++++++++++++++++++++++++++

To explore how the testing framework handles style violations, you can
deliberately introduce a trailing whitespace in your code. For example,
by adding a space at the end of a line in ``gungho_step_mod.x90``.
This will cause the ``style_checker`` task to fail,
demonstrating how the system enforces coding standards.

To avoid running the full test workflow, you can use:

.. tab-set::

   .. tab-item:: Workflow finished

      .. code-block:: console

         cylc vip -z group=scripts -n myfeature.style ./rose-stem

   .. tab-item:: A task failed

      If a task failed last time you can modify your workflow and
      rerun a set of tasks:

      .. code-block:: console

         cylc validate-reinstall myfeature.broken
         cylc trigger myfeature.broken \
            //1/export-source \
            //1/export-source_azspice \
            //1/fortitude_linter

.. hint::

   The error message from the ``style checker`` test will be in
   ``~/cylc-run/lfric_apps/run*/log/job/1/myfeature.broken/01/job.err``.
