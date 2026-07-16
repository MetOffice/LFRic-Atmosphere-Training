Getting Started: Copying a Workflow for the Idealised Suite
===========================================================

To begin working with the idealised suite, you first need to create your own copy of an existing workflow.

As introduced in the *Global Modelling Practical* and repeated in the *Regional Modelling Practical*, you can do this using the ``rose`` command-line tool.
Replace ``<suite-id>`` with the ID of the workflow you want to use:

.. tab-set::

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         rosie copy u-dz791

         # Alternatively, you can check out the workflow
         # instead of copying it:
         rosie checkout u-dz791
         # or
         rosie co u-dz791

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. important::

         These tutorials require you to be on a Cylc host.

      .. code-block:: bash

         rosie copy u-dz791

         # Alternatively, you can check out the workflow
         # instead of copying it:
         rosie checkout u-dz791
         # or
         rosie co u-dz791


.. note:: Reminder: what's the difference between ``copy`` and ``checkout``?

   :Copying a workflow:
      - Creates an independent version in your ``~/roses`` directory
      - Allows you to modify it freely without affecting the original
      - Recommended for this practical

   :Checking out a workflow:
      - Links to the original (shared) workflow
      - Typically used for collaborative or trunk development
      - Changes may affect or depend on the main version
