
Practical Exercises
===================

Building and running the model is usually done via `Cylc workflows <https://cylc.github.io/cylc-doc/latest/html/tutorial/introduction.html#what-is-a-workflow>`_. The follwing exercises demonstrates how to run a simplified development setup and tests. These workflows are intended for model and workflow development. Model applications for global and regional modelling are follwowing later in this training.

Practical 1: Standard Suite
---------------------------

LFRic Apps Standard Suites are availble for several computers. Workflow IDs are documented on the `LFRic Apps wiki pages <https://code.metoffice.gov.uk/trac/lfric_apps#WorkingwithLFRicApps>`_. Assuming you want to run the exercise on the Met Office Azure Spice platform you can checkout the standard suite with

.. code-block:: bash
   :linenos:
   
   rosie co u-dn674
   mv ~/roses/u-dn674 ~/cylc-src/lfric_apps_standard_suite

For other platforms chose appropiate alternative workflow IDs.

Change to ``~/cylc-src/lfric_apps_standard_suite`` explore the workflow in a text editor, look at its `graph <https://cylc.github.io/cylc-doc/stable/html/glossary.html#term-graph>`_ and the `apps <https://metomi.github.io/rose/doc/html/tutorial/rose/applications.html>`_. The standard suite extracts the model code, builds the excutable and runs a global model. It also builds the mesh generator and creates a low resolution C12 mesh as an input for the model.


.. figure:: /_static/3/lfric_apps_standard_suite.svg
  :width: 400px

  Graph of the LFRic Apps Standard Suite.

Start the workflow with

.. code-block:: bash
   :linenos:
   
   cd ~/cylc-src/lfric_apps_standard_suite
   cylc vip

Look at the workflow in the cylchub GUI while it is running, explore the model output in ``~/cylc-run/lfric_apps_standard_suite/``, and the logs Cylc Review.

Let's do two simple configuration changes to gain more expirence with the LFRic Apps Standard Suite:

1) Reduce the number of iterated time steps in the workflow by 50%. 
2) Reduce the length of the time step by 50%.

Run both experiments and compare the number of produced NetCDF files with the  

Hint: In the workflow directory ``~/cylc-src/lfric_apps_standard_suite`` navigate to ``app/lfric_atm`` and edit the configuration with rose edit (or an text editor). You need to to modify the variables ``timestep_end`` and ``dt``. The NetCDF files can be found under the path ``~/cylc-run/lfric_apps_standard_suite/run?/work/1/lfric_atm/*nc``.

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


