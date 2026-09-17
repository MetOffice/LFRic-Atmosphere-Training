.. _land-surface-and-jules:

Land Surface and JULES
======================

LFRic Atmosphere is part of a wider Momentum Framework. In coupled or
atmosphere-land configurations, it exchanges information with other
components, including the land surface, ocean, and sea ice. The land
surface supplies fluxes of momentum, heat, moisture, and carbon to the
atmosphere, and responds to atmospheric forcing in return.

The land surface is represented by `JULES <https://github.com/MetOffice/jules>`_, the Joint UK Land Environment
Simulator. JULES can run as a standalone model using observed forcing data
or be coupled to an atmospheric global circulation model for weather
prediction and climate modelling.

JULES is driven by atmospheric and surface information such as air
temperature, precipitation, radiation, wind, humidity, pressure, surface-type
fractions, snow state, canopy water, leaf area index, canopy height, soil
moisture, soil temperature, and soil carbon.

JULES uses these inputs to simulate processes such as:

* Surface albedo and radiation exchange,
* Surface energy balance, turbulent fluxes, and momentum transfer,
* Snow accumulation, melt, sublimation, and insulation,
* Runoff, infiltration, soil-water movement, and river routing,
* Soil temperature, soil moisture, freezing, and thawing,
* Transpiration, photosynthesis, vegetation dynamics, crop processes, and soil
  carbon.

The land surface is represented using multiple surface types, including
vegetated and non-vegetated tiles, and multiple soil layers. By default, the
surface has nine surface tiles in each grid box, five of which are vegetated
(broadleaf trees, needleleaf trees, C3 (temperate) grass, C4 (tropical) grass
and shrubs), and four are non-vegetation types (urban, inland water, bare soil
and land ice). Each JULES surface tile calculates its own fluxes of heat,
moisture and momentum, derived from bulk aerodynamic formulae through
functions of specific humidity, air temperature, wind speed and available
energy. These are averaged and weighted by the fractional cover of each
surface tile over the grid box to produce grid box mean components of the
surface energy balance.

.. _fig-intro-jules-surface-processes:

.. figure:: /_static/1/jules_surface_processes.png
   :width: 650px
   :alt: JULES surface process schematic showing heat, water, carbon, momentum, radiation, precipitation, evaporation, and different land surface types

   JULES represents land-atmosphere exchanges across vegetated, urban, wetland,
   snow-covered, and bare-soil surfaces. Source: `JULES website
   <https://jules.jchmr.org/about>`_, `JULES model description diagram
   <https://jules.jchmr.org/sites/default/files/2023-06/jules-model-description.png>`_.

JULES calculates the exchanges of energy and momentum between the surface and
the atmosphere by representing a range of surface and sub-surface processes,
including snow, surface and soil hydrology, and vegetation physiology and
dynamics. JULES currently uses a tiled model to represent surface heterogeneity
with separate energy and water fluxes computed for each surface type within
an atmospheric grid box.



For this LFRic Atmosphere training, the important point is that JULES is an
active model component, not just a static boundary dataset. Land initial
conditions, surface-type fractions, snow, soil moisture, vegetation state, and
coupling choices can all impact atmospheric behaviour.

Further resources
-----------------

The JULES model description papers provide the scientific background:

* Best et al. (2011) [Best_et_al_2011]_, model description Part 1: energy and
  water fluxes.
* Clark et al. (2011) [Clark_et_al_2011]_, model description Part 2: carbon
  fluxes and vegetation dynamics.

See also:

* Rumbold et al. (2023) [Rumbold_et_al_2023]_, section 2.1, for further scheme
  description.


The `JULES user documentation <https://metoffice.github.io/jules/latest/>`_ and
`JULES external website <http://jules.jchmr.org/>`_ provide further details.
