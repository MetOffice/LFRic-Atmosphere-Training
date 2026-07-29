Copying an Existing Workflow
============================

To start, you will need to obtain a workflow. You can either copy an existing
workflow or create a new one. For this practical, a workflow has been provided
for you to copy. For a regional workflow example please use ``u-by395``, for a
global workflow example please use ``u-dz612``.

You can copy or check out an existing workflow using the ``rosie`` command-line
tool, replacing ``u-dz612`` with the actual suite ID.

.. _rosie-copy-vs-checkout:

.. admonition:: What's the difference between copying and checking out?

   **Copying a workflow**

   - Creates an independent version in your ``~/roses`` directory
   - Allows you to modify it freely without affecting the original
   - Recommended for the practicals in this course

   **Checking out a workflow**

   - Links to the original (shared) workflow
   - Typically used for collaborative or trunk development
   - Changes may affect or depend on the main version

   Both commands are described in the Rose command reference:
   :external+rose:ref:`rosie copy <command-rosie-create>` and
   :external+rose:ref:`rosie checkout <command-rosie-checkout>`.

For this practical, we recommend copying the workflow.

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         rosie copy u-dz612

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         rosie copy u-dz612

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: bash

         rosie copy u-dz612

After this, the following information will be displayed, this is the metadata
associated with the workflow you have just copied. To edit this information,
press ``a`` on your keyboard. Once you have finished, press the ``Esc`` key
followed by ``:wq`` to write and quit.

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/rosie-copy-metadata.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/snippets/rosie-copy-metadata.rst

   .. tab-item:: Other
      :sync: other

      .. include:: /include/snippets/rosie-copy-metadata.rst

You will then be asked in the terminal:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         $ rosie copy u-dz612
         Copy "u-dz612/trunk@123456" to "u-?????"? [y or n (default)]

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: console

         $ rosie copy u-dz612
         Copy "u-dz612/trunk@123456" to "u-?????"? [y or n (default)]

   .. tab-item:: Other
      :sync: other

      .. code-block:: console

         $ rosie copy u-dz612
         Copy "u-dz612/trunk@123456" to "u-?????"? [y or n (default)]

Press ``y`` to confirm you want to copy the workflow. You will then see the
following message confirming the workflow has been copied.

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/rosie-copy-confirm.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/snippets/rosie-copy-confirm.rst

   .. tab-item:: Other
      :sync: other

      .. include:: /include/snippets/rosie-copy-confirm.rst

Congratulations, you have successfully copied workflow ``u-dz612`` and made the
new suite ID ``u-?????``. Make a note of that new ID: the rest of this
practical refers to it as ``<suite-id>``. You can now navigate to the workflow
directory and start working on it.
