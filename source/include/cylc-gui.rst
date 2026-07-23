.. Re-usable chunk on how to monitor a workflow with the Cylc GUI or TUI.
.. To use it: .. include:: /include/cylc-gui.rst

.. include:: /include/x11-forwarding.rst

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. code-block:: bash

         cylc gui
         # or, if you prefer the terminal interface
         cylc tui

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. code-block:: bash

         cylc tui

      .. note::

         Use ``cylc tui`` on Monsoon3. ``cylc gui`` needs a browser or an X11
         connection that is not available from every Monsoon3 service.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform.rst

      .. code-block:: bash

         cylc gui
         # or, if a graphical interface is not available
         cylc tui

Both interfaces show nearly identical information, so the choice is largely
personal preference:

* ``cylc gui`` — easier to interact with, but needs a browser or an X11
  connection.
* ``cylc tui`` — lightweight and works in any terminal without X11.
