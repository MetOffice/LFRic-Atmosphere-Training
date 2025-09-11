***********
Core Models
***********

The Momentum framework develops four core models: 

* **Atmosphere**: `LFRic <https://www.metoffice.gov.uk/research/approach/modelling-systems/lfric>`_

* **Land**: Joint UK Land Environment Simulator (`JULES <https://jules.jchmr.org/>`_)

* **Ocean**: Nucleus for European Modelling of the Ocean (`NEMO <https://www.nemo-ocean.eu/>`_)

* **Sea Ice**: Sea Ice modelling Integrated Initiative (`SI³ <https://zenodo.org/records/7534900#.Y8GIF-xKg-Q>`_)

In the GC approach, the atmosphere and land models are integrated together to form a *Global Atmosphere Land* (GAL) model, and the Ocean and Sea Ice models are integrated to yield the *Global Ocean and Sea Ice* (GOSI) model. 

This is because the atmosphere-land (ocean-sea ice) processes are physically interconnected, meaning the two models need to exchange data every timestep, requiring them to be contained in a single executable. This is known as *intra-model coupling*.

The GAL and GOSI models are coupled to form the GC configuration. This is done via the *OASIS* coupler. OASIS allows for the exchange of information between the different components of the model at varied resolutions and timescales, known as *inter-model* coupling. This alternative approach is necessary because ocean and sea ice processes typically evolve on longer timescales and larger spatial scales than atmospheric and land processes meaning that they cannot efficiently be combined in the same executable.

.. admonition:: Fun fact!

   LFRic, pronounced "elfrick", was named after Lewis Fry Richardson, a pioneering British meteorologist who made significant contributions to the field of numerical weather prediction. His methods laid the groundwork for modern weather forecasting, and the name LFRic pays homage to his legacy in atmospheric science.