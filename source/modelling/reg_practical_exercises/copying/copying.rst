Getting Started: Copying a Workflow for the Regional Nesting Suite
===================================================================

To begin working with the regional nesting suite, you first need to create your own copy of an existing workflow.

As introduced in the *Global Modelling Practical*, you can do this using the ``rosie`` command-line tool:

.. tab-set::

    .. tab-item:: Met Office

        .. code-block:: bash

            rosie copy u-by395

    .. tab-item:: Monsoon

      .. code-block:: bash

            rosie copy u-by395/u-by395_lfric_monsoon3

Alternatively, you can check out the workflow instead of copying it:

.. tab-set::

    .. tab-item:: Met Office

        .. code-block:: bash

            rosie checkout u-by395

    .. tab-item:: Monsoon

      .. code-block:: bash

            rosie copy u-by395/u-by395_lfric_monsoon3

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

For this hands-on exercise, go ahead and **copy the workflow**, just as you did in the global modelling practical.
This will give you a clean, editable version to experiment with safely.

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: bash

            rosie copy u-by395

   .. tab-item:: Monsoon

      .. code-block:: bash

            rosie copy u-by395/u-by395_lfric_monsoon3
