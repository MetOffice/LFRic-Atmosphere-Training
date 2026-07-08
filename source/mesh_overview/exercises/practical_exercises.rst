.. _mesh-practical-exercises:

*********************************
Practical using unstructured data
*********************************

The Mesh Tutorial provides practical training on handling LFRic unstructured mesh data.

All tutorial content is delivered through interactive Jupyter notebooks.
The upstream material comes from `iris-mesh-tutorial <https://github.com/scitools-classroom/iris-mesh-tutorial>`_ and is provided in this repository under:

.. code-block:: text

   notebooks/iris-mesh-tutorial/

New to these tools?
-------------------
This practical is about working with LFRic unstructured mesh data. It uses
Git, the command line, Conda, Python, and JupyterLab. If you are new to Python
or have not used notebooks before, read :ref:`using-jupyter-notebooks` before
starting the setup below. If the Git, terminal, or environment setup commands
are unfamiliar, use the resources in this section as optional preparation or as
reference material while you work through the notebooks.

The most important ideas for this practical are:

* A Git repository is a version-controlled project. Cloning a repository creates
  a local copy on your machine.
* The terminal runs commands in a current working directory. Commands such as
  ``cd my_directory`` and ``git clone`` depend on where you are in the file system.
* A conda environment keeps the Python packages for this practical separate
  from other Python installations.
* A Jupyter kernel is the Python process that runs notebook cells. For this
  practical, choose the ``Python (lfric-mesh)`` kernel so that the notebook uses
  the packages installed in the setup steps below.

.. list-table:: Recommended introductory resources
   :header-rows: 1
   :widths: 22 34 44

   * - Area
     - Use this when
     - Recommended resource
   * - Git and GitHub
     - You need to understand repositories, commits, branches, remotes, or why
       the training material is hosted on GitHub.
     - Start with the official GitHub pages on `About GitHub and Git
       <https://docs.github.com/en/get-started/start-your-journey/about-github-and-git>`_
       and `Git basics <https://docs.github.com/en/get-started/git-basics>`_.
   * - Cloning a repository
     - You need help with the ``git clone`` command used below.
     - Use GitHub's official `Cloning a repository
       <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_
       guide.
   * - Branches and pull requests
     - You want context for how changes are usually made and reviewed in a
       GitHub-hosted project.
     - Read GitHub's official `GitHub flow
       <https://docs.github.com/en/get-started/using-github/github-flow>`_
       guide.
   * - Git as a version-control tool
     - You want the Git project's own reference material, or a longer
       beginner-friendly worked lesson.
     - Use the official `Pro Git book
       <https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control>`_
       for background, or the `Software Carpentry Git novice lesson
       <https://swcarpentry.github.io/git-novice/>`_ for a practical tutorial.
   * - Terminal and file paths
     - You are not yet comfortable with commands such as ``cd``, moving around
       folders, or running commands from the correct directory.
     - Work through the `Software Carpentry Unix Shell lesson
       <https://swcarpentry.github.io/shell-novice/>`_. It is not specific to
       LFRic, but it covers the command-line skills used here.
   * - Jupyter and notebooks
     - You are new to notebooks or want to understand what JupyterLab is before
       running ``jupyter lab``.
     - Start with :ref:`using-jupyter-notebooks`, then use the official
       `Project Jupyter documentation <https://docs.jupyter.org/en/latest/>`_
       for more detail.
   * - Notebook cells and kernels
     - You need to understand how to run cells, switch kernels, or stop a kernel
       that is still running.
     - Use :ref:`using-jupyter-notebooks` for the course workflow, then
       JupyterLab's `Notebooks
       <https://jupyterlab.readthedocs.io/en/stable/user/notebook.html>`_ page
       for more detail.
   * - Python environments
     - You need help understanding ``conda create``, ``conda activate``, or why
       the practical uses a named environment.
     - Use the official conda `Getting started with conda
       <https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html>`_
       and `Managing environments
       <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_
       documentation. For the Jupyter kernel command used below, see IPython's
       `Installing the IPython kernel
       <https://ipython.readthedocs.io/en/stable/install/kernel_install.html>`_
       page.

If you are completely new to these tools, a useful preparation route is:

1. Learn enough terminal usage to move between directories and run commands.
2. Read the GitHub introduction to Git and practise cloning a repository.
3. Read the JupyterLab interface and notebook basics pages.
4. Return to this practical and follow the setup commands exactly.

Get the training repository
---------------------------
If you do not already have this repository locally, clone it:

.. code-block:: console

   git clone https://github.com/MetOffice/LFRic-Atmosphere-Training.git
   cd LFRic-Atmosphere-Training

If you already have a local clone, move into it:

.. code-block:: console

   cd /path/to/LFRic-Atmosphere-Training

Set up the Python environment
-----------------------------
For the full mesh and regridding practicals, use a conda environment:

.. code-block:: console

   conda create -n lfric-mesh python=3.12 -y
   conda activate lfric-mesh
   conda install -c conda-forge esmpy -y
   python -m pip install -e '.[notebooks]'
   python -m ipykernel install --user --name lfric-mesh --display-name "Python (lfric-mesh)"

Start the tutorial
------------------
Once the environment is set up:

1. Activate the environment:

   .. code-block:: console

      conda activate lfric-mesh

2. Move to the tutorial notebook directory:

   .. code-block:: console

      cd notebooks/iris-mesh-tutorial/notebooks

3. Start JupyterLab:

   .. code-block:: console

      jupyter lab

4. In the JupyterLab file browser, open the first tutorial notebook,
   ``00_Mesh_Tutorial_Intro.ipynb``.

5. With the notebook open, select:

   - ``Kernel -> Change Kernel -> Python (lfric-mesh)``

   If JupyterLab asks you to choose a kernel as the notebook opens, select
   ``Python (lfric-mesh)`` from that dialog instead.

.. important::
   Always launch JupyterLab from within ``notebooks/iris-mesh-tutorial/notebooks`` to ensure paths and imports work correctly.

After running ``jupyter lab``, a new browser window or tab should automatically open.
If it does not open automatically, copy the URL shown in the terminal into your browser.

Recommended learning path
-------------------------
The notebooks are ordered by filename so they appear in sequence in JupyterLab.

1. Work through the core content in this order:

   - ``00_Mesh_Tutorial_Intro.ipynb``
   - ``01_Load_and_Examine.ipynb``
   - ``02_Meshes.ipynb``
   - ``03_Plotting.ipynb``
   - ``04_Regridding.ipynb``
   - ``05_RegionExtraction.ipynb``

2. Complete the consolidation exercises:

   - ``06_Exercise_01.ipynb``
   - ``07_Exercise_02.ipynb``

Optional auxiliary content
--------------------------
After completing the core pathway, optional auxiliary notebooks are available:

- ``80_Bonus_01_mesh_from_numbers.ipynb``
- ``81_Bonus_02_Mesh_Connectivities_demo.ipynb``
- ``82_Bonus_03_MeshCube_Extraction.ipynb``

Upstream relationship
---------------------
- Upstream source: `scitools-classroom/iris-mesh-tutorial <https://github.com/scitools-classroom/iris-mesh-tutorial>`_
- This repository contains the training-delivery copy used in LFRic Atmosphere training.
- General improvements that are not LFRic-specific should be proposed back to the upstream project.

For file-level details and maintainer/reference notes, see:

- ``notebooks/README.md``
- ``notebooks/iris-mesh-tutorial/README.md``
