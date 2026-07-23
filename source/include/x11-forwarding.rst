.. admonition:: Running graphical applications over SSH
   :collapsible: closed

   If you are connected to a remote system over SSH, graphical applications
   need X11 forwarding to display on your computer. Start an X server on your
   computer first (for example, XQuartz on macOS), then connect from a terminal
   using generic host details supplied by your service:

   .. code-block:: bash

      ssh -AY <remote-host>

   Repeat the options for every additional SSH hop. The ``-Y`` option enables
   trusted X11 forwarding. The ``-A`` option forwards your SSH authentication
   agent and should only be used with systems you trust. A terminal integrated
   into an editor such as VS Code works in the same way as any other terminal.

   On the system where you will start the graphical application, run
   ``echo "$DISPLAY"``. It should return a value. If it is blank, disconnect
   and reconnect with X11 forwarding enabled at every hop before continuing.
