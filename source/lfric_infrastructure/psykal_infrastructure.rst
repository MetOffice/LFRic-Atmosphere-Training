PSyKAl and PSyclone
===================

LFRic uses a domain specific language to separate computational science from natural science in the programming.   The software architecture to do this is called `PSyKAl <https://psyclone.readthedocs.io/en/stable/                 introduction_to_psykal.html>`_, which stands for `Parallel System <https://psyclone.readthedocs.io/en/stable/      introduction_to_psykal.html#psy-layer>`_, `Kernel <https://psyclone.readthedocs.io/en/stable/                      introduction_to_psykal.html#kernel-layer>`_, and `Algorithm <https://psyclone.readthedocs.io/en/stable/            introduction_to_psykal.html#algorithm-layer>`_.

Scientific operations on full field are implemented in the Algorithm layer. Kernels specify operations for         vertical columns. Parallelism is implemented in the Parallel System layer which is auto generated with a tool      called `PSyclone <https://psyclone.readthedocs.io/en/stable/>`_.

.. figure:: /_static/psykal.png
  :width: 650px

  Separation of Natural and Computational Science in the PSyKAl architecture.

