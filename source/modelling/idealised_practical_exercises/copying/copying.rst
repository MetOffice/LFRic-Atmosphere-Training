Getting Started: Copying a Workflow for the Idealised Suite
===========================================================

To begin working with the idealised suite, you first need to create your own copy of an existing workflow.

As introduced in the *Global Modelling Practical* and repeated in the *Regional Modelling Practical*, you can do this using the ``rose`` command-line tool.
Replace ``<suite-id>`` with the ID of the workflow you want to use:

.. code-block:: bash

   rosie copy <suite-id>

Alternatively, you can check out the workflow instead of copying it:

.. code-block:: bash

   rosie checkout <suite-id>
   # or
   rosie co <suite-id>

Reminder: what's the difference between ``copy`` and ``checkout``?
------------------------------------------------------------------

**Copying a workflow**

- Creates an independent version in your ``~/roses`` directory
- Allows you to modify it freely without affecting the original
- Recommended for this practical

**Checking out a workflow**

- Links to the original (shared) workflow
- Typically used for collaborative or trunk development
- Changes may affect or depend on the main version

What should you do?
-------------------

For this hands-on exercise, go ahead and **copy the workflow**, just as you did in the previous practicals.
This will give you a clean, editable version to experiment with safely.

.. code-block:: bash

   rosie copy u-dz791