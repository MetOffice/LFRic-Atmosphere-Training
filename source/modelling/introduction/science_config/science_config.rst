**********************
Science Configurations
**********************
A science configuration specifies a set of scientific and numerical settings for a single component model or a combination of component models. These settings include, for example, physical parameterization, numerical schemes and model coupling choices.

Below diagram illustartes the Regional Atmosphere and Land (RAL) development cycle.  RAL defines the set of science configurations for the atmosphere and land used in all regional models by the Met Office and Momentum partners across the globe

.. figure:: /_static/RAL.png
   :width: 650px
   :alt: RAL cycle configuration

   RAL development cycle


Science configurations are tested and evaluated across a set of spatial resolutions and temporal scales - e.g. Numerical Weather Prediction (NWP) to climate - to ensure they meet the required standards for accuracy and reliability. Once the evaluation is complete, the configuration is:

1. **Frozen**, so that the scientific settings are fixed
2. **Versioned and numbered**, enabling clear identification and traceability 
3. **Released** as a standard package for use in modelling systems for research and operational purposes.

Released science configurations form the scientific foundation of prediction and projection systems. Dedicated workflows are constructed around these configurations using the Momentum technical infrastructure. These workflows support activities such as:

* Software compilation and execution
* Data assimilation for forecast systems
* Post-processing and analysis of model output

By using the same science configuration within different workflows, the Momentum framework enables seamless modelling across a variety of prediction and projection systems.

Once a science configuration is defined, it can be used for different systems across the Momentum Partnership. For example:

* For **CMIP6**, **GC3.1** was used in **UKESM1.1** and **GAL7.1** was used in **KACE**

* The **GC4** science configuration is used for several operational NWP systems across the Momentum Partnership e.g. MOGREPS, ACCESS-S1, and NCUM.
* **TO DO for Fourough** 
* These details for limited area model configuration can be added from slide 10 of Module 5 which is there in this link https://metoffice.sharepoint.com/:p:/r/sites/metofficengmsprogrammeext/NGUX/training/Module%205/NGUX_Module-5_session-1_15Jan2026.pptx?d=w5b397e2c487c42d8a2b734430d92e8b5&csf=1&web=1&e=QYwH8L*

* *Regional...*