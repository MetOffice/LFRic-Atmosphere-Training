Introduction to Global Coupled (GC) configurations
==================================================

The Met Office develops science configurations for their numerical models. In GC configurations, the atmosphere and ocean are coupled and feedback to each other. Within these Met Office science configurations, there are four component models that make up the GC configuration. Each GC configuration is then split into a GAL and a GOSI configuration, which are coupled by the OASIS coupler as shown below.

.. image:: /_static/components.png
   :width: 650px

A science configuration is a frozen package of mature science settings which has been rigorously tested across seamless timescales from NWP to climate. Here, the term seamless refers to the same science settings being used across all timescales and resolutions. The GC configuration is then used for different systems at the Met Office and across the Partnership. For example:

* **GC3.1** was implemented in **UKESM1.1** for CMIP6
* **GC4** was implemented for **PS45** (Met Offices operational suite for NWP)
* **GC4** was implemented for **ACCESS-S1** (the Bureau of Meteorology's seasonal system)

.. image:: /_static/seamless_modelling.png
   :width: 650px

Each GC configuration goes through an approximate 2-year development cycle, where it is tested for key systematic errors. The configuration has individual component testing and package testing, with continuous evaluation and verification.

.. admonition:: Interested in getting involved in evaluation of science configurations?

   The 2-year development and evaluation cycle involves scientists from across the Partnership, utilising the varied expertise across the different centres. One way to get involved is by joining a PEG (Priority Evaluation Group) or a CoG (Collaboration Group). PEGs focus on a few key systemic biases making them a great way to become involved. If interested, find the PEG or CoG lead on the GMED MOSRS pages and contact them, or you can contact um_collaboration@metoffice.gov.uk.

.. image:: /_static/seamless_dev_cycle.png
   :width: 650px

.. admonition:: Task: Explore MOSRS, GitHub and Wiki tickets

   Visit the Met Office Science Repository Service (MOSRS) and navigate to the Global Model Evaluation and Development (GMED) pages. Investigate the following:

   * Where the documentation for science configurations is stored.
   * The process of releasing configurations.
   * The differences between configurations and how they are developed.
   * The difference between the UM and LFRic versions of the GC configurations.
   * How wiki tickets are used to track and manage tasks related to science configurations.

In July 2022, the final UM-based GC configuration was released, 'GC5', before the implementation of the LFRic atmospheric model into GC configurations. 

Following GC5-UM, there was a project associated with the NGMS programme to develop a GC5-LFRic science configuration. This was a like-for-like LFRic version of GC5, for purely research and validation purposes. The GC5-LFRic configuration is then taken as the baseline for GC6 development, which will be the first operational use of LFRic in a science configuration at the Met Office and across the Partnership. GC6 will be implemented in PS49 and in UKESM3 for CMIP8.