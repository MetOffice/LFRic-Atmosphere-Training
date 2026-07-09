Components, Science Configurations, and Systems
===============================================

The `Momentum  <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ Framework is built from a set of interoperable scientific components that can be combined to create complete prediction and projection systems.
One of these components is LFRic Atmosphere, the atmospheric model within the framework.

To ensure scientific consistency and reproducibility, prediction systems are defined using carefully tested Science Configurations.
A Science Configuration specifies the scientific and numerical setup of model components, including parameter settings, domain, resolution, and coupling options.
Science Configurations are typically grouped into:

Global configurations
   Used for global weather and climate simulations.
Regional configurations
   Used for high-resolution simulations over limited geographical areas.
Coupled configurations
   Where atmosphere, ocean, land, and sea-ice models exchange information during a simulation.

A key feature of the Momentum development approach is the separation between several related layers of the modelling system:

Components
   Individual scientific models such as atmosphere or ocean models.
Science Configurations
   Validated scientific setups of those models.
Operational systems
   Implementations used for research, forecasting, and climate projection.

Each has its own release cycle, but they build on each other and remain compatible within the wider framework.

The naming and numbering conventions for Momentum Science Configurations continue the heritage of the Unified Model ecosystem. Examples include:

GC6
   The Global Coupled Science Configuration
RAL4
   The Regional Atmosphere and Land configuration

These are among the first Science Configurations to use LFRic Atmosphere within the Momentum Framework.

.. _fig-intro-components:

.. figure:: /_static/1/intro_components.png
   :width: 650px
   :alt: Components of prediction and projection systems

   Key functional components needed to build prediction and projection systems with the Momentum Framework.

