***********************
Adding a new diagnostic
***********************

In this exercise, you will add the atmospheric diagnostic **"v component of
wind on pressure levels"** back into the model configuration. This diagnostic
has been intentionally removed, and your task is to restore it by editing the
relevant XML configuration file.

The ``v_in_w3`` field represents the northward (v) component of wind
interpolated onto pressure levels. Without it, this wind component will not be
written to the model output.

Step 1: Navigate to the file directory
======================================

First, change into the directory that contains the diagnostic output
configuration files:

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

         cd app/lfric_atm/file

   .. tab-item:: Monsoon

      .. code-block:: console

         cd app/lfric_atm/file

Step 2: Open the diagnostics configuration file
================================================

Open ``file_def_diags_user.xml`` in a text editor of your choice. This file
defines which diagnostic fields are written to output for each field group.

Step 3: Locate the pressure level output group
==============================================

Search for the field group named ``lfric_stream_g``. This group controls which
fields are output on pressure levels as time-day means. You should find a block
of ``<field>`` entries that includes ``u_in_w3`` (the u component of wind) but
is missing ``v_in_w3``.

Step 4: Add the missing field for ``v_in_w3``

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: xml
         :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
         :emphasize-lines: 5

            <!-- Stream G - Monthly mean fields -->
            ...
            <field field_ref="ageofair"/>
            <field field_ref="u_in_w3"/>
            <field field_ref="v_in_w3"/>
            <field field_ref="m_v" long_name="vapour_mixing_ratio"/>

   .. tab-item:: Monsoon

      .. code-block:: xml
         :caption: trunk/app/lfric_atm/file/file_def_diags_user_temp.xml
         :emphasize-lines: 5

            <!-- Stream G - Monthly mean fields -->
            ...
            <field field_ref="ageofair"/>
            <field field_ref="u_in_w3"/>
            <field field_ref="v_in_w3"/>
            <field field_ref="m_v" long_name="vapour_mixing_ratio"/>

Add the line ``<field field_ref="v_in_w3"/>`` to include the v component of
wind in the output. Make sure to save your changes to the file.

Step 5: Run the model and check the output
==========================================

Now that you have added the missing diagnostic, run the model using what you
have learnt in the previous exercises. After the model has completed, check the
output files to confirm that the ``v_in_w3`` field is now included in the
pressure level diagnostics. You can use tools like ``ncdump`` or ``ncks`` to
inspect the contents of the output NetCDF files and verify that the v component
of wind is present.

Step 6: Visualise the ``v_in_w3`` field
========================================

To quickly visualise the new diagnostic, open the NetCDF output in ``xconv``
and display a pressure-level slice of ``v_in_w3``.

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

         xconv lfric_stream_g.nc  # replace with your output file name

   .. tab-item:: Monsoon

      .. code-block:: console

         xconv lfric_stream_g.nc  # replace with your output file name

In ``xconv``:

#. Select the variable ``v_in_w3``.
#. Choose a single ``time`` index (for example, the first output time).
#. Choose one pressure level to plot.
#. Display the field using a diverging colour scale (for example, red-blue).

This gives a quick spatial check that the field is present and has realistic
structure.

You should now have successfully added the v component of wind back into the
model output diagnostics!
