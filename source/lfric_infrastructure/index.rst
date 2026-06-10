**************************
3. LFRic code and software
**************************

In this section, LFRic is introduced from a software perspective, focusing 
on the LFRic Atmosphere model and its underlying components.

.. admonition:: In this module you will learn about...

   * how LFRic Atmosphere fits within the wider LFRic software stack and the Momentum Framework;
   * how the LFRic codebase is split across LFRic Core, LFRic Apps, and larger science component repositories;
   * how the PSyKAl architecture and PSyclone separate scientific code from parallelisation, data movement, and performance concerns;
   * which development tools and repositories you need to work with LFRic source code, configurations, and tests;
   * where the LFRic working practices are documented, including guidance on issues, branches, testing, reviews, and multi-repository development;
   * where to find support when you are unsure how to apply the working practices;
   * how model output is controlled through XIOS and the ``iodef.xml`` configuration file.

.. admonition:: At the end of this module you should be able to...

   * describe the main LFRic code repositories and identify which parts of the model they contain;
   * recognise the role of LFRic Apps, LFRic Core, science component repositories, dependencies, and interfaces in a model build;
   * explain, at a high level, how the algorithm, kernel, and PSy layers fit together in the PSyKAl approach;
   * find the appropriate working-practice guidance before creating issues, branches, tests, reviews, or multi-repository changes;
   * identify the support routes for questions about LFRic development and working practices;
   * follow the practical workflow for checking out code, compiling, running a simple configuration, making a small change, and using tests as evidence;
   * locate and modify ``iodef.xml`` to control which fields are written, at what frequency, and to which output files.


.. toctree::
   :maxdepth: 1
   :caption: Contents

   code_repositories.rst
   psykal_infrastructure.rst
   working_practices.rst
   output_control.rst
   practical_exercises.rst
