.. The stream G field list used by the "add a diagnostic" exercise.
.. To use it: .. include:: /include/snippets/diags-user-xml.rst

.. code-block:: xml
   :caption: app/lfric_atm/file/file_def_diags_user.xml
   :emphasize-lines: 5

   <!-- Stream G - Monthly mean fields -->
   ...
   <field field_ref="ageofair"/>
   <field field_ref="u_in_w3"/>
   <field field_ref="v_in_w3"/>
   <field field_ref="m_v" long_name="vapour_mixing_ratio"/>
