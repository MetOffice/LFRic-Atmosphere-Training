.. _land-surface-and-jules:

Land Surface and JULES
======================

LFRic Atmosphere is one component of the wider Momentum Framework. In coupled
or atmosphere-land configurations it exchanges information with other
components, including the land surface, ocean, and sea ice. The land surface is
one of the most direct couplings because it supplies the lower boundary
conditions seen by the atmosphere and responds to atmospheric forcing in
return.

The land surface is represented by JULES: the Joint UK Land Environment
Simulator. JULES is the Met Office community land surface model used in weather
prediction and climate modelling. It represents exchanges of momentum, energy,
water, and carbon between the surface and the atmosphere.

.. _fig-intro-jules-surface-processes:

.. figure:: /_static/1/jules_surface_processes.png
   :width: 650px
   :alt: JULES surface process schematic showing heat, water, carbon, momentum, radiation, precipitation, evaporation, and different land surface types

   JULES represents land-atmosphere exchanges across vegetated, urban, wetland,
   snow-covered, and bare-soil surfaces. Source: `JULES website
   <https://jules.jchmr.org/about>`_, `JULES model description diagram
   <https://jules.jchmr.org/sites/default/files/2023-06/jules-model-description.png>`_.

Why land coupling matters
-------------------------

Land-surface processes occur at the interface between the land and the
atmosphere. They control how incoming radiation and precipitation are
partitioned into surface temperature, sensible and latent heat fluxes, runoff,
infiltration, soil moisture, snow, vegetation growth, and carbon exchange.

This matters for both numerical weather prediction and climate modelling. The
land surface can act as a source or sink of energy, water, carbon, and
momentum, so errors in the land state can feed back onto boundary-layer
development, clouds, precipitation, near-surface temperature, wind, drought,
flooding, wildfire risk, and crop impacts.

What JULES represents
---------------------

JULES is driven by atmospheric and surface information such as air temperature,
precipitation, radiation, wind, humidity, pressure, surface-type fractions,
snow state, canopy water, leaf area index, canopy height, soil moisture, soil
temperature, and soil carbon.

Using this information, JULES calculates processes including:

* surface albedo and radiation interactions,
* surface energy balance, turbulent fluxes, and momentum exchange,
* snow accumulation, snowmelt, sublimation, and snow insulation,
* runoff, infiltration, vertical soil-water flow, and river routing,
* soil temperature, soil moisture, freezing and thawing,
* transpiration, photosynthesis, vegetation dynamics, crops, and soil carbon.

By default, the land surface is represented using multiple surface types,
including vegetated and non-vegetated tiles, and four soil layers. This tiling
allows a grid box to contain different land covers, such as trees, grasses,
crops, urban surfaces, bare soil, water, and snow.

Coupling with the atmosphere
----------------------------

The atmosphere provides JULES with near-surface meteorology, precipitation, and
radiation. JULES returns lower-boundary information to the atmosphere,
including surface temperature, surface fluxes of heat, moisture, momentum and
carbon, roughness, albedo, soil moisture influence, snow influence, and
vegetation influence.

Some of these exchanges vary on fast timescales. To capture surface fluxes
correctly while keeping model timesteps practical, the surface is coupled
implicitly to the atmosphere. Slower diffusive processes in the soil can be
coupled explicitly to the surface.

For this LFRic Atmosphere training, the important point is that JULES is an
active model component, not just a static boundary dataset. Land initial
conditions, surface-type fractions, snow, soil moisture, vegetation state, and
coupling choices can all be first-order causes of atmospheric behaviour.

Further resources
-----------------

The JULES model description papers provide the scientific background:

* M. J. Best et al. (2011), `The Joint UK Land Environment Simulator (JULES),
        model description, Part 1: energy and water fluxes
        <https://doi.org/10.5194/gmd-4-677-2011>`_.
* D. B. Clark et al. (2011), `The Joint UK Land Environment Simulator (JULES),
        model description, Part 2: carbon fluxes and vegetation
        <https://doi.org/10.5194/gmd-4-701-2011>`_.

The `JULES user documentation <https://metoffice.github.io/jules/latest/>`_ and
`JULES external website <http://jules.jchmr.org/>`_ provide further details.
