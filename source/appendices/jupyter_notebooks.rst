.. _using-jupyter-notebooks:

************************
Using Jupyter notebooks
************************

Some practical exercises in this course are delivered as Jupyter notebooks.
This page is for learners who are new to Python, JupyterLab, or ``.ipynb``
notebook files.

What you are starting
---------------------

JupyterLab is a browser-based workspace for writing notes, running code, and
viewing results. A notebook is a document made from cells:

* Markdown cells contain text, equations, links, and instructions.
* Code cells contain Python commands that can be run interactively.
* A kernel is the Python process that runs the code cells.
* A Python environment contains the packages available to the kernel.

For the mesh tutorial practical, the important rule is to use the kernel that
matches the environment from the setup steps: the default Python 3 kernel if
you loaded ``scitools`` at the Met Office or on Monsoon3, or the
``Python (lfric-mesh)`` kernel if you built a conda environment on your own
machine.

.. _fig-appendix-jupyterlab-interface:

.. figure:: /_static/jupyterlab/JupyterLab_Workspace.png
   :width: 100%
   :alt: JupyterLab interface showing the menu bar, file browser, notebook area,
      text editor, launcher, and image viewer panels.

   JupyterLab workspace showing the menu bar, file browser, notebook area, and
   open panels.

Before launching JupyterLab
---------------------------

Before starting a notebook, make sure you have:

1. A local copy of the training repository.
2. A Python environment with the notebook dependencies available.
3. A Jupyter kernel for that environment.

For the mesh tutorial, the setup commands are given in
:doc:`the practical using unstructured data
<../mesh_overview/exercises/practical_exercises>`. Complete those setup steps
once before launching JupyterLab.

Launching the mesh tutorial notebooks
-------------------------------------

Open a terminal and move to the root of the training repository. If your
repository is somewhere else, replace the path in the first command with your
local path:

.. code-block:: bash

   cd /path/to/LFRic-Atmosphere-Training

Make the tutorial environment available:

.. include:: /include/iris.rst

Move into the notebook directory:

.. code-block:: bash

   cd notebooks/iris-mesh-tutorial/notebooks

Start JupyterLab:

.. code-block:: bash

   jupyter lab

JupyterLab normally opens in a browser tab automatically. If it does not, copy
the local URL printed in the terminal into your browser. It will usually start
with ``http://localhost:`` and may include a ``token=`` value. Treat that URL as
private while the notebook server is running.

.. important::
   Start JupyterLab from ``notebooks/iris-mesh-tutorial/notebooks`` when working
   through the mesh tutorial. Several notebooks use paths relative to this
   directory.

Opening and running a notebook
------------------------------

1. In the JupyterLab file browser, open the first tutorial notebook:
   ``00_Mesh_Tutorial_Intro.ipynb``.
2. If JupyterLab asks you to select a kernel, choose the one for your
   environment: the default Python 3 kernel under ``scitools``, or
   ``Python (lfric-mesh)`` for a conda environment.
3. If the notebook has already opened with a different kernel, use
   ``Kernel -> Change Kernel`` to switch.
4. Read each Markdown cell, then run the next code cell.
5. To run a cell, click in it and press ``Shift`` + ``Enter``. You can also use
   the run button in the notebook toolbar.
6. Wait for a cell to finish before running the next one. A cell marked ``[*]``
   is still running. A finished code cell is given a number such as ``[3]``.
7. Save your work with ``File -> Save Notebook`` or ``Ctrl`` + ``S``.

Run notebooks from top to bottom unless the instructions say otherwise. Code
cells can depend on variables created by earlier cells, so running cells out of
order can produce confusing errors.

.. _fig-appendix-jupyterlab-notebook-ui:

.. figure:: /_static/jupyterlab/notebook-ui.png
   :width: 100%
   :alt: JupyterLab notebook showing Markdown text, code cells, outputs, the
      notebook toolbar, kernel status, and the file browser.

   Notebook view showing Markdown text, code cells, outputs, the toolbar, the
   selected kernel, and the notebook status bar.

Restarting and stopping
-----------------------

Use these actions when a notebook gets into an unexpected state:

* ``Kernel -> Interrupt Kernel`` stops the currently running cell.
* ``Kernel -> Restart Kernel`` clears Python variables and starts the kernel
  again.
* ``Run -> Run All Cells`` reruns the notebook from the top after a restart.
* ``Kernel -> Shut Down Kernel`` stops the Python process for the active
  notebook.

When you have finished:

1. Save any notebooks you changed.
2. Shut down any running kernels you no longer need.
3. Return to the terminal where ``jupyter lab`` is running.
4. Press ``Ctrl`` + ``C`` to stop the JupyterLab server.
5. Close the browser tab.

Closing the browser tab alone does not necessarily stop the server or the
notebook kernels.

Common problems
---------------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Symptom
     - What to try
   * - ``jupyter: command not found`` or ``jupyter lab`` is not recognised.
     - Make the environment available first, with ``module load scitools`` or
       ``conda activate lfric-mesh``. If it still fails, return to the setup
       commands in :doc:`the practical using unstructured data
       <../mesh_overview/exercises/practical_exercises>`.
   * - The ``Python (lfric-mesh)`` kernel is missing.
     - Activate the environment and rerun the kernel registration command from
       :doc:`the practical using unstructured data
       <../mesh_overview/exercises/practical_exercises>`: ``python -m
       ipykernel install --user --name lfric-mesh --display-name "Python
       (lfric-mesh)"``. This applies to the conda route only.
   * - A notebook opens, but ``import`` statements fail.
     - Check that the selected kernel matches the environment you set up.
       Package import errors often mean the notebook is using a different
       Python environment.
   * - Opening a 3D view crashes the kernel.
     - See the OpenGL note in :doc:`the practical using unstructured data
       <../mesh_overview/exercises/practical_exercises>`. Set
       ``MESA_GL_VERSION_OVERRIDE=3.3`` before starting JupyterLab.
   * - A notebook cannot find data files or support modules.
     - Stop JupyterLab and restart it from
       ``notebooks/iris-mesh-tutorial/notebooks``.
   * - A cell is stuck on ``[*]``.
     - Wait a little longer for expensive cells. If it is clearly stuck, use
       ``Kernel -> Interrupt Kernel``. If the notebook is then inconsistent, use
       ``Kernel -> Restart Kernel`` followed by ``Run -> Run All Cells``.
   * - The browser says it cannot connect to the notebook.
     - Check that the terminal running ``jupyter lab`` is still open. If the
       server stopped, start it again and use the new local URL.
