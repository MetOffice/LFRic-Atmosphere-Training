Getting Started: Copying a Workflow for the Idealised Suite
===========================================================

To begin working with the idealised suite, you first need to create your own
copy of an existing workflow.

As introduced in the *Global Modelling Practical*, you can do this using the
``rosie`` command-line tool — see there for :ref:`the difference between
copying and checking out <rosie-copy-vs-checkout>`. As in the earlier
practicals, **copy** the workflow rather than checking it out:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/rosie-copy-idealised.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. important::

         These tutorials require you to be on a Cylc host.

      .. include:: /include/snippets/rosie-copy-idealised.rst

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. include:: /include/snippets/rosie-copy-idealised.rst

The command reports the new suite ID it created, and the local copy it made
under ``~/roses``. Make a note of that ID: the rest of this practical refers to
it as ``<suite-id>``.
