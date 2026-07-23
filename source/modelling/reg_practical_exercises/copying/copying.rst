Getting Started: Copying a Workflow for the Regional Nesting Suite
===================================================================

To begin working with the regional nesting suite, you first need to create your
own copy of an existing workflow.

As introduced in the *Global Modelling Practical*, you can do this using the
``rosie`` command-line tool. Monsoon3 uses a dedicated branch of the workflow,
so the source you copy differs by platform:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         rosie copy u-by395

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: console

         rosie copy u-by395/u-by395_lfric_monsoon3

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: console

         rosie copy u-by395

Alternatively, you can check out the workflow instead of copying it:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         rosie checkout u-by395

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: console

         rosie checkout u-by395/u-by395_lfric_monsoon3

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: console

         rosie checkout u-by395

Either command reports the new suite ID it created, and the local copy it made
under ``~/roses``. Make a note of that ID: the rest of this practical refers to
it as ``<suite-id>``.

What's the difference?
-----------------------

**Copying a workflow**

- Creates an independent version in your ``~/roses`` directory
- Allows you to modify it freely without affecting the original
- Recommended for this practical

**Checking out a workflow**

- Links to the original (shared) workflow
- Typically used for collaborative or trunk development
- Changes may affect or depend on the main version

What should you do?
--------------------

For this hands-on exercise, go ahead and **copy the workflow**, just as you did
in the global modelling practical. This will give you a clean, editable version
to experiment with safely.
