******************************
Experiment 1 - Adding rotation
******************************

In this experiment, we will enable the effects of rotation.

Note that even though the rotation rate is non-zero:

.. code-block:: ini
   :caption: app/lfric_atm/rose-app.conf
   :emphasize-lines: 4

   [namelist:planet]
   cp=14300.00
   gravity=9.81
   omega=7.292116E-5
   p_zero=100000.0
   rd=4124.00
   scaling_factor=1.0

rotation is actually switched off in the equations formulation section:

.. code-block:: ini
    :caption: app/lfric_atm/rose-app.conf
    :emphasize-lines: 14

    [namelist:formulation]
    dlayer_on=.true.
    dry_static_adjust=.true.
    eos_method='sampled'
    exner_from_eos=.false.
    horizontal_physics_predictor=.false.
    horizontal_transport_predictor=.false.
    init_exner_bt=.true.
    l_multigrid=.true.
    lagged_orog=.true.
    moisture_formulation='traditional'
    moisture_in_solver=.true.
    p2theta_vert=.true.
    rotating=.false.
    shallow=.true.
    si_momentum_equation=.false.
    theta_moist_source=.true.
    use_multires_coupling=.false.
    use_physics=.true.
    use_wavedynamics=.true.
    vector_invariant=.false.


.. grid:: 2
   :gutter: 2

   .. grid-item::

      .. _fig-planet_namelist_omega:

      .. figure:: /_static/planet_namelist_omega.png
         :alt: Planetary parameters section in Rose GUI

         Rose GUI: planetary parameters (``planet`` namelist).

   .. grid-item::

      .. _fig-dynamics_namelist_rotating:

      .. figure:: /_static/dynamics_namelist_rotating.png
         :alt: Dynamics parameters section in Rose GUI

         Rose GUI: dynamics parameters enabling rotation (``formulation`` namelist).

**So we first enable rotation and then we can also play with
the rotation rate.**


Step 1: Switch on rotation
--------------------------

1. Open Rose GUI or ``app/lfric_atm/rose-app.conf`` in a text
   editor of your choice
2. Search for the ``rotating`` key.
3. Change it to ``.true.``.

Step 2: Run the model
---------------------

Now run the model using what you have learnt in the previous exercises.
Check the output using Python or another tool of your choice.

Step 3. Compare with the control experiment
-------------------------------------------

Using a Python script or Jupyter Notebook, make plots for both
experiments and compare them to each other to see the effect of rotation.
