******************************
Experiments with Global Models
******************************

.. admonition:: Thought experiment: How would you design your experiment?

   As scientists we want to explore how climate models perform and respond to changes. How sensitive are they to   CO2 or what impact does an eddy parametrisation have on ocean circulation. **Think** about what parameters you would want to test within a global model? Once you have an idea, think about the next questions.

   * Where you might change this - is it in the **configuration namelist** settings within the workflow or in a ** source code**?

   * Browse the source code and workflow to look see how you might make this change. 

   * What **diagnostic** would you plot to see the change?

.. Caution:: If you decide to test your own experiment with a code or configuration change, be ready to do lots of debugging! If you want an example which is tried and tested, use the given examples below.

.. admonition:: Real World Example: Snow Albedo Tuning in HadGEM3 GC3.1

   `Kuhlbrodt et al. (2018) <https://doi.org/10.1029/2018MS001370>`_ describe a tuning change made during the development of the low-resolution version of HadGEM3 GC3.1:

      To achieve an acceptable simulation of Arctic sea ice thickness it proved necessary to reduce the albedo of snow on sea-ice by 2% in N96O1 for both infra-red (0.70 reduced to 0.68) and visible (0.98 to 0.96) parts of the solar spectrum, with all values well within observational constraints. This change was required due to the 1° ocean model failing to advect sufficient warm water into the Arctic Ocean through the narrow straits connecting the Atlantic with the Arctic.

   This is a good example of a **configuration namelist** change — a small parameter adjustment motivated by a known model bias which had a measurable impact on a key climate variable (Arctic sea ice thickness).

Next steps
^^^^^^^^^^
Now use the following practical exercises to explore different experiment configurations:

.. toctree::
   :maxdepth: 1
   :caption: Contents

   add_diag/add_diag.rst
   10xco2/10xco2.rst
   earth_rot/earth_rot.rst