***********************
Adding a new diagnostic
***********************

In this exercise, you will add the atmospheric diagnostic **"v component of wind on pressure levels"** back into the model configuration. This diagnostic has been intentionally removed, and your task is to restore it by editing the relevant XML configuration file.

The ``v_in_w3`` field represents the northward (v) component of wind interpolated onto pressure levels. Without it, this wind component will not be written to the model output.

Step 1: Navigate to the file directory
======================================

First, change into the directory that contains the diagnostic output configuration files:

.. code-block:: bash

   cd app/lfric_atm/file

Step 2: Open the diagnostics configuration file
================================================

Open ``file_def_diags_user_temp.xml`` in a text editor of your choice. This file defines which diagnostic fields are written to output for each field group.

Step 3: Locate the pressure level output group
==============================================

Search for the field group named ``lfric_pressure_level_tdaym``. This group controls which fields are output on pressure levels as time-day means. You should find a block of ``<field>`` entries that includes ``u_in_w3`` (the u component of wind) and ``w_in_w3`` (the vertical wind component), but is missing ``v_in_w3``.

Step 4: Add the missing field for ``v_in_w3``

.. code-block:: xml
   :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
   :emphasize-lines: 3

   <field field_ref="processed__pressure_in_w3"/>
   <field field_ref="u_in_w3"/>
   <field field_ref="v_in_w3"/>
   <field field_ref="w_in_w3"/>
   </field_group>

Add the line ``<field field_ref="v_in_w3"/>`` to include the v component of wind in the output. Make sure to save your changes to the file.

Step 5: Run the model and check the output
==========================================

Now that you have added the missing diagnostic, run the model using what you have learnt in the previous exercises. After the model has completed, check the output files to confirm that the ``v_in_w3`` field is now included in the pressure level diagnostics. You can use tools like ``ncdump`` or ``ncks`` to inspect the contents of the output NetCDF files and verify that the v component of wind is present.

You should now have successfully added the v component of wind back into the model output diagnostics!