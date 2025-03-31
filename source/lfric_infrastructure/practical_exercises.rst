
Practical Exercises
===================

Building and running the model is usually done via `Cylc workflows <https://cylc.github.io/cylc-doc/latest/html/tutorial/introduction.html#what-is-a-workflow>`_. The following exercises demonstrates how to run a simplified development setup and tests. These workflows are intended for model and workflow development. Model applications for global and regional modelling are following later in this training.


.. include:: practical_standart_suite.rst


Practical 2: Model build and  stem tests
----------------------------------------

Check out the source code and run lfric_atm_developer `rose stem test <https://metomi.github.io/rose/doc/html/tutorial/rose/furthertopics/rose-stem.html>`_ and the related `Cylc <https://cylc.github.io/cylc-doc/latest/html/  index.html>`_ workflow to compile the model:

.. code-block:: bash
   :linenos:
   :emphasize-lines: 4,5

   fcm co fcm:lfric_apps.x_tr lfric_apps_tr
   cd lfric_apps_tr
   export CYLC_VERSION=8
   rose stem --group=lfric_atm_developer
   cylc play <working copy name>
   cylc gui




Practical 3: Code Change
------------------------


