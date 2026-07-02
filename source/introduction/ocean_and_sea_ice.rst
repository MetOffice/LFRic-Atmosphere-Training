.. _ocean-and-sea-ice:

Ocean and Sea Ice
=================

In Momentum configurations, the ocean and sea-ice components provide the evolving lower boundary beneath the atmosphere over the oceans and polar regions.

The marine physical models used in current Momentum training are NEMO for the ocean and SI3 for sea ice. They sit alongside other components such as JULES.

Why marine coupling matters
---------------------------

Ocean and sea-ice processes occur at the interface between the atmosphere and the marine environment. They control how heat, freshwater, salt, carbon, and momentum are stored, transported, and exchanged with the atmosphere.

The ocean evolves more slowly than the atmosphere, but it has a long memory. Sea-surface temperature, ocean heat content, salinity, currents, and surface mixing can all affect surface fluxes, evaporation, boundary-layer structure, clouds, precipitation, tropical variability, and extratropical weather systems.

Sea ice is also an active part of the lower boundary. It changes surface albedo, insulates the ocean from the atmosphere, modifies exchanges of heat and moisture, and changes freshwater and salt budgets as it forms, melts, and moves. In polar regions, the coupled atmosphere-ocean-sea-ice state can strongly affect both weather forecasts and climate simulations.

What NEMO represents
--------------------

NEMO, the Nucleus for European Modelling of the Ocean, is the ocean modelling framework used for global and regional marine configurations. It represents the evolving three-dimensional ocean state, including currents, temperature, salinity, sea-surface height, and ocean mixing.

NEMO is driven by surface forcing and boundary information such as wind stress, heat fluxes, freshwater fluxes, river input, sea-ice interaction, and lateral boundary conditions in regional domains.

Using this information, NEMO calculates processes including:

* ocean circulation and currents,
* sea-surface temperature and salinity,
* transport of heat, freshwater, salt, and tracers,
* vertical mixing and mixed-layer evolution,
* interaction with coastlines, bathymetry, and ocean topography,
* regional shelf-sea and global ocean behaviour.

What SI3 represents
-------------------

SI3, the Sea Ice modelling Integrated Initiative, is the native sea-ice engine in NEMO. It represents the growth, melt, drift, deformation, and thermodynamic state of sea ice.

Sea ice is not a uniform surface. Within a model grid cell, there may be open water, thin ice, thick ice, snow-covered ice, ridged ice, and melt ponds. SI3 represents this mixture using sub-grid categories rather than trying to model every individual floe and lead.

SI3 calculates processes including:

* sea-ice concentration and thickness,
* snow depth on sea ice,
* sea-ice growth and melt at the top and base,
* sea-ice movement under winds and ocean currents,
* deformation, ridging, and opening of leads,
* melt ponds and surface albedo effects.

Coupling with the atmosphere
----------------------------

In coupled Momentum systems, NEMO and SI3 exchange surface information with the atmosphere through the coupler. The atmosphere supplies near-surface winds, heat fluxes, freshwater fluxes, and radiative forcing. The marine components return sea-surface temperature, sea-ice area, ice and snow state, and surface properties that affect fluxes back to the atmosphere.

The important point for this LFRic Atmosphere training is that the ocean and sea ice are active model components, not static boundary datasets. Their initial conditions, coupling choices, surface states, and configuration details can all influence atmospheric behaviour, especially for longer forecasts, seasonal prediction, climate simulations, and polar applications.

Marine configurations
---------------------

The Joint Marine Modelling Programme develops two families of marine configurations used in Met Office and partner systems:

Global Ocean and Sea Ice configurations
   GOSI configurations are global NEMO-SI3 configurations used in climate, Earth system, seasonal-prediction, and coupled weather-forecast systems. GOSI9 is a traceable hierarchy of global ocean and sea-ice models at 1 deg, 1/4 deg, and 1/12 deg horizontal resolution, all using 75 vertical levels.
Coastal Ocean configurations
   CO configurations are regional shelf-sea configurations. The North West European Shelf configurations include AMM7 at about 7 km resolution and AMM15 at about 1.5 km resolution, both with 51 vertical levels.

Useful detail to recognise
--------------------------

Learners do not need the full numerical detail at this stage, but it is useful to recognise two ideas that appear repeatedly in marine modelling:

Grids
   Ocean models use their own horizontal and vertical grids. NEMO global configurations commonly use ORCA tripolar grids, which avoid placing a singular grid point in the Arctic Ocean.
Parameterisations
   Even high-resolution ocean and sea-ice models cannot resolve all important processes. Ocean eddies, vertical turbulence, ice floes, leads, ridges, and ice-thickness variation must often be parameterised.

.. _fig-intro-nemo-orca-mesh:

.. figure:: /_static/1/nemo_orca_mesh_conception.png
   :width: 650px
   :alt: ORCA tripolar ocean mesh over the Northern Hemisphere, with embedded ellipses and computed normals used to avoid an Arctic Ocean pole singularity

   ORCA mesh conception used by NEMO global ocean configurations. Source: `NEMO ocean engine reference manual <https://doi.org/10.5281/zenodo.6334656>`_, Figure 15.1.

.. _fig-intro-si3-thickness-categories:

.. figure:: /_static/1/si3_ice_thickness_categories.png
   :width: 650px
   :alt: SI3 schematic showing a sea-ice grid cell divided into open water and multiple ice-thickness categories with different ice thickness, snow depth, and concentration

   Representation of the sea-ice pack using multiple ice-thickness categories in SI3. Source: `SI3: Sea Ice modelling Integrated Initiative - the NEMO sea ice engine <https://doi.org/10.5281/zenodo.7534900>`_, Figure 1.1.

Further resources
-----------------

The following references provide the scientific and technical background:

* `NEMO ocean engine reference manual <https://doi.org/10.5281/zenodo.6334656>`_ and `NEMO citation guidance <https://sites.nemo-ocean.io/user-guide/cite.html>`_.
* `SI3: Sea Ice modelling Integrated Initiative - the NEMO sea ice engine <https://doi.org/10.5281/zenodo.7534900>`_.
* Guiavarc'h et al. (2025), `GOSI9: UK Global Ocean and Sea Ice configurations <https://doi.org/10.5194/gmd-18-377-2025>`_.
* Blockley et al. (2024), `The sea ice component of GC5: coupling SI3 to HadGEM3 using conductive fluxes <https://doi.org/10.5194/gmd-17-6799-2024>`_.
* O'Dea et al. (2017), `The CO5 configuration of the 7 km Atlantic Margin Model: large-scale biases and sensitivity to forcing, physics options and vertical resolution <https://doi.org/10.5194/gmd-10-2947-2017>`_.
* Graham et al. (2018), `AMM15: a new high-resolution NEMO configuration for operational simulation of the European north-west shelf <https://doi.org/10.5194/gmd-11-681-2018>`_.
* `Joint Marine Modelling Programme repositories <https://github.com/JMMP-Group>`_.
