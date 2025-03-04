Working Practices
=================

Developers for LFRic Atmosphere need to know the `Simulation Systems Working Practices <https://metoffice.github.  io/simulation-systems>`_, which detail the development cycle and process. The `Working Practices <https://         metoffice.github.io/simulation-systems/WorkingPractices/working_practices.html>`_ pages give instructions for      `ticketing <https://metoffice.github.io/simulation-systems/WorkingPractices/tickets.html>`_, `branching <https://  metoffice.github.io/simulation-systems/WorkingPractices/branches.html>`_, `developing <https://metoffice.github.io/simulation-systems/WorkingPractices/developing_change.html>`_, working with `multiple repositories <https://       metoffice.github.io/simulation-systems/WorkingPractices/multi_repository.html>`_, `testing <https://metoffice.     github.io/simulation-systems/WorkingPractices/testing.html>`_, and passing the code and science `reviews <https:// metoffice.github.io/simulation-systems/WorkingPractices/reviews.html>`_.

.. figure:: /_static/working_practices.jpg
  :width: 650px

  Simulation Systems Working Practices.

The Simulation Systems pages also include details about the `support contacts <https://metoffice.github.io/        simulation-systems/FurtherDetails/who.html>`_ and a `Discussions <https://github.com/MetOffice/simulation-systems/ discussions/categories/lfric>`_ forum.


PSyKAl and PSyclone
^^^^^^^^^^^^^^^^^^^

LFRic uses a domain specific language to separate computational science from natural science in the programming.   The software architecture to do this is called `PSyKAl <https://psyclone.readthedocs.io/en/stable/                 introduction_to_psykal.html>`_, which stands for `Parallel System <https://psyclone.readthedocs.io/en/stable/      introduction_to_psykal.html#psy-layer>`_, `Kernel <https://psyclone.readthedocs.io/en/stable/                      introduction_to_psykal.html#kernel-layer>`_, and `Algorithm <https://psyclone.readthedocs.io/en/stable/            introduction_to_psykal.html#algorithm-layer>`_.

Scientific operations on full field are implemented in the Algorithm layer. Kernels specify operations for         vertical columns. Parallelism is implemented in the Parallel System layer which is auto generated with a tool      called `PSyclone <https://psyclone.readthedocs.io/en/stable/>`_.

.. figure:: /_static/psykal.png
  :width: 650px

  Separation of Natural and Computational Science in the PSyKAl architecture.

