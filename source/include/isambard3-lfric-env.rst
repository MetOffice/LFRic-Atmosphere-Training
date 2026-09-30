.. Re-usable chunk: load the LFRic build and workflow environment on Isambard 3.
.. The module version is pinned here only; bump it here when a new build of
.. https://github.com/ickc/lfric-env-isambard is published.
.. To use it: .. include:: /include/isambard3-lfric-env.rst

.. code-block:: bash

   module use "$LFRIC_TRAINING_PREFIX/modulefiles"
   module load lfric-env/v2026.09.28/cray
