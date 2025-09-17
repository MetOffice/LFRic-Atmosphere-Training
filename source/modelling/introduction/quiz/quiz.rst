**************************
Quiz: Model Configurations
**************************

.. quizdown::

   ---
   title: Configurations Quiz
   description: Test your understanding of model configurations.
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
   > Try again! A science configuration is more than just a forecast.
   1. [x] A frozen package of mature science settings tested across timescales
   > Correct! A science configuration is a carefully tested and frozen package of settings.
   1. [ ] A software update for LFRic
   > Try again! It's not just a software update.
   1. [ ] A set of climate observations
   > No, but climate observations are important for evaluating science configurations.

   ## Which of the following is *not* one of the Momentum framework’s four core models?
   > hint: One of these is popular in the US, not the UK.
   1. [ ] LFRic Atmosphere
   > Try again! LFRic Atmosphere is the atmospheric model in the Momentum framework.
   1. [ ] NEMO
   > Try again! NEMO is the ocean model in the Momentum framework.
   1. [ ] SI³
   > Try again! SI³ is the sea ice model in the Momentum framework.
   1. [x] WRF
   > Correct! WRF is not part of the Momentum framework; it's a different atmospheric model.

   ## What does GAL stand for in the GC configuration?
   > hint: The name contains two important parts of the Earth system.
   1. [ ] Global Atmospheric Layer
   > Try again! Think about the components involved.
   1. [x] Global Atmosphere Land
   > Correct! GAL stands for Global Atmosphere Land.
   1. [ ] General Atmospheric Logic
   > Try again! That's not quite right.
   1. [ ] Global Analysis Loop
   > Try again! That's not the correct term.

   ## What is the purpose of the OASIS coupler in GC configurations?
   > hint: Think of OASIS as a matchmaker for model components.
   1. [ ] To simulate sea ice melting
   > Try again! OASIS couples the sea ice model with the atmospheric model but it does not simulate sea ice melting
   1. [x] To couple the GAL and GOSI components
   > Correct! OASIS couples the GAL and GOSI components.
   1. [ ] To visualize model outputs
   > Try again! Visualization is not OASIS's role.
   1. [ ] To replace LFRic
   > Try again! OASIS does not replace LFRic.

   ## Which GC configuration was the last to use the Unified Model (UM)?
   > hint: The number is one higher than GC4.
   1. [ ] GC3.1
   > Try again! GC3.1 is earlier than the last UM-based configuration.
   1. [ ] GC4
   > Try again! GC4 is not the last UM-based configuration.
   1. [x] GC5
   > Correct! GC5 was the last configuration to use the UM.
   1. [ ] GC6
   > Try again! GC6 will be the first to use LFRic operationally.

   ## What is LFRic named after?
   > hint: He was a pioneer in weather prediction 1. look for the initials.
   1. [ ] A famous climate model
   > Try again! LFRic is not named after a model.
   1. [ ] Low-Frequency Radiative Instability Code
   > Try again! That's not correct.
   1. [x] Lewis Fry Richardson, a British mathematician
   > Correct! LFRic is named after Lewis Fry Richardson.
   1. [ ] A programming language
   > Try again! It's not a programming language.

   ## How are the GAL and GOSI components coupled?
   > hint: They need a little help from a friend called OASIS.
   1. [ ] Intra-model coupling
   > Try again! Intra-model coupling is for atmosphere-land or ocean-sea ice pairs.
   1. [x] Inter-model coupling via OASIS
   > Correct! They are coupled via OASIS, which is inter-model coupling.
   1. [ ] Manual data transfer
   > Try again! It's not manual.
   1. [ ] Shared memory execution
   > Try again! They don't share memory directly.

   ## Are GC configurations used only for climate projections?
   > hint: Think bigger - weather and climate are both in the mix.
   1. [ ] Yes, only for long-term climate studies
   > Try again! GC configurations are more versatile than that.
   1. [x] No, they are used across weather and climate timescales
   > Correct! GC configurations are used for both weather and climate.
   1. [ ] Only for seasonal forecasts
   > Try again! They are not limited to seasonal forecasts.
   1. [ ] Only for operational NWP
   > Try again! They are used for more than just NWP.

   ## What is the first GC configuration to use LFRic operationally?
   > hint: It's the highest number in the list.
   1. [ ] GC4
   > Try again! GC4 uses the UM, not LFRic.
   1. [ ] GC5
   > Try again! GC5 also uses the UM.
   1. [ ] GC5-LFRic
   > Try again! GC5-LFRic is a research version, not operational.
   1. [x] GC6
   > Correct! GC6 will be the first operational use of LFRic.

   ## What are PEGs and CoGs?
   > hint: Not mechanical parts, but groups of people.
   1. [ ] Types of model components
   > Try again! They are not model components.
   1. [x] Evaluation and collaboration groups within the GC development process
   > Correct! PEGs and CoGs are groups that help evaluate and develop GC configurations.
   1. [ ] Ocean modelling tools
   > Try again! They are not tools.
   1. [ ] Coupling interfaces
   > Try again! They are not interfaces.

   ## What is the main advantage of the seamless modelling strategy?
   > hint: Seamless means smooth transitions - think consistency.
   1. [ ] It reduces the need for ocean models
   > Try again! Seamless modelling is about more than just ocean models.
   1. [x] It enables consistent modelling across timescales and spatial resolutions
   > Correct! Seamless modelling ensures consistency across different scales.
   1. [ ] It simplifies data storage
   > Try again! Data storage is not the main focus.
   1. [ ] It avoids the need for testing
   > Try again! Testing is still essential.

   ## What is the role of the GMED team?
   > hint: They're the brains behind GC development.
   1. [ ] To run operational forecasts
   > Try again! Running forecasts is not their main role.
   1. [x] To evaluate and develop GC configurations collaboratively
   > Correct! The GMED team focuses on evaluating and developing GC configurations.
   1. [ ] To manage IT infrastructure
   > Try again! IT management is not their focus.
   1. [ ] To publish climate reports
   > Try again! Publishing reports is not their main role.

   ## Why are the atmosphere and land models integrated into a single executable?
   > hint: They need to talk to each other every timestep.
   1. [ ] To reduce memory usage
   > Try again! Memory usage is not the main reason.
   1. [x] Because they are physically interconnected and exchange data every timestep
   > Correct! The atmosphere and land models are closely linked and need to exchange data frequently.
   1. [ ] To simplify the codebase
   > Try again! Code simplicity is not the main reason.
   1. [ ] To allow for manual tuning
   > Try again! Manual tuning is not the reason.

   ## How long is the typical development cycle for a GC configuration?
   > hint: It's how long it took to construct the Panama canal.
   1. [ ] 6 months
   > Try again! The development cycle is longer than that.
   1. [ ] 1 year
   > Try again! The development cycle is longer than that.
   1. [x] Approximately 2 years
   > Correct! The development cycle is about 2 years.
   1. [ ] 5 years
   > Try again! The development cycle is shorter than that.

   ## Regional model question placeholder. Maybe add more questions or replace some existing ones.
   > hint: Write a hint here.
   1. [x] Option A
   > Correct! Write feedback here.
   1. [ ] Option B
   > Try again! Write feedback here.
   1. [ ] Option C
   > Try again! Write feedback here.
   1. [ ] Option D
   > Try again! Write feedback here.