Getting Started: Copying a Workflow for the Regional Nesting Suite
===================================================================

To begin working with the regional nesting suite, you first need to create your
own copy of an existing workflow.

As introduced in the *Global Modelling Practical*, you can do this using the
``rosie`` command-line tool — see there for :ref:`the difference between
copying and checking out <rosie-copy-vs-checkout>`. As in that practical,
**copy** the workflow rather than checking it out. Monsoon3 uses a dedicated
branch of the workflow, so the source you copy differs by platform:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         rosie copy u-by395

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         rosie copy u-by395/u-by395_lfric_monsoon3

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: bash

         rosie copy u-by395

Alternatively, you can check out the workflow instead of copying it:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         rosie checkout u-by395

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: bash

         rosie checkout u-by395/u-by395_lfric_monsoon3

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. code-block:: bash

         rosie checkout u-by395

Either command reports the new suite ID it created, and the local copy it made
under ``~/roses``. Make a note of that ID: the rest of this practical refers to
it as ``<suite-id>``.
