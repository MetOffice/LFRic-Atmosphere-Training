Practical 3: Run integration tests
----------------------------------

In earlier exercises, you learned how to check out the model, modify the source, and run it from the :ref:`command line <practical_3_1-caption>` and via :ref:`Cylc <practical_3_2-caption>`.

This practical introduces integration testing using `rose stem <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html>`_, which helps ensure your changes work correctly within the system. These tests are essential for contributing code in line with model development :ref:`working practices <working-practices-caption>`.

In the :ref:`command line application <practical_3_1-caption>` practical, you modified the source code file :ref:`gungho_step_mod.x90 <practical_3_1-hint_code>`. Here, you can test whether this change is compliant with the automated rose stem tests.

**Document and version control your code changes**

Before running integration tests, it's important to document your changes and manage them using version control. This ensures traceability and compliance with LFRic model development practices.

*1. Create a Ticket*

Start with `creating a ticket <https://metoffice.github.io/simulation-systems/WorkingPractices/tickets.html#>`_ by opening a `new ticket <https://code.metoffice.gov.uk/trac/lfric_apps/newticket>`_ on the LFRic Apps ticketing system to document your model experiment.

.. figure:: /_static/3/practical_rose_stem_ticket.png
  :width: 625px

  LFRic Apps ticket for documenting your model experiment.

This ticket will provide a reference number to associate with your development branch.

*2. Create and Checkout a Branch*

Use `fcm bc <https://metomi.github.io/fcm/doc/user_guide/code_management.html#svn_branching>`_ to `create a branch <https://metoffice.github.io/simulation-systems/WorkingPractices/branches.html>`_:

.. code-block:: bash

   fcm bc --ticket=NNN --type=dev branchname fcm:lfric_apps.x_tr@vnXX.Y

Replace:

- ``NNN`` with your ticket number,
- ``branchname`` with a descriptive name (e.g. practical_stem_test),
- ``vnXX.Y`` with the `release version <https://code.metoffice.gov.uk/trac/lfric_apps/wiki#Releases>`_ (e.g. vn2.2).

Then, check out the branch using your MOSRS ``USERNAME``:

.. code-block:: bash

   svn co https://code.metoffice.gov.uk/svn/lfric_apps/main/branches/dev/USERNAME/vn2.2_practical_stem_test vn2.2_practical_stem_test

*3. Apply and Commit Your Changes*

Implement the modified source file from the earlier :ref:`command line practical <practical_3_1-caption>` into your working copy in:

.. code-block:: bash

   vn2.2_practical_stem_test/practical_command_line/lfric_apps/science/gungho/source/driver/gungho_step_mod.x90

Then commit the change to version control:

.. code-block:: bash

  cd vn2.2_practical_stem_tes
  svn ci -m "Add log output to gungho_step"

Verify that your `change <https://code.metoffice.gov.uk/trac/lfric_apps/changeset/12764/main/branches/dev/bjoernfock/vn2.2_practical_stem_test>`_ has been successfully uploaded to the repository.

**Run the rose stem tests**

Rose stem tests are organised into `groups <https://metoffice.github.io/simulation-systems/WorkingPractices/TestSuites/lfric_apps.html#rose-stem>`_, allowing you to run only a subset of tests relevant to your changes. Here we want to run the ``lfric_atm_developer`` group:

.. code-block:: bash

   rose stem --group=lfric_atm_developer
   cylc play <working copy name> # hint: working copy name is lfric_apps
   cylc gui

All tasks in the rose stem test workflow should complete successfully - adding a few lines to the log output should not break any tests.

A summary of the rose stem test results can be found in the file ``~/cylc-run/lfric_apps/run*/trac.log``, as explained in the `Testing Your Change <https://metoffice.github.io/simulation-systems/WorkingPractices/testing.html#trac-log>`_ documentation. This is a wiki-formatted file intended to serve as test evidence for model development tickets. Use the file to determine how many tasks in the test workflow succeeded.

.. hint:: Given the benign nature of the model change, we expect all tasks in the rose stem test suite to pass. However, this depends on how the change was implemented. If you copied the :ref:`code <practical_3_1-hint_code>` from the hint in Practical 1 into ``gungho_step_mod.x90``, everything should work as intended.

**Break the stem test**

To explore how the testing framework handles style violations, you can deliberately introduce a trailing whitespace in your code - for example, by adding a space at the end of a line in ``gungho_step_mod.x90``. This will cause the ``style_checker`` task to fail, demonstrating how the system enforces coding standards.

To avoid running the full test workflow, you can use:

.. code-block:: bash

   rose stem --group=scripts
   cylc play <working copy name>
   cylc gui

This runs only the style-checking tests. Other groups, such as ``lfric_atm_developer``, are available for different testing scopes depending on your development focus.

.. hint:: The error message from the ``style checker`` test will be in ``~/cylc-run/lfric_apps/run*/log/job/1/style_checker/01/job.err``.
