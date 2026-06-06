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

Top-level configuration
~~~~~~~~~~~~~~~~~~~~~~~

Navigate to the ``template variables`` tab to check and, if needed, change the top-level settings required to run the idealised suite.

.. _fig-idealised_top_level_options:

.. figure:: /_static/idealised_top_level_options.png
   :width: 1200px
   :align: center
   :alt: Top-level options in the idealised suite `u-dz791`.
   
   Screenshot of the Rose configuration editor showing the top-level options panel of the idealised suite `u-dz791`.

- **EX_HOST**

  Select what machine to run the experiment on.
  Currently only the Met Office ex1a zone or Monsoon are available.

- **VN**

  LFRic Apps version. Currently it's set to `3.0` but we will upgrade this suite soon.

- **BUILD_LFRIC**

  Include compilation of the model (required for the first run).

- **COMPILER**

  Which compiler to use.
  Note: Cray (`CCE`) is preferred as its faster than GNU.

- **EXPT_DT**

  Dynamical time step of the model in seconds. Default: 10 s.

- **LFRIC_RES**

  Select a horizontal mesh. The convention for bi-periodic Cartesian meshes is to name them as `(number of x-points)x(number of y-points)-(dx)x(dy)`, where `dx` and `dy` are grid steps in the x- and y-directions, respectively.
  Default: 128 by 128 points with the grid spacing of 2000 m.

- **LFRIC_LEVS**

  Select a vertical levels set. Default: 200 uniformly spaced levels from 0 to 900 km.
  Yes, *km*.
  It's a hydrogen-dominated atmosphere, so the scale height is much larger than that for Earth's air.

- **PHYSICS_CONF**

  Select a physical configuration.
  Default: GungHo-only configuration (i.e., dynamical core only).

- **EXPT_START**

  Experiment start date and time.
  Given in a cylc time format: YYYYMMDDTHHMMZ
  The actual numbers are irrelevant for an idealised case.

- **EXPT_RUNLEN**

  Experiment run length in the cylc date-time format, e.g. `PT10H30M`, `P20D`, etc.

- **EXPT_RESUB**

  Experiment resubmission frequency, i.e. the length of continuation runs, in the cylc date-time format.

- **TOTAL_RANKS_REQ**

  Total number of processors to run the model on.
  Note: there are 128 per node on the ex1a machine and Monsoon.

- **LFRIC_CRUN_WALLCLOCK**

  Wallclock time to allocate to each continuation run.
  Given in the cylc date-time format, e.g. `PT1H`.
  Note: the limit is 3 hours on the Met Office ex1a zone and Monsoon.

- **HOUSEKEEPING**

  Clean up output directory on successful finish. Currently only removes `xios_*` log files.

- **MIRROR_LOC**

  Alias for the git mirror location.
  Check your `~/.gitconfig` when setting this up.

- **USE_MIRRORS**

  If true, use local mirrors to clone the model's source code.
  If false, clone from GitHub.

- **USE_TOKENS**

  If true, switches sources to use https URLs instead of ssh.
  This requires a personal access token to be setup to authenticate with GitHub.
