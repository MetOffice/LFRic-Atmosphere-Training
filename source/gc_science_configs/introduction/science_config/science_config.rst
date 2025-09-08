**********************
Science Configurations
**********************

The GAL and GOSI models are coupled to form the GC configuration. This is done via the *OASIS* coupler. OASIS allows for the exchange of information between the different components of the model at varied resolutions and timescales, known as *inter-model* coupling. This alternative approach is necessary because ocean and sea ice processes typically evolve on longer timescales and larger spatial scales than atmospheric and land processes meaning that they cannot efficiently be combined in the same executable.

More specifically, a science configuration is when a defined version of each of the core models is combined together with a set of science settings, such as parameterisations and resolutions, to create a complete model system. The science configuration is then tested and evaluated to ensure that it meets the required standards for accuracy and reliability. Once this is done, the configuration is frozen, numbered, and released as a package that can be used for research and operational purposes; this is illustrated in the diagram below.

.. image:: /_static/components.png
   :width: 650px

Once a GC configuration is defined, it can be used for different systems at the Met Office and across the Momentum partnership. For example:

* **GC3.1** was implemented in **UKESM1.1** for CMIP6

* **GC4** was implemented for **PS45** (Met Office's operational suite for NWP)

* **GC4** was implemented for **ACCESS-S1** (the Bureau of Meteorology's seasonal system)