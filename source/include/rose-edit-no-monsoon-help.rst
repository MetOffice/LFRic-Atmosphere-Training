.. reusable note on using rose edit without the Monsoon3 help link

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

         You must be using Cylc host to access ``rose-edit``.
         You will need to have used X11-forwarding (``ssh -X``) to
         access both the lander and Cylc host.


.. admonition:: What does the ``rose-edit &`` command do?
   :collapsible: closed

   - This command opens the suite in the Rose graphical user
     interface, allowing you to view and modify its configuration.
   - The ``&`` at the end runs the GUI in the background, so
     your terminal remains available for other commands.
