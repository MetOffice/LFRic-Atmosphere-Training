.. Re-usable chunk on opening a suite in the Rose GUI.
.. To use it: .. include:: /include/rose-edit.rst

.. include:: /include/x11-forwarding.rst

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         rose edit &

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         rose edit &

      .. note::

         You must be on the Cylc host to run ``rose edit``. It is not
         available on the compute nodes. X11 forwarding must be enabled on
         every hop, including the lander and the Cylc host.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      .. code-block:: bash

         rose edit &

.. admonition:: What does the ``rose edit &`` command do?
   :collapsible: closed

   - This command opens the suite in the Rose graphical user
     interface, allowing you to view and modify its configuration.
   - The ``&`` at the end runs the GUI in the background, so
     your terminal remains available for other commands.
