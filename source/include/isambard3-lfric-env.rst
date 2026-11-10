.. Re-usable chunk: load the LFRic environment on Isambard 3.
.. LFRIC_TRAINING_PREFIX is set as described in the Isambard 3 appendix.
.. The module version is pinned here only; bump it here when a new build of
.. https://github.com/ickc/lfric-env-isambard is published.
.. To use it: .. include:: /include/isambard3-lfric-env.rst

.. code-block:: bash

   module use "$LFRIC_TRAINING_PREFIX/modulefiles"
   module load lfric-env/v2026.10.08/cray
