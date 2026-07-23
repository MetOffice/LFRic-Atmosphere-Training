.. Re-usable chunk on loading the LFRic build and workflow module stack.
.. To use it: .. include:: /include/lfric-modules.rst

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         module use ~lfricadmin/lmod
         module load lfric

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         module use /home/users/lfricadmin.mon/lmod
         module load lfric

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      Follow your site's `LFRic Development Environment`_ documentation to
      provide an equivalent environment. The exact compiler and library
      versions are platform-specific and are owned by the supported LFRic
      build environment and the repository dependency files, not by this
      training course.

.. note::

   ``ml`` is a shorthand for ``module``, so ``ml lfric`` and
   ``module load lfric`` are equivalent.

The module stack selects the compiler, MPI implementation, Python tools,
PSyclone, and supporting scientific libraries used by the practicals.
