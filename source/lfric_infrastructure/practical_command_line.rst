
Practical 0: Run model from command line
----------------------------------------

This practical introduces the LFRic Atmosphere as a command line application to show how the model can be build and run without the Cylc workflows.

The build requires you to have the needed compiler dependencies in place...  

Assuming you want to run the exercise on the Met Office Azure Spice platform, ...:

.. code-block:: bash
   :linenos:
   
   fcm co fcm:lfric_apps.x-tr lfric_apps_new_trunk
   cd lfric_apps_new_trunk
   ml use ~lfricadmin/lmod
   ml lfric
   ./build/local_build.py -a lfric_atm

This compiles the code,... 
      
The code contains an example configuration, colloquially called "canned" configuration, in  the folder `applications/lfric_atm/example <https://code.metoffice.gov.uk/trac/lfric_apps/log//main/trunk/applications/lfric_atm/example>`_. Change to that folder and run the example:

.. code-block:: bash
   :linenos:
   
   cd applications/lfric_atm/example      
   ../bin/lfric_atm configuration.nml

The namelist file configuration.nml controls how the model is run. Redirect the standard output to a text file to examine later:

.. code-block:: bash
   :linenos:
      
   ../bin/lfric_atm configuration.nml > log.txt

Explore the the log and the other output files.

**Add debug output**

To gain more familarity with the model try to add your own print statement into the model, print out the value of XXX, does it change when you modify YYY in configuration.nml?

**Hint:** ...
