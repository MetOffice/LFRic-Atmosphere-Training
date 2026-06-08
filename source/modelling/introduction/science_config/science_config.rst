**********************
Science Configurations
**********************
A science configuration specifies a set of scientific and numerical
settings for a single component model or a combination of component
models. These settings include, for example, physical
parameterization, numerical schemes and model coupling choices.

Science configurations are tested and evaluated across a set of
spatial resolutions and temporal scales - e.g. Numerical Weather
Prediction (NWP) to climate - to ensure they meet the required
standards for accuracy and reliability. Once the evaluation is
complete, the configuration is:

1. **Frozen**, so that the scientific settings are fixed
2. **Versioned and numbered**, enabling clear identification and
   traceability
3. **Released** as a standard package for use in modelling systems
   for research and operational purposes.

Released science configurations form the scientific foundation of
prediction and projection systems. Dedicated workflows are
constructed around these configurations using the Momentum technical
infrastructure. These workflows support activities such as:

* Software compilation and execution
* Data assimilation for forecast systems
* Post-processing and analysis of model output

By using the same science configuration within different workflows,
the Momentum framework enables seamless modelling across a variety of
prediction and projection systems.

Once a science configuration is defined, it can be used for different
systems across the Momentum Partnership. For example:

* For **CMIP6**, **GC3.1** was used in **UKESM1.1** and **GAL7.1**
  was used in **KACE**

* The **GC4** science configuration is used for several operational
  NWP systems across the Momentum Partnership e.g. MOGREPS,
  ACCESS-S1, and NCUM.

Regional (Limited Area) Science Configurations
----------------------------------------------
In addition to global configurations, the Momentum framework also
defines science configurations for regional (limited area) models,
focusing on the atmosphere and land components.
These are known as Regional Atmosphere and Land (RAL) configurations.

A RAL configuration is a set of science configurations for the
atmosphere and land components that is designed for use in regional
models. These configurations support both:

* Numerical Weather Prediction (NWP)
* Regional climate simulations
* Regional coupled simulations


RAL configurations ensure that regional models across the Momentum
Partnership share a consistent scientific basis, in the same way that
global configurations (e.g. GC and GAL) do.

RAL Development and Lifecycle
+++++++++++++++++++++++++++++
RAL configurations follow the same principles as other science
configurations:

* They are developed, tested, and evaluated across multiple systems
  and regions
* Evidence is gathered to assess performance across a range of
  applications and scales
* Once validated, they are frozen, versioned, and released for
  operational and research use

Within the Momentum Partnership, this process is coordinated by the
RMED (Regional Model Evaluation and Development) activity, which:

* Coordinates package testing across partners
* Builds the scientific evidence base through evaluation
* Delivers new RAL configurations for use across the partnership

At any given time:

* One RAL version is operationally in use
* The next RAL version is under development and evaluation

The diagram below illustrates the development process for regional
modelling systems within the Momentum framework.

.. _fig-developing-regional-models:

.. figure:: /_static/develop-regional-models.png
   :width: 650px
   :alt: Regional Model Evaluation and Development

   RMED coordinates the RAL process by working with many other groups
   from across the office and Momentum partnership to identify the
   improvement needs, evaluate new science configurations and deliver
   the new RAL​

Versioning and Operational Use
++++++++++++++++++++++++++++++

RAL configurations are versioned in a similar way to global
configurations. RALn denotes the current released version.
For example:

* RAL3 is the current operational configuration (as of January 2026)
* It is used in operational forecasting systems such as the UKV
* It unified previously separate tropical and mid-latitude
  configurations into a single framework
* It has also been operationalised by partners including National
  Centre for Medium Range Weather Forecasting (NCMRWF) and Centre for
  Climate Research Singapore (CCRS)

Future development will lead to the next release (e.g. RAL4),
continuing the cycle of evaluation, improvement, and operational
deployment.

