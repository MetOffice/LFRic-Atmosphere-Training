What is an idealised configuration?
===================================

Here, we use the term 'idealised' to mean a minimal configuration of LFRic-Atmosphere that is typically used in research applications.


Idealised convection modelling
------------------------------

We will focus on the so-called the cloud-resolving model (CRM) configuration, which uses:

* Cartesian-geometry spatial grid
* double periodic lateral boundary conditions
* flat uniform surface
* prescribed domain-wide forcings
* minimal LFRic physics setup

This configuration is used for studying convective processes on Earth and other planets.

In the practical, we will use a dynamics-only configuration in ``u-dz791``.
This suite is set up for simulating thermo-compositional convection in hydrogen-rich atmospheres.

.. _fig-crm-examples:

.. figure:: /_static/crm-examples.png
   :width: 500px
   :align: center
   :alt: 3D plots of cloud fraction for four different scenarios.

   An example of a CRM setup. 3D plots of cloud fraction for four different scenarios.


Other idealised and extraterrestrial configurations
---------------------------------------------------

There are many other configurations of LFRic-Atmosphere that can be categorised as 'idealised', to name but a few:

* a global aquaplanet configuration, i.e. Earth without continents (and a slab ocean),
* temperature or wind forcing test cases (e.g., the Held-Suarez test) for Earth and other planets,
* a setup with radiative transfer and idealised chemistry for hot extrasolar gas giants.
