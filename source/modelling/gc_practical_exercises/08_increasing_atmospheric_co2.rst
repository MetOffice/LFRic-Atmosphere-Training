***********************
Experiment 1 - CO2 x 10
***********************

In this experiment, you will increase the atmospheric CO2 concentration by a
factor of 10 to observe its effect on the model climate.

Step 1: Navigate to the application directory
=============================================
Start by changing into the ``lfric_atm`` application directory of the suite you
copied earlier:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/lfric-atm-app-dir.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. include:: /include/snippets/lfric-atm-app-dir.rst

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. include:: /include/snippets/lfric-atm-app-dir.rst

Step 2: Edit the configuration file
===================================
1. Open ``rose-app.conf`` in a text editor of your choice.
2. Search for the ``co2_mix_ratio`` key (located under the
   ``[namelist:radiative_gases]`` section).
3. Change the value from ``5.6062e-04`` (present-day CO2) to ``5.6062e-03``
   (10x present-day CO2), as highlighted below.

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/radiative-gases-namelist.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. include:: /include/snippets/radiative-gases-namelist.rst

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      .. include:: /include/snippets/radiative-gases-namelist.rst

Step 3: Run the model and check the output
==========================================

Now that you have increased the CO2 concentration, run the model using what you
have learnt in the previous exercises. After the model has completed, check the
output files to observe the impact of the increased CO2 on the model climate.
You can use tools like ``ncdump``, ``xconv``, or ``python`` to inspect the
contents of the output NetCDF files and verify the changes.

You should now have successfully completed the CO2 x 10 experiment!
