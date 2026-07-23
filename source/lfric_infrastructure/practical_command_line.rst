.. remove all trac refs

.. _example mesh file: https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications/lfric_atm/example
.. _lfric example: https://github.com/MetOffice/lfric_apps/blob/main/applications/lfric_atm/example
.. _iodef.xml example: https://github.com/MetOffice/lfric_apps/blob/main/applications/lfric_atm/example/iodef.xml

.. _practical_3.1:

Practical 1: Run the model from command line
--------------------------------------------

.. admonition:: Aims

   * Build and run the LFRic Atmosphere as a command line application.
   * Explore how model output is controlled via the ``iodef.xml`` configuration file.
   * Modify the output configuration to change what is written and how often.
   * Add custom messages to the model's standard output.

Step 1: Compile the model
+++++++++++++++++++++++++

.. _checkout_from_github:

1. Checkout the code from github:

   .. tab-set::

      .. tab-item:: Met Office
         :sync: met-office

         .. code-block:: console

            git clone git@github.com:MetOffice/lfric_apps.git
            cd lfric_apps

      .. tab-item:: Non Met Office

         Consult your site's documentation for cloning git repositories, then
         clone the LFRic apps repository:

         .. code-block:: console

            # either
            git clone git@github.com:MetOffice/lfric_apps.git
            # or
            git clone https://github.com/MetOffice/lfric_apps.git
            # then
            cd lfric_apps


2. Set up the build environment and select the compiler.

   .. tab-set::

      .. tab-item:: Met Office
         :sync: met-office

         .. code-block:: text

            ml use ~lfricadmin/lmod
            ml lfric

      .. tab-item:: Non Met Office

         For other platforms, see the `LFRic Development Environment`_.

3. Compile the model

   .. code-block:: console

      ./build/local_build.py lfric_atm

   The compilation may take some time and uses code from the different
   repositories, algorithms, and kernels. It invokes PSyclone, compiles,
   and links the code. The compiled model executable ``lfric_atm``
   will be in the folder ``applications/lfric_atm/bin/`` once the
   compilation finishes.

Step 2: Run the model
+++++++++++++++++++++

The code contains an `LFRic example`_ configuration containing:

* A "canned configuration" in ``namelist.nml``. This sets up a "single
  column" run of LFRic Atmosphere.
* The configuration uses the example mesh file ``mesh_BiP2x2-50000x50000.nc``.

.. note::

   ``mesh_BiP2x2-50000x50000.nc`` is not a single column mesh, but a
   2x2 biperiodic mesh. The configuration is designed in such a way
   that each column is computed independently from the other columns and
   gives identical results for each column.

1. Navigate to the example configuration directory:

   .. code-block:: console

      cd applications/lfric_atm/example


2. Run the example with a "single-column" configuration:

   .. code-block:: console

      ../bin/lfric_atm configuration.nml > log.txt

   The namelist file ``configuration.nml`` configures the model run.
   Note the we redirect the ``stdout`` to ``log.txt`` so we can look
   back at the output later.

3. Explore the outputs:

   As well as our ``log.txt`` file can you identify files containing:

   * Run time profiling?
   * Checksums of model fields after the last time step (for tests)?
   * NetCDF output files. How to open NetCDF files is covered in the
     :ref:`iris.basics` tutorial.

   Inspect the NetCDF header for the main diagnostic file:

   .. code-block:: console

      ncdump -h lfric_diag.nc | less

   .. tab-set::

      .. tab-item:: Met Office

         ``ncdump`` is part of the NetCDF tools available in the Met Office
         ``lfric`` environment.

      .. tab-item:: Non Met Office

         Install the NetCDF utilities using your site's supported package or
         module route, or use the :ref:`iris.basics` Python workflow instead.

4. Explore the NetCDF output configuration:

   The NetCDF output is controlled by both ``iodef.xml`` and the ``&io``
   namelist settings in ``configuration.nml`` (see the `iodef.xml example`_
   and :ref:`output-control`). Open both files and answer the following:

   * How many ``<file>`` definitions are configured in ``iodef.xml``, and
     what are their names?
   * Which file definitions are enabled, disabled, or opened in read mode?
   * Which diagnostic output files are selected by ``diag_active_files`` in
     ``configuration.nml``?
   * Roughly how many fields does ``lfric_diag`` write, and what are a few
     examples? How does its field list compare with ``lfric_averages``?
   * At what frequency is output written?

   .. hint::
      :collapsible: closed

      Look for ``<file>`` elements — each defines one XIOS file. The ``name``
      attribute gives the output filename. ``<field>`` elements nested inside
      each ``<file>`` block list the model fields written to that file. The
      ``output_freq`` attribute on ``<file>`` sets how often output is
      written. The ``enabled`` and ``mode`` attributes describe the XML file
      definition, while namelist settings such as ``diag_active_files`` and
      ``write_initial`` control which definitions are used by this run.

Step 3: Modify the Model
++++++++++++++++++++++++

To gain familiarity with the model:

1. Add your own print statement at the end of each time step (and a different
   print statement after time step 72).

   .. hint::
      :collapsible: closed

      Search the code for the log messages available in ``log.txt``
      (e.g. with ``grep -R "End of timestep" *``) to find where to
      change the code and write such an output.

   .. important::

      Note that you must edit
      ``science/gungho/source/driver/gungho_step_mod.x90``
      **not** in
      ``applications/lfric_atm/working/build_lfric_atm/driver/gungho_step_mod.f90``.

      **Why**

      Files with the ``.x90`` extension are the PSyclone source files that
      developers are expected to modify. During the build, PSyclone
      reads these ``.x90`` files and automatically generates the
      corresponding ``.f90`` files in the ``working/build_*`` directory, which
      are then compiled. The ``working/build_*`` directory
      contains temporary build artefacts that are regenerated every
      time the model is rebuilt. Any changes made directly to the
      autogenerated ``.f90`` files will be silently overwritten on the
      next build and should never be relied upon.

2. Adjust the code, re-compile, and re-run the model.

   You will see your new message in the output.

   .. hint::

      You can write to standard output by adding the following
      Fortran code at the end of the subroutine ``gungho_step`` in
      ``science/gungho/source/driver/gungho_step_mod.x90``:

   .. _practical_3.1.hint.code:

   .. hint:: Fortran code to write info message
      :collapsible: closed

      .. code-block:: fortran

         write( log_scratch_space, '(A)' ) "###_INFO_#1 END OF TIME STEP"
         call log_event( log_scratch_space, LOG_LEVEL_INFO )

         if (model_clock%get_step() .lt. 72) then
            write( log_scratch_space, '(A)' ) "###_INFO_#2 THE WEATHER IS FINE"
         else
            write( log_scratch_space, '(A)' ) "###_INFO_#2 ENJOY THE MODEL TUTORIAL"
         endif
         call log_event( log_scratch_space, LOG_LEVEL_INFO )

.. note:: Version Control.

   Changes like the one you've implemented here should be tracked using
   version control. This ensures traceability and supports collaborative
   development. You'll learn how to document and manage your code changes
   using tickets and branches in Practical 3.

Step 4: Modify the Output
+++++++++++++++++++++++++

Unlike the model source code, the output configuration does not require a
recompile. You can change what is written and how often by editing
``configuration.nml`` and ``iodef.xml``, then re-running the model.

If you are not still in the example directory after recompiling, return to it
first:

.. code-block:: console

   cd applications/lfric_atm/example

1. Open ``configuration.nml`` and add the
   ``lfric_averages`` file to ``diag_active_files``:

   .. code-block:: fortran

      diag_active_files='lfric_diag','lfric_averages',

2. Re-run the model to create a baseline ``lfric_averages.nc`` file at the
   default 12-hour output frequency:

   .. code-block:: console

      rm -f lfric_averages.nc
      ../bin/lfric_atm configuration.nml > log_averages_12h.txt

3. Inspect the file and note the time dimension and variable names:

   .. code-block:: console

      ncdump -h lfric_averages.nc | less

4. Keep the baseline file so that you can compare it with the next run:

   .. code-block:: console

      mv lfric_averages.nc lfric_averages_12h.nc

5. Open ``iodef.xml`` and find the
   ``lfric_averages`` file definition.

6. Change its ``output_freq`` from ``12h`` to ``6h`` so that averaged fields
   are written at the same frequency as the diagnostics.

7. Add the ``rho`` field to the ``lfric_averages`` file with a time average
   operation:

   .. hint::
      :collapsible: closed

      Inside the ``lfric_averages`` ``<file>`` block, add:

      .. code-block:: xml

         <field field_ref="rho" operation="average" />

8. Re-run the model (no recompile needed):

   .. code-block:: console

      ../bin/lfric_atm configuration.nml > log_averages_6h.txt

9. Compare the headers from the old and new averages files:

   .. code-block:: console

      ncdump -h lfric_averages_12h.nc | grep -E "time =|rho"
      ncdump -h lfric_averages.nc | grep -E "time =|rho"

   Check that the new ``lfric_averages.nc`` file contains a ``rho`` variable
   and has more time records than the 12-hour baseline file. With the default
   24-hour run, the 12-hour baseline should hold 2 time records and the 6-hour
   file 4.

.. seealso::

   :ref:`output-control` explains the full ``iodef.xml`` structure, including
   how to enable checkpoint files and how to reference fields from the LFRic
   metadata catalogues.
