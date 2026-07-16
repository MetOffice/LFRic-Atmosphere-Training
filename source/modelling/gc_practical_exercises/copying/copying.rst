Copying an Existing Workflow
============================

To start, you will need to obtain a workflow. You can either copy an existing
workflow or create a new one. For this practical, a workflow has been provided
for you to copy. For a regional workflow example please use ``u-by395``, for a
global workflow example please use ``u-dz612``.

You can copy or checkout an existing workflow using the rose command-line tool,
replacing ``u-dz612`` with the actual suite ID. Remember that copying a
workflow will create a new instance of the workflow in your ``~/roses``
directory, while checking out will link to the original workflow allowing for
trunk development. For this practical, we recommend copying the workflow.


.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

            $ mkdir ~/roses $ cd ~/roses $ rosie copy u-dz612

   .. tab-item:: Monsoon

      .. code-block:: console

            $ mkdir ~/roses $ cd ~/roses $ rosie copy u-dz612

After this, the following information will be displayed, this is the metadata
associated with the workflow you have just copied. To edit this information,
press ``a`` on your keyboard. Once you have finished, press the ``Esc`` key
followed by ``:wq`` to write and quit.

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

            description=  < This is where you can write information about the
            workflow  e.g. Copy of u-ab122/trunk@123456 > owner=  < Your
            username will appear here  > project=  < The associated project
            title e.g. GC6-climate-amip > title= < The title of the workflow
            should be put here e.g. Global AtmosOnly Climate Workflow > # Make
            changes ABOVE these lines. # The "owner", "project" and "title"
            fields are compulsory. # Any KEY=VALUE pairs can be added. Known
            fields include: # "access-list", "description" and "sub-project".

   .. tab-item:: Monsoon

      .. code-block:: console

            description=  < This is where you can write information about the
            workflow  e.g. Copy of u-ab122/trunk@123456 > owner=  < Your
            username will appear here  > project=  < The associated project
            title e.g. GC6-climate-amip > title= < The title of the workflow
            should be put here e.g. Global AtmosOnly Climate Workflow > # Make
            changes ABOVE these lines. # The "owner", "project" and "title"
            fields are compulsory. # Any KEY=VALUE pairs can be added. Known
            fields include: # "access-list", "description" and "sub-project".

You will then be asked in the terminal:

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

            $ rosie copy u-dz612 Copy "u-dz612/trunk@123456" to "u-?????"? [y
            or n (default)]

   .. tab-item:: Monsoon

      .. code-block:: console

            $ rosie copy u-dz612 Copy "u-dz612/trunk@123456" to "u-?????"? [y
            or n (default)]

Press ``y`` to confirm you want to copy the workflow. You will then see the
following message confirming the workflow has been copied.

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

            [INFO] u-?????: created at
            https://code.metoffice.gov.uk/svn/roses-u/?/?/?/?/? [INFO] u-?????:
            copied items from u-dz612/trunk@123456 [INFO] u-?????: local copy
            created at ~/roses/u-?????

   .. tab-item:: Monsoon

      .. code-block:: console

            [INFO] u-?????: created at
            https://code.metoffice.gov.uk/svn/roses-u/?/?/?/?/? [INFO] u-?????:
            copied items from u-dz612/trunk@123456 [INFO] u-?????: local copy
            created at ~/roses/u-?????

Congratulations, you have successfully copied workflow ``u-dz612`` and made the
new suite-id ``u-????``! You can now navigate to the workflow directory and
start working on it.
