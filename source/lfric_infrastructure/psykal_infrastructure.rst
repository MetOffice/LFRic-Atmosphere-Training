PSyKAl and PSyclone
===================

LFRic is designed so scientists and software engineers can work on different parts of the code independently. To implement this separation of concerns, LFRic uses a domain-specific language (DSL) — a special 
programming layer — that separates:

*	**Natural science code**: equations and models that describe the atmosphere, physics, and other scientific processes.

*	**Computational science code**: the parallelisation, data management, and performance optimisations that make the model run efficiently on computers.

The software architecture that enables this is called `PSyKAl <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html>`_, which stands for `Parallel System <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#psy-layer>`_, `Kernel <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#kernel-layer>`_, and `Algorithm <https://psyclone.readthedocs.io/en/stable/introduction_to_psykal.html#algorithm-layer>`_.

Scientific operations on full fields are implemented in the Algorithm layer. Kernels specify operations for vertical columns. Parallelism is implemented in the Parallel System layer which is auto generated with a tool called `PSyclone <https://psyclone.readthedocs.io/en/stable/>`_.

.. figure:: /_static/psykal.png
  :width: 650px

  Separation of Natural and Computational Science in the PSyKAl architecture.

