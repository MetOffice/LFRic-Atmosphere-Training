***********************
Adding a new diagnostic
***********************

The atmospheric diagnostic “v component of wind on pressure levels" is missing from this model. Use the following  instructions to add it back to the configuration.

.. code-block:: bash

   cd app/lfric_atm/file

* Open ``file_def_diags_user_temp.xml``.
* Find ``lfric_pressure_level_tdaym``.
* Add a new field for ``v_in_w3``:

.. code-block:: xml
   :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
   :emphasize-lines: 3

   <field field_ref="processed__pressure_in_w3"/>
   <field field_ref="u_in_w3"/>
   <field field_ref="v_in_w3"/>
   <field field_ref="w_in_w3"/>
   </field_group>