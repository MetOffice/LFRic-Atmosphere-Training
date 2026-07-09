.. reusable note on using iris
.. to use use .. include:: /include/cylc-gui.rst

.. tab-set::

   .. tab-item:: Met Office
      :sync: metoffice

      .. code-block:: bash

         module load scitools

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: bash

         module load scitools

   .. tab-item:: Other
      :sync: other

      Use your preferred environment manager to create an environment
      and install these tools from PyPi. A typical workflow might include:

      .. code-block:: bash

         conda create -n my_env python pip
         pip install iris dask numpy matplotlib

      .. seealso::

         - [Iris Documentation](
            https://scitools-iris.readthedocs.io/en/stable/)
