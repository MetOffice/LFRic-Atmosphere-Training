PSyKAl and PSyclone
===================

LFRic is designed so scientists and software engineers can work on different
parts of the code independently. To implement this separation of concerns,
LFRic uses a domain-specific language (DSL) — a special programming layer that
separates:

Natural science code:
  Equations and models that describe the atmosphere, physics, and other
  scientific processes.

Computational science code:
  The parallelisation, data management, and performance optimisations that
  make the model run efficiently on computers.

The software architecture that enables this is called 
PSyKAl (
:external+psyclone:doc:`user_guide/introduction_to_psykal` - short for
:external+psyclone:ref:`psy-layer`,
:external+psyclone:ref:`kernel-layer`,
:external+psyclone:ref:`algorithm-layer`
).

* Scientific operations on full fields are implemented in the
  :external+psyclone:ref:`algorithm-layer`.
* The :external+psyclone:ref:`kernel-layer`, specifies operations for
  vertical columns.
* Parallelism is implemented in the :external+psyclone:ref:`psy-layer` which
  is auto generated with a tool called :external+psyclone:doc:`PSyclone <index>`

.. figure:: /_static/psykal.png
   :width: 650px

   Separation of Natural and Computational Science in the PSyKAl architecture.
