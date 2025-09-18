***********************
Adding a new diagnostic
***********************

The atmospheric diagnostic “v component of wind on pressure levels" is missing from this model. Use the following  instructions to add it back to the configuration.

* cd into ``app/lfric_atm/file``
* open ``file_def_diags_user_temp.xml``
* find ``lfric_pressure_level_tdaym``
* add in a new field for ``v_in_w3``

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
   :emphasize-lines: 3

   <field field_ref="processed__pressure_in_w3"/>
   <field field_ref="u_in_w3"/>
   <field field_ref="v_in_w3"/>
   <field field_ref="w_in_w3"/>
   </field_group>

Experiment 1 - CO2 x 10
^^^^^^^^^^^^^^^^^^^^^^^
* cd into ``app/lfric_atm``
* open the ``rose-app.conf``
* search for ``co2_mix_ratio``
* change this value from 5.60353e-04 to 5.60353e-03

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/rose-app.conf
   :emphasize-lines: 6

   [namelist:well_mixed_gases]
    cfc113_mix_ratio=0.0
    cfc11_mix_ratio=0.0
    cfc12_mix_ratio=4.3919e-09
    ch4_mix_ratio=9.8200e-07
    co2_mix_ratio=5.6062e-03
    hcfc22_mix_ratio=0.0
    hfc134a_mix_ratio=3.6811e-10
    n2_mix_ratio=0.7553
    n2o_mix_ratio=4.7957e-07
    o2_mix_ratio=0.2314
    so2_mix_ratio=0.0

