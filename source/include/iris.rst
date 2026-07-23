.. Re-usable chunk on making Iris and the scientific Python stack available.
.. To use it: .. include:: /include/iris.rst

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: console

         module load scitools

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: console

         module load scitools

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      Use your preferred environment manager to create an environment and
      install these tools. A typical workflow might be:

      .. code-block:: console

         conda create -n my_env python
         conda activate my_env
         conda install -c conda-forge iris dask numpy matplotlib

.. seealso::

   `Iris documentation <https://scitools-iris.readthedocs.io/en/stable/>`_
