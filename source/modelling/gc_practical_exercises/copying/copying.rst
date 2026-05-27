Copying an Existing Workflow
============================

To start, you will need to obtain a workflow. You can either copy an existing workflow or create a new one.
For this practical, a workflow has been provided for you to copy. For a regional workflow example please use
``<suite-id>``, for a global workflow example please use ``<suite-id>``.

You can copy or checkout an existing workflow using the rose command-line tool, replacing ``<suite-id>`` with
the actual suite ID. Remember that copying a workflow will create a new instance of the workflow in your
``~/roses`` directory, while checking out will link to the original workflow allowing for trunk development.
For this practical, we recommend copying the workflow.

.. code-block:: bash

   mkdir ~/roses
   cd ~/roses
   rosie copy <suite-id>

After this, the following information will be displayed, this is the metadata associated with the workflow
you have just copied. To edit this information, press ``a`` on your keyboard. Once you have finished, press
the ``Esc`` key followed by ``:wq`` to write and quit.

.. code-block:: none
   description=  < This is where you can write information about the workflow  e.g. Copy of u-ab122/trunk@123456 >
   owner=  < Your username will appear here  >
   project=  < The associated project title e.g. GC6-climate-amip >
   title= < The title of the workflow should be put here e.g. Global AtmosOnly Climate Workflow >
   # Make changes ABOVE these lines.
   # The "owner", "project" and "title" fields are compulsory.
   # Any KEY=VALUE pairs can be added. Known fields include:
   # "access-list", "description" and "sub-project".

You will then be asked in the terminal:

.. code-block:: bash

   rosie copy <suite-id>
   Copy "u-ab122/trunk@123456" to "u-?????"? [y or n (default)]

Press ``y`` to confirm you want to copy the workflow. You will then see the following message confirming the
workflow has been copied.

.. code-block:: none

   [INFO] u-ab123: created at https://code.metoffice.gov.uk/svn/roses-u/a/b/1/2/3
   [INFO] u-ab123: copied items from u-ab122/trunk@123456
   [INFO] u-ab123: local copy created at ~/roses/u-ab123

Congratulations, you have successfully copied workflow ``u-ab122`` and made the new suite-id ``u-ab123``!

.. note::

   **Fun fact!**

   The suite-id is made up of a ``u-`` followed by two letters and three numbers - this is known as an
   alphanumeric identifier. The suite-id increases using alphanumeric ordering, so after ``u-aa999`` comes
   ``u-ab000`` and so on. This allows for a large number of workflows to be created without running out of
   suite-ids. The 5 character identifier allows for 26 x 26 x 999 = 675,324 unique suite-ids, whereas just
   numbers would only allow for 99,999 unique suite-ids.

