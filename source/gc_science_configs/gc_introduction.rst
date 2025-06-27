Introduction to Global Coupled (GC) configurations
==================================================
The Met Office's global coupled (GC) models are built upon the Met Office's core models, which are modular components that can be combined in various ways to create science configurations. A science configuration is a frozen package of mature science settings which has been rigorously tested across seamless timescales from NWP to climate.

The GC science configurations are central to the Met Office's seamless modelling strategy, which is an approach that enables the use of the same science configuration to simulate a wide range of timescales -- from numerical weather prediction (NWP) to seasonal forecasts and climate projections -- and spatial resolutions, from metres to hundreds of kilometres. By testing the consistency of the configuration across these scales, the approach supports accurate and reliable predictions of weather, climate, and environmental processes. Furthermore, the modular nature of the core models allows for flexibility and adaptability in the modelling process and development, enabling scientists to tailor configurations to specific research needs or operational requirements.

.. image:: /_static/seamless_modelling.png
   :width: 650px

The Met Office develops four core models, which are:
* **Atmosphere**: Unified Model (UM) or LFRic
* **Ocean**: Nucleus for European Modelling of the Ocean (NEMO)
* **Land**: Joint UK Land Environment Simulator (JULES) 
* **Sea Ice**: Los Alamos Sea Ice Model (CICE)
  
In the GC approach, the atmosphere and land models are integrated together to form a Global Atmosphere Land (GAL) model, and the Ocean and Sea Ice models are integrated to yield the Global Ocean and Sea Ice (GOSI). This is known as intra-model coupling. The reason for this is that the atmosphere-land (ocean-sea ice) processes are physically interconnected, meaning the two models need to exchange data every timestep, requiring them to be contained in a single executable. This is not the case when the GAL and GOSI configurations are coupled.

Inter-model coupling via the OASIS coupler is used between GAL and GOSI to create a fully coupled system. OASIS allows for the exchange of information between the different components of the model at varied resolutions and timescales, which is necessary because ocean and sea ice processes typically evolve on longer timescales and larger spatial scales than atmospheric and land processes.

More specifically, a science configuration is when a defined version of each of the core models is combined together with a set of science settings, such as parameterisations and resolutions, to create a complete model system. The science configuration is then tested and evaluated to ensure that it meets the required standards for accuracy and reliability. Once this is done, the configuration is frozen, numbered, and released as a package that can be used for research and operational purposes; this is illustrated in the diagram below.

.. image:: /_static/components.png
   :width: 650px

Once a GC configuration is defined, it can be used for different systems at the Met Office and across the Partnership. For example:
* **GC3.1** was implemented in **UKESM1.1** for CMIP6
* **GC4** was implemented for **PS45** (Met Office's operational suite for NWP)
* **GC4** was implemented for **ACCESS-S1** (the Bureau of Meteorology's seasonal system)

Each GC configuration goes through an approximate 2-year development cycle, where it is tested for key systematic errors. The configuration has individual component testing and package testing, with continuous evaluation and verification. This is done by the Global Model Evaluation and Development (GMED) team, which is part of the Met Office's Science and Technology Partnership. The GMED team has strong links throughout the Momentum Partnership to ensure that the GC configurations are developed and evaluated in a collaborative manner, utilising the expertise of scientists from different centres and regions. This pooling of knowledge and resources helps to ensure that the configurations are robust, reliable, and suitable for a wide range of applications while also accelerating the development process.

.. admonition:: Interested in getting involved in evaluation of science configurations?

   The 2-year development and evaluation cycle involves scientists from across the Partnership, utilising the varied expertise across the different centres. One way to get involved is by joining a PEG (Priority Evaluation Group) or a CoG (Collaboration Group). PEGs focus on a few key systemic biases, making them a great way to become involved. If interested, find the PEG or CoG lead on the Global Model Evaluation and Development (GMED) Met Office Science Repository Service (MOSRS) pages and contact them, or you can contact Momentum_Partnership@metoffice.gov.uk.

.. image:: /_static/seamless_dev_cycle.png
   :width: 650px

.. admonition:: Task: Explore MOSRS, GitHub and Wiki tickets

   Visit the Met Office Science Repository Service (MOSRS) and navigate to the Global Model Evaluation and Development (GMED) pages. Investigate the following:

   * Where the documentation for science configurations is stored.
   * The process of releasing configurations.
   * The differences between configurations and how they are developed.
   * The difference between the UM and LFRic versions of the GC configurations.
   * How wiki tickets are used to track and manage tasks related to science configurations.

In July 2022, the final UM-based GC configuration was released, 'GC5', before the implementation of the LFRic atmospheric model into GC configurations. LFRic is the next-generation atmospheric model being developed by the Met Office, which is designed to be more modular and flexible than the UM. It is intended to replace the UM in future GC configurations, allowing for more efficient and effective modelling of atmospheric processes.

.. admonition:: Fun fact!
   LFRic, pronounced "elfrick", was named after Lewis Fry Richardson, a pioneering British meteorologist who made significant contributions to the field of numerical weather prediction. His methods laid the groundwork for modern weather forecasting, and the name LFRic pays homage to his legacy in atmospheric science.

Following GC5-UM, there was a project associated with the Next Generation Modelling System (NGMS) programme to develop a GC5-LFRic science configuration. This was a like-for-like LFRic version of GC5, for purely research and validation purposes. The GC5-LFRic configuration will not be released as a science configuration, but it has been used to validate the LFRic model in a coupled configuration and will be the basis for the next science configuration, GC6.

GC6 will be the first operational use of LFRic in a science configuration at the Met Office and across the Momentum Partnership. GC6 will be implemented in PS49 and in UKESM3 for CMIP8. The development of GC6 is ongoing, with the first release expected in early 2026.