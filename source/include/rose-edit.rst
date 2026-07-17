.. reusable note on using rose edit
.. to use use .. include:: /include/cylc-gui.rst

.. include:: /include/x11-forwarding.rst

.. tab-set::

   .. tab-item:: Met Office
      :sync: metoffice

      .. code-block:: bash

         rose edit &

   .. tab-item:: Monsoon
      :sync: monsoon

      .. code-block:: bash

         rose edit &

      .. note::

         You must be using the Cylc host to access ``rose-edit``.


.. admonition:: What does the ``rose-edit &`` command do?
   :collapsible: closed

   - This command opens the suite in the Rose graphical user
     interface, allowing you to view and modify its configuration.
   - The ``&`` at the end runs the GUI in the background, so
     your terminal remains available for other commands.
