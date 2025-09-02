Introduction to Global Coupled (GC) configurations
==================================================

Introduction and Seamless Modelling
-----------------------------------

The Momentum framework's global coupled (GC) models are built upon core models, which are modular components that can be combined in various ways to create *science configurations*. A science configuration is a frozen package of mature science settings which has been rigorously tested across seamless timescales from NWP to climate.

The GC science configurations are central to the Momentum framework's :ref:`seamless-modelling` strategy. By testing the consistency of the configuration across temporal and spatial scales, the approach supports accurate and reliable predictions of weather, climate, and environmental processes. Furthermore, the modular nature of the core models allows for flexibility and adaptability in the modelling process and development, enabling scientists to tailor configurations to specific research needs or operational requirements.

.. image:: /_static/seamless_modelling.png
   :width: 650px

Core Models, Science Configurations, and GMED
---------------------------------------------

The Momentum framework develops four core models: 

* **Atmosphere**: `LFRic <https://www.metoffice.gov.uk/research/approach/modelling-systems/lfric>`_

* **Ocean**: Nucleus for European Modelling of the Ocean (`NEMO <https://www.nemo-ocean.eu/>`_)

* **Land**: Joint UK Land Environment Simulator (`JULES <https://jules.jchmr.org/>`_)

* **Sea Ice**: Sea Ice modelling Integrated Initiative (`SI³ <https://zenodo.org/records/7534900#.Y8GIF-xKg-Q>`_)

In the GC approach, the atmosphere and land models are integrated together to form a *Global Atmosphere Land* (GAL) model, and the Ocean and Sea Ice models are integrated to yield the *Global Ocean and Sea Ice* (GOSI) model. The reason for this is that the atmosphere-land (ocean-sea ice) processes are physically interconnected, meaning the two models need to exchange data every timestep, requiring them to be contained in a single executable. This is known as *intra-model coupling*.

The GAL and GOSI models are coupled to form the GC configuration. This is done via the *OASIS* coupler. OASIS allows for the exchange of information between the different components of the model at varied resolutions and timescales, known as *inter-model* coupling. This alternative approach is necessary because ocean and sea ice processes typically evolve on longer timescales and larger spatial scales than atmospheric and land processes meaning that they cannot efficiently be combined in the same executable.

More specifically, a science configuration is when a defined version of each of the core models is combined together with a set of science settings, such as parameterisations and resolutions, to create a complete model system. The science configuration is then tested and evaluated to ensure that it meets the required standards for accuracy and reliability. Once this is done, the configuration is frozen, numbered, and released as a package that can be used for research and operational purposes; this is illustrated in the diagram below.

.. image:: /_static/components.png
   :width: 650px

Once a GC configuration is defined, it can be used for different systems at the Met Office and across the Momentum partnership. For example:

* **GC3.1** was implemented in **UKESM1.1** for CMIP6

* **GC4** was implemented for **PS45** (Met Office's operational suite for NWP)

* **GC4** was implemented for **ACCESS-S1** (the Bureau of Meteorology's seasonal system)

Each GC configuration goes through an approximate 2-year development cycle, where it is tested for key systematic errors. The configuration has individual component testing and package testing, with continuous evaluation and verification. This is done by the Momentum Partnership.

The GMED team has strong links throughout the Momentum Partnership to ensure that the GC configurations are developed and evaluated in a collaborative manner, utilising the expertise of scientists from different centres and regions. This pooling of knowledge and resource helps to ensure that the configurations are robust, reliable, and suitable for a wide range of applications while also accelerating the development process.

.. admonition:: Interested in getting involved in evaluation of science configurations?

   One way to get involved is by joining a **PEG (Priority Evaluation Group)** or a **CoG (Collaboration Group)**.  

   * **PEGs** focus on a few key systemic biases, making them a great way to become involved. 
   
   * **CoGs** are larger groups that focus on a wider range of issues, allowing for more comprehensive evaluation and development of the configurations.
  
   * If interested, find the PEG or CoG lead on the GMED Met Office Science Repository Service (MOSRS) pages and contact them, or you can contact Momentum_Partnership@metoffice.gov.uk.

.. image:: /_static/seamless_dev_cycle.png
   :width: 650px

In July 2022, the final UM-based GC configuration was released, 'GC5', before the implementation of the LFRic atmospheric model into GC configurations. LFRic is the next-generation atmospheric model being developed by the Momentum framework, which is designed to be more modular and flexible than the UM. It is intended to replace the UM in future GC configurations, allowing for more efficient and effective modelling of atmospheric processes.

.. admonition:: Fun fact!

   LFRic, pronounced "elfrick", was named after Lewis Fry Richardson, a pioneering British meteorologist who made significant contributions to the field of numerical weather prediction. His methods laid the groundwork for modern weather forecasting, and the name LFRic pays homage to his legacy in atmospheric science.

Following GC5-UM, there was a project associated with the Next Generation Modelling System (NGMS) programme to develop a GC5-LFRic science configuration. This was a like-for-like LFRic version of GC5, for purely research and validation purposes. The GC5-LFRic configuration will not be released as a science configuration, but it has been used to validate the LFRic model in a coupled configuration and will be the basis for the next science configuration, GC6.

GC6 will be the first operational use of LFRic in a science configuration at the Met Office and across the Momentum Partnership. GC6 will be implemented in PS49 and in UKESM3 for CMIP8. The development of GC6 is ongoing, with the first release expected in early 2026.

.. quizdown::

   ---
   title: GC Configurations Quiz
   description: Test your understanding of Global Coupled (GC) configurations.
   shuffle: true
   show_answers: true
   show_score: true
   show_correct_answers: true
   show_incorrect_answers: true
   show_question_count: true
   ---

   ## What is a science configuration in the context of Momentum framework?
   > hint: Think of something that's carefully tested and not changed on a whim.
   1. [ ] A real-time weather forecast
   1. [x] A frozen package of mature science settings tested across timescales
   > Correct! A science configuration is a carefully tested and frozen package of settings.
   1. [ ] A software update for LFRic
   1. [ ] A set of climate observations

   ## Which of the following is *not* one of the Momentum framework’s four core models?
   > hint: One of these is popular in the US, not the UK.
   1. [ ] LFRic
   1. [ ] NEMO
   1. [ ] CICE
   1. [x] WRF
   > Correct! WRF is not part of the Momentum framework; it's a different atmospheric model.

   ## What does GAL stand for in the GC configuration?
   > hint: The name contains two important parts of the Earth system.
   1. [ ] Global Atmospheric Layer
   1. [x] Global Atmosphere Land
   > Correct! GAL stands for Global Atmosphere Land.
   1. [ ] General Atmospheric Logic
   1. [ ] Global Analysis Loop

   ## What is the purpose of the OASIS coupler in GC configurations?
   > hint: Think of OASIS as a matchmaker for model components.
   1. [ ] To simulate sea ice melting
   1. [x] To couple the GAL and GOSI components
   > Correct! OASIS couples the GAL and GOSI components.
   1. [ ] To visualize model outputs
   1. [ ] To replace LFRic

   ## Which GC configuration was the last to use the Unified Model (UM)?
   > hint: The number is one higher than GC4.
   1. [ ] GC3.1
   1. [ ] GC4
   1. [x] GC5
   > Correct! GC5 was the last configuration to use the UM.
   1. [ ] GC6

   ## What is LFRic named after?
   > hint: He was a pioneer in weather prediction 1. look for the initials.
   1. [ ] A famous climate model
   1. [ ] Low-Frequency Radiative Instability Code
   1. [x] Lewis Fry Richardson, a British mathematician
   > Correct! LFRic is named after Lewis Fry Richardson.
   1. [ ] A programming language

   ## How are the GAL and GOSI components coupled?
   > hint: They need a little help from a friend called OASIS.
   1. [ ] Intra-model coupling
   1. [x] Inter-model coupling via OASIS
   > Correct! They are coupled via OASIS, which is inter-model coupling.
   1. [ ] Manual data transfer
   1. [ ] Shared memory execution

   ## Are GC configurations used only for climate projections?
   > hint: Think bigger - weather and climate are both in the mix.
   1. [ ] Yes, only for long-term climate studies
   1. [x] No, they are used across weather and climate timescales
   > Correct! GC configurations are used for both weather and climate.
   1. [ ] Only for seasonal forecasts
   1. [ ] Only for operational NWP

   ## What is the first GC configuration to use LFRic operationally?
   > hint: It's the highest number in the list.
   1. [ ] GC4
   1. [ ] GC5
   1. [ ] GC5-LFRic
   1. [x] GC6
   > Correct! GC6 will be the first operational use of LFRic.

   ## What are PEGs and CoGs?
   > hint: Not mechanical parts, but groups of people.
   1. [ ] Types of model components
   1. [x] Evaluation and collaboration groups within the GC development process
   > Correct! PEGs and CoGs are groups that help evaluate and develop GC configurations.
   1. [ ] Ocean modelling tools
   1. [ ] Coupling interfaces

   ## What is the main advantage of the seamless modelling strategy?
   > hint: Seamless means smooth transitions - think consistency.
   1. [ ] It reduces the need for ocean models
   1. [x] It enables consistent modelling across timescales and spatial resolutions
   > Correct! Seamless modelling ensures consistency across different scales.
   1. [ ] It simplifies data storage
   1. [ ] It avoids the need for testing

   ## Which of the following systems has implemented a Momentum GC configuration?
   > hint: Only one of these has "UK" in its name.
   1. [x] UKESM1.1
   > Correct! UKESM1.1 uses GC3.1.
   1. [ ] GFS
   1. [ ] ICON
   1. [ ] ERA5

   ## What is the role of the GMED team?
   > hint: They're the brains behind GC development.
   1. [ ] To run operational forecasts
   1. [x] To evaluate and develop GC configurations collaboratively
   > Correct! The GMED team focuses on evaluating and developing GC configurations.
   1. [ ] To manage IT infrastructure
   1. [ ] To publish climate reports

   ## Why are the atmosphere and land models integrated into a single executable?
   > hint: They need to talk to each other every timestep.
   1. [ ] To reduce memory usage
   1. [x] Because they are physically interconnected and exchange data every timestep
   > Correct! The atmosphere and land models are closely linked and need to exchange data frequently.
   1. [ ] To simplify the codebase
   1. [ ] To allow for manual tuning

   ## How long is the typical development cycle for a GC configuration?
   > hint: It's how long it took to construct the Panama canal.
   1. [ ] 6 months
   1. [ ] 1 year
   1. [x] Approximately 2 years
   > Correct! The development cycle is about 2 years.
   1. [ ] 5 years