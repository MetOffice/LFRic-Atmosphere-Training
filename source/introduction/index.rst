***********************************
1. Introduction to LFRic Atmosphere
***********************************

Modern weather and climate prediction requires models that can simulate
processes across a wide range of spatial and temporal scales, from local
weather events over hours and days to global climate change over decades and
centuries. These models must also be able to run efficiently on modern
high-performance computing systems.

Momentum provides the wider modelling framework, while LFRic Atmosphere
provides the atmospheric model component. Together, they provide a flexible and
scalable foundation for next-generation Earth system modelling through
collaboration between the Met Office, research institutions, universities, and
international partners.

This module introduces the LFRic Atmosphere model and the Momentum Framework.
You will learn about the principles of seamless modelling, how prediction
systems are constructed from reusable scientific components, and the key
features that distinguish LFRic Atmosphere from earlier modelling systems.

For learners who want more technical detail, the paper `LFRic: Meeting the
challenges of scalability and performance portability in Weather and Climate
models <https://www.sciencedirect.com/science/article/pii/S0743731518305306>`_
gives an overview of the model infrastructure and its scalability goals.


.. admonition:: Aims and objectives

   By the end of this module, you will be able to:

   * Explain the motivation for developing LFRic Atmosphere and the Momentum
     Framework.
   * Describe the history and evolution of LFRic Atmosphere and its
     relationship to the Unified Model.
   * Summarise the principles of seamless modelling and explain why they are
     important for Earth system prediction.
   * Identify the major components of the Momentum Framework and describe how
     they work together to build prediction and projection systems.
   * Explain why land-atmosphere coupling matters and describe the role of
     JULES in LFRic Atmosphere configurations.
   * Describe the role of the ocean and sea-ice components in coupled Momentum
     configurations.

.. toctree::
   :maxdepth: 1
   :caption: Contents

   seamless_modelling.rst
   components.rst
   land_surface_and_jules.rst
   ocean_and_sea_ice.rst
   history_context.rst
   quiz.rst
