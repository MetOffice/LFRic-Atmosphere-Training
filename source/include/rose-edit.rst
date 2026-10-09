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

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. include:: /include/isambard3-help.rst

      The Rose configuration editor (``rose edit``) is not installed on
      Isambard 3. Instead, open the ``rose-suite.conf`` and ``app/*/rose-app.conf``
      files in a text editor. They are plain INI-style files, and the setting
      names are the same as those shown in ``rose edit``. For example:

      .. code-block:: bash

         vim rose-suite.conf
         vim app/lfric_atm/rose-app.conf

      To look up a setting, search the files with ``grep``, for example
      ``grep -rn timestep_end app/``.

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
