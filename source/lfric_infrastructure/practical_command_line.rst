
Practical 1: Run model from command line
----------------------------------------

Before showing how to run the model as part of Cylc workflows this practical introduces the LFRic Atmosphere as a command line application. It shows how the model can be built and run from the command line, and how one can add a message to the standard output of the model.

Use `fcm <https://metomi.github.io/fcm/doc/user_guide/annex_quick_ref.html>`_ to checkout the code:

.. code-block:: text
   :linenos:
       
   mkdir practical_command_line ; cd  practical_command_line
   fcm co fcm:lfric_apps.x-tr lfric_apps
   
The model build requires you to have the needed environment modules available. Assuming you want to run this practical on the Met Office Azure Spice platform, you can load the module and set the compiler with:

.. code-block:: bash
   :linenos:
      
   ml use ~lfricadmin/lmod
   ml lfric

See the documentation for the `LFRic Development Enviroment <https://code.metoffice.gov.uk/trac/lfric/wiki/DevelopmentEnvironment>`_ for how to activate the environment for other platforms. Now compile the model with:

.. code-block:: text
   :linenos:
   :emphasize-lines: 2
   
   cd lfric_apps
   ./build/local_build.py -a lfric_atm

The code contains an example configuration, colloquially called "canned configuration", in  the namelist file `applications/lfric_atm/example/configuration.nml <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications/lfric_atm/example/configuration.nml>`_. This configuration sets up a "single column" run of LFRic Atmosphere. It is configured to use the mesh file in the `example <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/applications/lfric_atm/example>`_ directory which is, in reality, not a single column mesh, but a 2x2 biperiodic mesh. However, the configuration is designed in such a way as each column is computed independently from the other columns and, in fact, gives identical results for each column.

Change to that folder and run the example:

.. code-block:: text
   :linenos:
   :emphasize-lines: 2
   
   cd applications/lfric_atm/example      
   ../bin/lfric_atm configuration.nml

The namelist file ``configuration.nml`` controls how the model is run. Redirect the standard output to a text file to examine later:

.. code-block:: bash
   :linenos:
      
   ../bin/lfric_atm configuration.nml > log.txt

Explore the file ``log.txt`` and the other output files.

**Add debug output to model log**

To gain first familiarity with the model try to add your own print statement at the end of each time step (and a different print statement after time step 72). Search the code for the log messages available in ``log.txt`` (e.g. with ``grep -R "End of timestep" *``) to find where to change the code and write such an output. Adjust the code, re-compile, and re-run the model.

**Hint:** You can write to standard out by adding the following Fortran code

.. code-block:: fortran
   :linenos:

    write( log_scratch_space, '(A)' ) "###_DEBUG_#1 END OF TIME STEP" 
    if (model_clock%get_step() .lt. 72) then
       write( log_scratch_space, '(A)' ) "###_DEBUG_#2 THE WEATHER IS FINE 20 DEG C"
    else
       write( log_scratch_space, '(A)' ) "###_DEBUG_#2 THE WEATHER IS GREAT 22 DEG C"
       write( log_scratch_space, '(A)' ) "###_DEBUG_#2 ENJOY THE MODEL TUTORIAL" 
    endif
    call log_event( log_scratch_space, LOG_LEVEL_INFO )

at the end of the subroutine gungho_step in the file `gungho_step_mod.x90 <https://code.metoffice.gov.uk/trac/lfric_apps/browser/main/trunk/science/gungho/source/driver/gungho_step_mod.x90?rev=9055#L217>`_  in the folder ``science/gungho/source/driver``.
