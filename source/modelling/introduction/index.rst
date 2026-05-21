**************************************
Introduction to Science Configurations
**************************************

.. toctree::
   :maxdepth: 1
   :caption: Contents

   core_models/core_models.rst
   science_config/science_config.rst
   quiz/quiz.rst

Developing a weather or climate model requires a large number of scientific choices, including how physical processes are represented, which numerical methods are used, and how different parts of the Earth system interact. Within the Momentum framework, these choices are organised and managed through science configurations.

A science configuration is a standardised and rigorously tested set of scientific settings for one or more model components. It provides a stable and well-defined basis for running simulations, ensuring that the selected options are scientifically consistent and suitable for a wide range of applications. Before a science configuration is released, it is evaluated across multiple spatial resolutions and temporal scales, from numerical weather prediction to climate modelling. This approach underpins the Momentum framework’s strategy for :ref:`seamless-modelling`, in which the same scientific configuration can be applied consistently across different timescales and modelling systems.

Science configurations are constructed from component models, each of which represents a key part of the Earth system. These components are combined in established ways to form complete modelling systems for research and operational use. By relying on shared, well-tested science configurations, the Momentum framework promotes scientific consistency, reproducibility, and collaboration across the weather and climate modelling community.

This chapter first introduces the component models used within the Momentum framework and explains how they are coupled. It then describes the concept of science configurations, their testing and release process, and their role in supporting seamless modelling across research and operational applications.

.. _fig-model-seamless:

.. figure:: /_static/seamless_modelling.png
   :width: 650px
   :alt: Weather and climate modelling applications across spatial and temporal scales

   Seamless modelling across spatial and temporal scales.
