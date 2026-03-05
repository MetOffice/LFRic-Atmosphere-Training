*********************************
Practical using unstructured data
*********************************

The Mesh Tutorial provides practical training on handling LFRic unstructured mesh data.

All tutorial content is delivered through interactive Jupyter notebooks.
The upstream material comes from `iris-mesh-tutorial <https://github.com/scitools-classroom/iris-mesh-tutorial>`_ and is provided in this repository under:

.. code-block:: text

   notebooks/iris-mesh-tutorial/

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
   pip install -e .[mesh_tutorials]
   python -m ipykernel install --user --name lfric-mesh --display-name "Python (lfric-mesh)"

Start the tutorial
------------------
Once the environment is set up:

1. Activate the environment:

   .. code-block:: console

      source .venv/bin/activate

2. Move to the tutorial notebook directory:

   .. code-block:: console

      cd notebooks/iris-mesh-tutorial/notebooks

3. Start Jupyter Lab:

   .. code-block:: console

      jupyter lab

4. In Jupyter, select:

   - ``Kernel -> Change Kernel -> Python (lfric-mesh)``

.. important::
   Always launch Jupyter Lab from within ``notebooks/iris-mesh-tutorial/notebooks`` to ensure paths and imports work correctly.

After running ``jupyter lab``, a new browser window or tab should automatically open.
If it does not open automatically, copy the URL shown in the terminal into your browser.

Recommended learning path
-------------------------
The notebooks are ordered by filename so they appear in sequence in Jupyter Lab.

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
