Practical 3: Run automated model tests
--------------------------------------

After learning how to run LFRic Atmosphere as a standalone :ref:`command line application <practical_3_1-caption>` and as part of a :ref:`Cylc workflow <practical_3_2-caption>`, this practical introduces the automated `rose stem <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html>`_ tests. These tests are required for model code development in accordance with the :ref:`working-practices-caption`.

Set up a new folder for this practical and copy in the model code:

.. code-block:: bash

   mkdir practical_stem_test
   cd  practical_stem_test
   fcm co fcm:lfric_apps.x_tr lfric_apps

In the :ref:`command line application <practical_3_1-caption>` practical, you modified the source code file :ref:`gungho_step_mod.x90 <practical_3_1-hint_code>`. Here, you can test whether this change is compliant with the automated rose stem tests. Copy your modified file into the pristine code directory:

.. code-block:: bash

   cp ../practical_command_line/lfric_apps/science/gungho/source/driver/gungho_step_mod.x90 lfric_apps/science/gungho/source/driver/gungho_step_mod.x90

Change into the ``lfric_apps`` directory and confirm that it contains your modified code:

.. code-block:: bash

   cd lfric_apps
   svn diff

**Run the rose stem tests**

.. code-block:: bash

   rose stem --group=lfric_atm_developer
   cylc play <working copy name> # hint: working copy name is lfric_apps
   cylc gui

All tasks in the rose stem test workflow should complete successfully - adding a few lines to the log output should not break any tests.

A summary of the rose stem test results can be found in the file ``~/cylc-run/lfric_apps/run*/trac.log``, as explained in the `Testing Your Change <https://metoffice.github.io/simulation-systems/WorkingPractices/testing.html#trac-log>`_ documentation. This is a wiki-formatted file intended to serve as test evidence for model development tickets. Use the file to determine how many tasks in the test workflow succeeded.

.. hint:: Given the benign nature of the model change, we expect all tasks in the rose stem test suite to pass. However, this depends on how the change was implemented. If you copied the :ref:`code <practical_3_1-hint_code>` from the hint in Practical 1 into ``gungho_step_mod.x90``, everything should work as intended.

   To explore how the testing framework handles style violations, you can deliberately introduce a trailing whitespace in your code - for example, by adding a space at the end of a line in ``gungho_step_mod.x90``. This will cause the ``style_checker`` task to fail, demonstrating how the system enforces coding standards.

   To avoid running the full test workflow again, use the command ``rose stem --group=scripts`` to run only the relevant style-checking tests.
