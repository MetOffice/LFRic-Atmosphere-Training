***********************
Quiz: GC Configurations
***********************

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