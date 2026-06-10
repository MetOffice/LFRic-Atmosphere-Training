.. _iodef.xml example: https://github.com/MetOffice/lfric_apps/blob/main/applications/lfric_atm/example/iodef.xml
.. _XIOS documentation: https://ipsl.pages.in2p3.fr/projets/xios-projects/xios/

.. _output-control:

Output Control
==============

LFRic Atmosphere uses `XIOS <https://gitlab.in2p3.fr/ipsl/projets/xios-projects/xios>`_ (XML
I/O Server) to manage model output. XIOS runs as a separate I/O server process
alongside the model and writes NetCDF files asynchronously, so that I/O does
not stall the model computation.

Output control is split between an XML file called ``iodef.xml`` and the
runtime namelist. The XML file describes the XIOS files, fields, frequencies,
and grid conventions. The namelist controls which categories of output are
active in a particular run. You do not need to recompile the model to change
these settings.

The ``iodef.xml`` file
----------------------

The `iodef.xml example`_ file in the LFRic Apps repository shows the structure
used by the LFRic Atmosphere example configuration.

.. note::

   The file names, fields, and frequencies described on this page reflect the
   example configuration on the ``main`` branch at the time of writing. The
   linked `iodef.xml example`_ is always authoritative — check it if the
   details have moved on.

A trimmed outline looks like this:

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
* **Grid conventions** — the ``convention`` attribute selects the output
  convention for the file, while field metadata such as ``grid_ref`` describes
  how fields sit on the mesh.

The namelist then selects which of these definitions are used by the canned
configuration. For example, the default ``configuration.nml`` selects only the
main diagnostic output stream:

.. code-block:: fortran

   &io
   diag_active_files='lfric_diag',
   write_diag=.true.,
   write_initial=.false.
   /

Output files
------------

The example ``iodef.xml`` contains these file definitions:

.. list-table::
   :header-rows: 1

   * - File definition
     - Purpose
     - Frequency
     - Default run status
   * - ``lfric_diag``
     - Instantaneous atmospheric diagnostics.
     - 6 hours
     - Written by default because ``diag_active_files`` selects it.
   * - ``lfric_averages``
     - Time-averaged diagnostics.
     - 12 hours
     - Defined and enabled in XML, but not selected by the default
       ``diag_active_files`` namelist entry.
   * - ``lfric_initial``
     - Initial-condition diagnostics.
     - Once, on the first time step
     - Defined and enabled in XML, but not written in the default run (which
       sets ``write_initial=.false.``).
   * - ``lfric_checkpoint_write``
     - Checkpoint output.
     - 1 time step
     - Disabled by default.
   * - ``lfric_checkpoint_read``
     - Checkpoint input.
     - 1 time step
     - Disabled by default and opened in read mode.
   * - ``lfric_fd_dump``
     - Full dump output.
     - 1 time step
     - Disabled by default.
   * - ``read_lfric_fd_dump``
     - Full dump input.
     - 1 time step
     - Disabled by default and opened in read mode.

The main diagnostic outputs use the UGRID convention:

.. list-table::
   :header-rows: 1

   * - File definition
     - Example content
   * - ``lfric_diag``
     - Atmospheric diagnostics (temperature, moisture, winds, radiation,
       surface fields, and more)
   * - ``lfric_averages``
     - Time-averaged fields (potential temperature, Exner pressure, wind
       components)
   * - ``lfric_initial``
     - Initial-condition fields written once at the start of the run

Controlling output
------------------

**Enabling or disabling a file**

Set ``enabled=".TRUE."`` or ``enabled=".FALSE."`` on a ``<file>`` element.
For diagnostic files, also select the file in ``configuration.nml``:

.. code-block:: xml

   <file id="lfric_averages" name="lfric_averages"
         output_freq="12h" convention="UGRID" enabled=".TRUE.">

.. code-block:: fortran

   diag_active_files='lfric_diag','lfric_averages',

**Changing output frequency**

Edit the ``output_freq`` attribute. Accepted units include ``ts`` (model time
steps), ``h`` (hours), ``d`` (days), and ``mi`` (minutes):

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

The field must be one the model actually computes and sends to XIOS — in
practice, one already produced by the active diagnostic system. You cannot
write a field that the model does not provide, even if it is defined in the
metadata.

**Removing a field**

Delete or comment out the corresponding ``<field field_ref="..."/>`` line.

Output format
-------------

LFRic NetCDF output follows the `CF conventions <https://cfconventions.org>`_.
The atmospheric diagnostic files also use the `UGRID conventions
<https://ugrid-conventions.github.io/ugrid-conventions/>`_ to describe fields
on unstructured meshes. These files can be read with Python libraries such as
`Iris <https://scitools-iris.readthedocs.io>`_ and `iris-esmf-regrid
<https://iris-esmf-regrid.readthedocs.io>`_.

.. seealso::

   * `iodef.xml example`_ in the LFRic Apps repository.
   * `XIOS documentation`_ for the full XIOS XML reference.
   * The :ref:`iris.basics` tutorial for reading and plotting LFRic NetCDF output.
