Introduction to Global Coupled (GC) configurations
==================================================

The Met Office develops science configurations for their numerical models. In GC configurations the atmosphere and ocean are coupled and feedback to each other. Within Met Office science configurations, there are four component   models that make up a GC configuration. Each GC configuration is then split into a GAL and a GOSI configuration,   which are coupled by the OASIS coupler.

.. image:: /_static/components.png
   :width: 650px

A science configuration is frozen package of mature science settings which has been rigourously tested across      seamless timescales from NWP to climate. The GC configuration is then used for different systems at the Met Office and across the Parntership. For example:

* **GC3.1** was implemented in **UKESM1.1** for CMIP6
* **GC4** was implmented for **PS45** (Met Offices operational suite for NWP)
* **GC4** was implmented for **ACCESS-S1** (the Bureau of Meteorology's seasonal system)

This means that the same science settings are used for all timescales and resolutions.

.. image:: /_static/seamless_modelling.png
   :width: 650px

Each GC configuration goes through an approximate 2-year development cycle, where it is tested for key systematic  errors. The configuration has individual component testing and package testting, with continuous evaluation and    verification.

.. admonition:: Interested in getting involved in evalutaion of science configurations?

   The 2-year development and evaluation cycle involves scientists from across the Patnership, with different      centres bringing different expertise. One way to get involved is to join PEGs or CoGs. PEGs are 'priority          evaluation groups' which focus on a few key systemic biases and this is a great way to become involved. If         interested find the PEG or CoG lead on the GMED MOSRS pages and contact them. Or contact um_collaboration@         metoffice.gov.uk.

.. image:: /_static/seamless_dev_cycle.png
   :width: 650px

.. admonition:: Task: Explore MOSRS, GitHub and wiki tickets

   Go to the Met Office Science Repository Service and explore the Global Model Evaluation and Development pages.  Where is the documentation stored, how are configurations released and what is the difference between a            configuration and a UM/LFRic version.

In July 2022, the final UM-based GC configuration was released, 'GC5', before the implementation of the LFRic      atmospheric model into GC configurations.

Following GC5-UM, there was a project assocaited with the NGMS programme to develop a GC5-LFRic science            configuration. This was a like-for-like LFRic version of GC5, for purely research purposes. The GC5-LFRic          configuration is then taken as the baseline for GC6 development, which will be the first operational use of LFRic  in a science configuration at the Met Office and across the Partnership. GC6 will be implmented in PS49 and in     UKESM3 for CMIP8.
