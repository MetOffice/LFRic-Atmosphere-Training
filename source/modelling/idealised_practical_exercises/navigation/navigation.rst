******************************
Navigating the Idealised Suite
******************************

Once you have copied the regional nesting suite (e.g. ``u-dz791``), the next step is to navigate to the suite directory and open it using the Rose graphical user interface (GUI).

Step 1: Navigate to the suite directory
---------------------------------------

Open a terminal and change to the directory where your suite is located:

.. code-block:: bash

   cd ~/roses/<suite-id>

Step 2: Open the suite in the Rose GUI
--------------------------------------

Launch the Rose editor by running:

.. code-block:: bash

   rose edit &

- This command opens the suite in the Rose graphical user interface, allowing you to view and modify its configuration.
- The ``&`` at the end runs the GUI in the background, so your terminal remains available for other commands.
- To bring it to the foreground, type `fg`

Step 3: Setting up the suite
----------------------------

Once the GUI is open, you can begin configuring the suite for your specific experiment or run by navigating through the tabs on the left side of the window.

General Run Options
~~~~~~~~~~~~~~~~~~~

Navigate to the ``General run options`` tab to define the key settings required to run your nesting suite.

.. _fig-idealised_top_level_options:

.. figure:: /_static/idealised_top_level_options.png
   :width: 1200px
   :align: center
   :alt: Top-level options in the idealised suite `u-dz791`.
   
   Screenshot of the Rose configuration editor showing the top-level options panel of the idealised suite `u-dz791`.
   
- **VN**

  LFRic Apps version. Currently it's set to `3.0` but we will upgrade this suite soon.

- **BUILD_LFRIC**

  Include compilation of the model (required for the first run).

- **HOUSEKEEPING**

  Clean up output directory on successful finish. Currently only removes `xios_*` log files.

- **EXPT_DT**

  Dynamical time step of the model in seconds. Default: 10 s.

- **LFRIC_RES**

  Select a horizontal mesh. The convention for bi-periodic Cartesian meshes is to name them as `(number of x-points)x(number of y-points)-(dx)x(dy)`, where `dx` and `dy` are grid steps in the x- and y-directions, respectively.
  Default: 128 by 128 points with the grid spacing of 2000 m.

- **LFRIC_LEVS**

  Select a vertical levels set. Default: 200 uniformly spaced levels from 0 to 900 km.
  Yes, *km*.
  It's a hydrogen-dominated atmosphere, so the scale height is much larger than that for Earth's air.