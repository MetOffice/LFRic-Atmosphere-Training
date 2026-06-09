*******************************************
Experiment 1 - Size of initial perturbation
*******************************************

In this experiment, the initial temperature field is perturbed by a small random noise to induce convective motions, which subsequently grow larger due to convective instability.
To test the sensitivity of the experiment outcome to this perturbation, we suggest changing the amplitude of this perturbation and comparing the results to the control experiment.

The parameters that control the initial perturbation are:



Step 1: Navigate to the application directory
=============================================
Start by changing into the ``lfric_atm`` application directory:

.. code-block:: bash

   cd app/lfric_atm

Step 2: Edit the configuration file
===================================
1. Open ``rose-app.conf`` in a text editor of your choice.
2. Search for the ``co2_mix_ratio`` key (located under the
   ``[namelist:radiative_gases]`` section).
3. Change the value from ``5.6062e-04`` (present-day CO2) to ``5.6062e-03``
   (10x present-day CO2), as highlighted below.

.. code-block:: ini
   :caption: trunk/app/lfric_atm/rose-app.conf
   :emphasize-lines: 9

   [namelist:radiative_gases]
   ch4_mix_ratio=9.8200e-07
   ch4_rad_opt='constant'
   !!co2_clim_fcg_levls=
   !!co2_clim_fcg_nyears=
   !!co2_clim_fcg_rates=
   !!co2_clim_fcg_years=
   co2_mix_ratio=5.6062e-04
   co2_rad_opt='constant'

Step 3: Run the model and check the output
==========================================

Now that you have increased the CO2 concentration, run the model using what you have learnt in the previous exercises. After the model has completed, check the output files to observe the impact of the increased CO2 on the model climate. You can use tools like ``ncdump``, ``xconv``, or ``python`` to inspect the contents of the output NetCDF files and verify the changes.

You should now have successfully completed the CO2 x 10 experiment!