Editing a Workflow
==================

Now that you have successfully copied a workflow, you may want to make some
changes to it. This could be to change the model configuration, add additional
diagnostics, or change the length of the run.

Editing with Rose GUI
---------------------

To edit and view the workflow data, navigate into the ``roses/<suite-id>``
directory you just made and run the ``rose edit`` command:

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

            $ cd ~/roses/<suite-id> $ ls app  flow.cylc  meta  opt
            README_cylc8  rose-suite.conf  rose-suite.info  site  tests.cylc $
            rose edit

   .. tab-item:: Monsoon

      .. code-block:: console

            $ cd ~/roses/<suite-id> $ ls app  flow.cylc  meta  opt
            README_cylc8  rose-suite.conf  rose-suite.info  site  tests.cylc $
            rose edit

This will open up the Rose Graphical User Interface (GUI) for editing the
workflow. You can navigate through the different sections using the tabs at the
left of the window.

For example, navigate to the suite info tab where you should find the metadata
you entered when you copied the workflow. You can edit this information if you
wish - make sure you save your changes before exiting the GUI!

Unless you are familiar with the file structure of a workflow, it is
recommended to use the Rose GUI to make changes to the workflow. However, if
you are familiar with the file structure, you can also edit the files directly
using a text editor.

Change the run time
-------------------
To change the time settings, you need to first open the rose GUI. Next,
navigate to the suite conf > template variables tab. Here you will find the
runtime settings.

Let’s start by changing the run length of the model. The current setting is for
a 20 year and 6 month run P20Y6M. Note: the format is
P<years>Y<months>M<days>D. Change this so that the end date is 01-01-1990
00:00:00.

Change the resolution
---------------------
Next, let’s change the model resolution. Navigate to the suite conf > template
variables tab. Here you will find the resolution settings. What are the current
settings? Make sure you change the atmospheric horizontal resolution to C64 and
the ocean resolution to eORCA1. Save your changes and exit the Rose GUI.

Running the edited workflow
---------------------------
Now that you have made changes to the workflow, go to the next page to run your
workflow and see the changes you have made in action!
