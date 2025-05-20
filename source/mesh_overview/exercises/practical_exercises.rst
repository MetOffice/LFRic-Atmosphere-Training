**************************************************
Practical using unstrucutrued data in Jupyter Lab
**************************************************

The Mesh Tutorial provides training on handling LFRic unstructured mesh data.

All tutorial content is delivered through interactive Jupyter notebooks, which combine explanatory material and practical exercises for students.
There are five Jupyter notebook which the sections below provide guidance on how to access them.

Download the tutorial from GitHub
-------------------------------------

To download the tutorial materials, follow these steps:

1. Open a terminal.

2. Create a directory where you want to store the tutorial files and move into it:

 .. code-block:: console

     mkdir data-tutorials
     cd data-tutorials

3. Clone the repository into the new directory:

 .. code-block:: console

     git clone https://github.com/scitools-classroom/iris-mesh-tutorial.git

4. Navigate to the cloned repository:

 .. code-block:: console

     cd iris-mesh-tutorial


Set up the Python environment
----------------------------------
To ensure compatibility with the tested versions of required packages, create a Python environment using the provided lockfile:

 .. code-block:: console

     conda create --name meshtut_safelocked_env --file tutorial_conda_env_resolved.lock

This command will create a new Conda environment named meshtut_safelocked_env with all necessary packages installed.

Start the tutorial
----------------------
Once the environment is set up:

1. Activate the environment:

 .. code-block:: console
    
    conda activate meshtut_safelocked_env

2. Navigate to the /notebooks directory inside the cloned repository:

 .. code-block:: console

    cd notebooks

3. Start Jupyter Lab:

 .. code-block:: console

    jupyter lab

.. important::
    Always launch Jupyter Lab from within the /notebooks directory to ensure that paths and files are correctly located.

After running the jupyter lab command, a new browser window or tab should automatically open, displaying the Jupyter Lab interface.
If the browser does not open automatically, you can manually copy and paste the URL displayed in the terminal into your browser.

Get Started
------------
To begin the tutorial:

1. In Jupyter Lab, open the notebook Mesh_Tutorial_Intro.ipynb. After opening the notebook, the introductory screen will appear, as shown below.

 .. image:: /_static/iris_tutorial.png
    :width: 600px

