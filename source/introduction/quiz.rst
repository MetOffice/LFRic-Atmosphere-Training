************************
Introduction review quiz
************************

This quiz reviews the main ideas introduced in the first module.

.. quizdown::

   ---
   primary_color: orange
   secondary_color: lightgray
   text_color: black
   shuffle_questions: false
   ---

   ## What is LFRic Atmosphere?

   1. [ ] A workflow engine for running repeated model tasks
       > Incorrect. Workflow execution is handled by tools such as Cylc.
   1. [x] The atmospheric model component of the Momentum Framework
       > Correct! LFRic Atmosphere is the atmosphere component within Momentum.
   1. [ ] A visualisation package for plotting model output
       > Incorrect. Visualisation is handled by separate analysis tools.
   1. [ ] A repository hosting service for model code
       > Incorrect. Repository hosting is a separate development tool.

   ## Why is seamless modelling important for weather and climate prediction?

   1. [ ] It means every forecast and climate simulation uses a different model family
       > Incorrect. Seamless modelling is about consistency, not separation.
   1. [x] It supports consistent modelling across different spatial and temporal scales
       > Correct! The same model family can support applications from short-range weather prediction to long-term climate projection.
   1. [ ] It removes the need for physical parameterisations
       > Incorrect. Parameterisations remain an important part of the model.
   1. [ ] It is only used for regional forecasting
       > Incorrect. The module describes use across a broad range of applications.

   ## Which statement best describes Science Configurations in the Momentum Framework?

   1. [ ] They are temporary notes that record who ran a model experiment
       > Incorrect. Science Configurations are formal model setups, not informal notes.
   1. [ ] They are the hardware systems used to run the model
       > Incorrect. They describe scientific and numerical setup, not hardware.
   1. [x] They define tested scientific and numerical setups for model components
       > Correct! Science Configurations specify settings such as domain, resolution, coupling options, and parameter choices.
   1. [ ] They replace the need for model components
       > Incorrect. Science Configurations use model components; they do not replace them.

   ## LFRic Atmosphere is the successor to which earlier Met Office atmospheric model?

   1. [ ] NEMO
       > Incorrect. NEMO is an ocean model.
   1. [ ] JULES
       > Incorrect. JULES is the land surface model.
   1. [x] The Unified Model
       > Correct! LFRic Atmosphere succeeds the Unified Model.
   1. [ ] OASIS
       > Incorrect. OASIS is a coupler, not the predecessor of LFRic Atmosphere.

   ## Which pair of features is introduced by LFRic Atmosphere compared with the Unified Model?

   1. [ ] A latitude-longitude grid and no dynamical core
       > Incorrect. LFRic moves away from the traditional latitude-longitude grid and has a dynamical core.
   1. [x] A cubed-sphere mesh and the GungHo mixed finite-element dynamical core
       > Correct! These are key features highlighted in the module.
   1. [ ] Manual coupling and spreadsheet-based configuration
       > Incorrect. Those are not features of LFRic Atmosphere.
   1. [ ] A single-purpose design for one forecast range only
       > Incorrect. LFRic Atmosphere is part of a seamless modelling framework.

   ## Why is LFRic Atmosphere designed with modern high-performance computing in mind?

   1. [ ] To avoid running on supercomputers
       > Incorrect. Weather and climate models depend on high-performance computing.
   1. [ ] To make all science code hardware-specific
       > Incorrect. The infrastructure aims to separate science description from hardware optimisation details.
   1. [x] To improve scalability, portability, and performance on current and future architectures
       > Correct! The module links LFRic development to modern and future high-performance computing needs.
   1. [ ] To remove the need for testing Science Configurations
       > Incorrect. Tested configurations remain central to reproducible modelling.
