*******************************************
Experiment 3 - Size of initial perturbation
*******************************************

The initial temperature field in the suite is perturbed by a small random noise to induce convective motions, which subsequently grow larger due to convective instability.
To test the sensitivity of the experiment outcome to this perturbation, we suggest changing the amplitude of this perturbation and comparing the results to the control experiment.

The parameters that control the initial perturbation are: ``perturb_init`` (to switch it on), ``perturb_magnitude`` (base-10 logarithm of the perturbation magnitude), and ``perturb_seed`` - random seed.
In the GUI, they are stored in the **lfric_atm** -> Run Task Settings -> Job -> Initial Conditions.

In the configuration file the namelist is 

.. code-block:: ini
   :caption: app/lfric_atm/rose-app.conf
   :emphasize-lines: 3,4,5

   [namelist:idealised]
   f_lon_deg=0.0
   perturb_init=.true.
   perturb_magnitude=1
   perturb_seed=180906
   test='specified_profiles'

.. Note:: There are other perturbation options in the "Temperature" tab, e.g. `perturb` and `pert_width_scaling`, but we are not using them in this practical.

Step 1: Change perturbation magnitude
-------------------------------------

1. Open Rose GUI or ``app/lfric_atm/rose-app.conf`` a text editor of your choice.
2. Search for the ``perturb_init`` key
3. Change the value from ``0`` to ``1`` (or ``2``)

Step 2: Run the model
---------------------

Now that you have changed the configuration, run the model using what you have learnt in the previous exercises.
Check the output using Python or another tool of your choice

Step 3. Compare with the default configurations
-----------------------------------------------

Using a Python script or Jupyter Notebook, make plots for both experiments and compare them to each other to see the effect of the perturbation magnitude.