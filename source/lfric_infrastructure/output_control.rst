.. _iodef.xml example: https://github.com/MetOffice/lfric_apps/blob/main/applications/lfric_atm/example/iodef.xml
.. _XIOS documentation: https://forge.ipsl.jussieu.fr/ioserver/wiki/documentation

.. _output-control:

Output Control
==============

LFRic Atmosphere uses `XIOS <https://forge.ipsl.jussieu.fr/ioserver>`_ (XML
I/O Server) to manage model output. XIOS runs as a separate I/O server process
alongside the model and writes NetCDF files asynchronously, so that I/O does
not stall the model computation.

The output is configured entirely through an XML file called ``iodef.xml``. You
do not need to recompile the model to change what is written, how often, or to
which files. This makes it straightforward to add diagnostics, change output
frequencies, or enable checkpointing without touching any Fortran source.

The ``iodef.xml`` file
----------------------

The `iodef.xml example`_ file in the LFRic Apps repository shows the structure
used by the LFRic Atmosphere example configuration. A trimmed outline looks like
this:

.. code-block:: xml

   <simulation>
     <context id="gungho_atm">

       <!-- Variable, axis, domain, and grid definitions (sourced from metadata) -->
       <variable_definition src="../metadata/variable_def_main.xml"/>
       <axis_definition src="../metadata/axis_def_main.xml"/>
       <domain_definition src="../metadata/domain_def_main.xml"/>
       <grid_definition src="../metadata/grid_def_main.xml"/>

       <!-- Available field definitions (the model's output catalogue) -->
       <field_definition src="../metadata/lfric_dictionary.xml"/>
       <field_definition src="../metadata/field_def_diags.xml"/>

       <!-- Output file definitions -->
       <file_definition type="one_file" time_counter="none">
         <file id="lfric_diag" name="lfric_diag"
               output_freq="6h" convention="UGRID" enabled=".TRUE.">
           <field field_ref="theta" />
           <field field_ref="rho" />
           ...
         </file>
       </file_definition>

     </context>
   </simulation>

The key parts are:

* **Field definitions** — the metadata files list all fields the model *can*
  write, giving each a unique ``id``. You cannot write a field that is not
  defined here.
* **File definitions** — each ``<file>`` element describes one output NetCDF
  file: its name, output frequency, and the set of fields to include.
* **Field references** — each ``<field field_ref="..."/>`` inside a
  ``<file>`` selects a field from the definitions above.

Output files
------------

The example configuration produces three UGRID NetCDF files:

.. list-table::
   :header-rows: 1

   * - File
     - Content
     - Default frequency
   * - ``lfric_diag``
     - Atmospheric diagnostics (temperature, moisture, winds, radiation,
       surface fields, and more)
     - 6 hours
   * - ``lfric_averages``
     - Time-averaged fields (potential temperature, Exner pressure, wind
       components)
     - 12 hours
   * - ``lfric_initial``
     - Initial-condition fields written once at the start of the run
     - Once (first time step)

Checkpoint files (``lfric_checkpoint_write`` and ``lfric_checkpoint_read``)
are also defined in the file but are disabled by default
(``enabled=".FALSE."``).

Controlling output
------------------

**Enabling or disabling a file**

Set ``enabled=".TRUE."`` or ``enabled=".FALSE."`` on a ``<file>`` element:

.. code-block:: xml

   <file id="lfric_averages" name="lfric_averages"
         output_freq="12h" convention="UGRID" enabled=".FALSE.">

**Changing output frequency**

Edit the ``output_freq`` attribute. Accepted units are ``h`` (hours),
``min`` (minutes), and ``ts`` (model time steps):

.. code-block:: xml

   <!-- Write every 3 hours instead of 6 -->
   <file id="lfric_diag" name="lfric_diag"
         output_freq="3h" convention="UGRID" enabled=".TRUE.">

**Adding a field to an output file**

Look up the field ``id`` in the appropriate metadata file (e.g.
``metadata/lfric_dictionary.xml`` or ``metadata/field_def_diags.xml``) and add
a ``<field field_ref="..."/>`` line inside the ``<file>`` block:

.. code-block:: xml

   <file id="lfric_diag" name="lfric_diag"
         output_freq="6h" convention="UGRID" enabled=".TRUE.">
     <field field_ref="theta" />
     <field field_ref="exner" />   <!-- newly added -->
     ...
   </file>

**Removing a field**

Delete or comment out the corresponding ``<field field_ref="..."/>`` line.

Output format
-------------

LFRic output files follow the `CF conventions <https://cfconventions.org>`_
and use the `UGRID conventions <https://ugrid-conventions.github.io/ugrid-conventions/>`_
to describe fields on unstructured meshes. These files can be read with
Python libraries such as `Iris <https://scitools-iris.readthedocs.io>`_ and
`iris-esmf-regrid <https://iris-esmf-regrid.readthedocs.io>`_.

.. seealso::

   * `iodef.xml example`_ in the LFRic Apps repository.
   * `XIOS documentation`_ for the full XIOS XML reference.
   * The :ref:`iris.basics` tutorial for reading and plotting LFRic NetCDF output.
