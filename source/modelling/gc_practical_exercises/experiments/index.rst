******************************
Experiments with Global Models
******************************

.. admonition:: Thought experiment: How would you design your experiment?

   As scientists we want to explore how climate models perform and respond to changes. How sensitive are they to   CO2 or what impact does an eddy parametrisation have on ocean circulation. **Think** about what parameters you would want to test within a global model? Once you have an idea, think about the next questions.

   * Where you might change this - is it in the **configuration namelist** settings within the workflow or in a ** source code**?

   * Browse the source code and workflow to look see how you might make this change. 

   * What **diagnostic** would you plot to see the change?

.. Caution:: If you decide to test your own experiment with a code or configuration change, be ready to do lots of debugging! If you want an example which is tried and tested, use the given examples below.

Main Practical
^^^^^^^^^^^^^^
* Run a simulation a with different experimental setup

* Either use an existing experiment or your previous hypothesis

* Create a branch for each new experiment (to limit the new workflow IDs created)

* Plot the data and look for evidence of changes

.. note:: Feel free to enlarge the size of these changes (e.g. 20x CO2) if your analysis is not detecting much of  an impact. Copy the output files (files explained at the end of the last section) to your local Linux workstation  and analyse the files using Python/Iris. Try to plot differences between the experiments and the control in the fields that you think will be most strongly affected. If possible make a prediction at what these   differences might show before you do the plots. Were your predictions right?

.. toctree::
   :maxdepth: 2
   :caption: Contents

   add_diag/add_diag.rst
   blk_si/blk_si.rst
   earth_rot/earth_rot.rst
   rmv_evap/rmv_evap.rst