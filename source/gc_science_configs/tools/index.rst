**************************
Tools for Global Modelling
**************************

NWP and climate models have a large numbers of jobs which are executed at regular intervals to process new data and generate new forecasts. Dependence between these forecast cycles creates a single never-ending workflow, which NWP workflow schedulers have traditionally ignored.

Met Office science configurations are built on **Rose** and **Cylc (“Silk”)** to manage infinite cycling workflows efficiently even after delays in real-time operation, or in historical runs, when cycles can typically interleave for much-increased throughput.

.. admonition:: Aims and objectives

   * To be able to identify the tools used to manage and run Momentum science configurations
   * Direct you to resources for learning more about these tools
   * Familiarise you with the tools and processes used to manage and run Momentum science configurations

.. toctree::
   :maxdepth: 1
   :caption: Contents

   mosrs/mosrs.rst
   github/github.rst
   cylc/cylc.rst
   rose/rose.rst
   quiz/quiz.rst