**************************
Tools for Modelling
**************************

Numerical weather prediction (NWP) and climate models have a large numbers of jobs which are executed at regular intervals to process new data and generate new predictions and projections. Dependencies between these cycles creates a single never-ending workflow.

Momentum prediction and projection systems are built on **Rose** and **Cylc (“Silk”)** to manage infinite cycling workflows efficiently even after delays in real-time operation, or in historical runs, when cycles can typically interleave for much-increased throughput.

.. admonition:: Aims and objectives

   * Familiarise you with the tools and processes used to manage and run Momentum prediction and projection systems
   * Direct you to resources for learning more about these tools

.. toctree::
   :maxdepth: 1
   :caption: Contents

   mosrs/mosrs.rst
   github/github.rst
   cylc/cylc.rst
   rose/rose.rst
   quiz/quiz.rst
