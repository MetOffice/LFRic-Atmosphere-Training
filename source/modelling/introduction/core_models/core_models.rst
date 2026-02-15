****************
Component Models
****************

The Momentum framework represents the Earth system using four primary component models: 

* **Atmosphere**: `LFRic Atmosphere <https://www.metoffice.gov.uk/research/approach/modelling-systems/lfric>`_

* **Land**: Joint UK Land Environment Simulator (`JULES <https://jules.jchmr.org/>`_)

* **Ocean**: Nucleus for European Modelling of the Ocean (`NEMO <https://www.nemo-ocean.eu/>`_)

* **Sea Ice**: Sea Ice modelling Integrated Initiative (`SI³ <https://zenodo.org/records/7534900#.Y8GIF-xKg-Q>`_)

Together, these component models provide a comprehensive representation of the Earth system, enabling consistent simulations across weather and climate timescales.

Grouping of Component Models
----------------------------

In the Global Coupled (GC) approach, certain components are strongly coupled and therefore integrated into combined systems:

* The atmosphere and land components are combined to form the *Global Atmosphere Land* (GAL) model.
* The Ocean and Sea Ice components are combined to form the *Global Ocean and Sea Ice* (GOSI) model. 

Within each of these combined systems, information is exchanged at every model timestep. This frequent exchange reflects the strong physical coupling between the relevant processes, such as energy, moisture, and momentum fluxes. As a result, the components must run within a single executable. This form of coupling is referred to as *intra-model coupling*.

The GAL and GOSI models are further coupled to form the GC configuration. This coupling is achieved using the `OASIS <https://oasis.cerfacs.fr/en/home/>`_ coupler,  which manages the exchange of information between the two systems.
The diagram below illustrates coupling components in the GC approach.

.. figure:: /_static/components.png
   :width: 650px
   :alt: components in a GC-LFRic configuration

   Components coupling in a GC-LFRic configuration


This approach, known as *inter-model* coupling, allows components operating at different spatial resolutions and temporal scales to interact efficiently. It is particularly important because ocean and sea ice processes typically evolve more slowly and on larger spatial scales than atmospheric and land processes. Separating the systems while coupling them through OASIS provides both scientific consistency and computational efficiency.


*TODO for Forough*
*Add a sentence to mention that the limited area models also use the same model components... *

.. admonition:: Fun fact!

   LFRic, pronounced "elfrick", was named after Lewis Fry Richardson, a pioneering British mathematician who made significant contributions to the field of numerical weather prediction. His methods laid the groundwork for modern weather forecasting, and the name LFRic pays homage to his legacy in atmospheric science.
