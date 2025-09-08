***********
Core Models
***********

The Momentum framework develops four core models: 

* **Atmosphere**: `LFRic <https://www.metoffice.gov.uk/research/approach/modelling-systems/lfric>`_

* **Ocean**: Nucleus for European Modelling of the Ocean (`NEMO <https://www.nemo-ocean.eu/>`_)

* **Land**: Joint UK Land Environment Simulator (`JULES <https://jules.jchmr.org/>`_)

* **Sea Ice**: Sea Ice modelling Integrated Initiative (`SI³ <https://zenodo.org/records/7534900#.Y8GIF-xKg-Q>`_)

In the GC approach, the atmosphere and land models are integrated together to form a *Global Atmosphere Land* (GAL) model, and the Ocean and Sea Ice models are integrated to yield the *Global Ocean and Sea Ice* (GOSI) model. The reason for this is that the atmosphere-land (ocean-sea ice) processes are physically interconnected, meaning the two models need to exchange data every timestep, requiring them to be contained in a single executable. This is known as *intra-model coupling*.