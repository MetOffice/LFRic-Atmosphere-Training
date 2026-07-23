.. Re-usable note on the OpenGL software renderer needed by 3D mesh views.
.. To use it: .. include:: /include/opengl-software-rendering.rst

.. important:: 3D views and the OpenGL software renderer

   The mesh tutorial opens interactive 3D views through GeoVista and PyVista.
   On a remote desktop or an HPC login node there is usually no graphics card,
   so rendering falls back to a software renderer that reports an OpenGL
   version older than these libraries require. Opening a 3D view then
   segfaults, often taking the notebook kernel with it.

   Set the following before starting JupyterLab:

   .. code-block:: console

      export MESA_GL_VERSION_OVERRIDE=3.3

   Add it to your shell profile if you use the 3D views regularly.
