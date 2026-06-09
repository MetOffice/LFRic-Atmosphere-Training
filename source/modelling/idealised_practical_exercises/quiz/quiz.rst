******************************
Quiz: Idealised Configurations
******************************

.. quizdown::

   ---
   title: Idealised Configuration Quiz
   description: Test your understanding of idealised applications of LFRic-Atmosphere.
   shuffle: true
   show_answers: true
   show_score: true
   show_correct_answers: true
   show_incorrect_answers: true
   show_question_count: true
   ---

   ## What planetary parameters are hard-wired and cannot be changed in LFRic-Atmosphere?
   > hint: Think of different science cases discussed in the training.
   1. [ ] Surface gravity
   > Try again! This parameter can certainly be changed!
   1. [x] All these can be changed
   > Correct! LFRic-Atmosphere is quite flexible!
   1. [ ] Gas constants of the background air (it is always assumed to be Earth air.)
   > Try again! This can be changed!
   1. [ ] Stellar constant (it is a constant after all!)
   > No, even for Earth simulations this could be changed.

   ## What is the heat capacity of the atmosphere set by, and can it be changed?
   > hint: It lives alongside other planetary constants such as gravity and the gas constant.
   1. [ ] It is hard-coded for Earth's air and cannot be changed
   > Try again! Just like gravity and the gas constant, the heat capacity is a configurable planetary parameter.
   1. [x] It is set by the `cp` parameter and can be changed for other atmospheres
   > Correct! `cp` is the specific heat capacity at constant pressure, defined in `[namelist:planet]`, and can be modified to represent non-Earth atmospheres.
   1. [ ] It is calculated automatically from the gas constant `rd` and cannot be set directly
   > Try again! `cp` is set directly as its own namelist parameter, independently of `rd`.
   1. [ ] It only matters for configurations that include an ocean
   > Try again! The idealised configurations in this practical are atmosphere-only; `cp` describes the heat capacity of the atmosphere itself.

   ## Which namelist section would you look in to change the planet's gravity, and where would you look to change the amount of CO2 in the atmosphere?
   > hint: One section groups physical constants of the planet, the other groups atmospheric composition.
   1. [ ] Both are set in the same `[namelist:planet]` section
   > Try again! Gravity is a planetary constant, but CO2 concentration is configured elsewhere.
   1. [x] Gravity is set in `[namelist:planet]`, while CO2 concentration is set in `[namelist:radiative_gases]`
   > Correct! Planetary constants such as `gravity`, `cp`, `omega` and `radius` belong to `[namelist:planet]`, whereas gas concentrations such as `co2_mix_ratio` belong to `[namelist:radiative_gases]`.
   1. [ ] Both are set in `[namelist:radiative_gases]`
   > Try again! Gravity is not a radiative gas property; it belongs in `[namelist:planet]`.
   1. [ ] Gravity is set in `[namelist:radiative_gases]`, while CO2 concentration is set in `[namelist:planet]`
   > Try again! This is the wrong way round - gravity is a planetary constant, CO2 concentration is a radiative gas property.