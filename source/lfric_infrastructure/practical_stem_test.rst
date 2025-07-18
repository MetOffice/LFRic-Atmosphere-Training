Practical 3: Run automated model tests
--------------------------------------

After learning how to run LFRic Atmosphere as a standalone :ref:`command line application <practical_3_1-caption>` and as part of a :ref:`Cylc workflow <practical_3_2-caption>` this practical introduces the running the automated `rose stem <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html>`_ tests which are required for model code development follwing the :ref:`working-practices-caption`.

Set-up a practical folder and copy in the model code:

.. code-block:: bash

   mkdir practical_stem_test
   cd  practical_stem_test
   fcm co fcm:lfric_apps.x_tr lfric_apps

In the :ref:`command line application practical <practical_3_1-caption>` you modfied the the source code file ``gungho_step_mod.x90``. Here you can test if this change is compliient with the automated tests. Copy your modified code into the pristine code directory:

.. code-block:: bash

   cp ../practical_command_line/lfric_apps/science/gungho/source/driver/gungho_step_mod.x90 lfric_apps/science/gungho/source/driver/gungho_step_mod.x90

Change to ``lfric_apps`` and confirm that is contains your modified code:

.. code-block:: bash

   cd lfric_apps
   svn diff

And now run the test

.. code-block:: bash

   rose stem --group=lfric_atm_developer
   cylc play <working copy name>
   cylc gui

