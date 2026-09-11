.. _rivers:

Rivers
======

In coupled models, rivers are an important component of the water
cycle and are important to provide freshwater input into the oceans at the
river mouths and also to maintain water conservation.

The Momentum framework is unable to compile the river component within the
atmosphere and land executable (due to the LFRic cube-sphere grid being
incompatible with the rivers latitude-longitude grid). Instead the river
component is compiled into a separate executable and passes information
from/to the atmosphere and to the ocean via the :term:`OASIS3-MCT` coupler.

The river model used in Momentum is the Total Runoff Integrating Pathways
(:term:`TRIP`) model developed at the NASA/Goddard Space Flight Center
[Oki_and_Sud_1998]_.

In the Momentum framework :term:`JULES` (embedded within LFRic) handles the
soil moisture calculations and determines the amount of surface runoff and
sub-surface runoff. These two 2D fields are passed to the OASIS3-MCT coupler
which regrids these fields to the TRIP grid and passes them to the TRIP river
model. The TRIP river model then passes this water through the pre-determined
route of the rivers through the TRIP grid until the water arrives at the river
mouth. Then this 2D field of river outflows is converted to a 1D array where
each river is an index in that array, roughly in order of climatological
outflow (so the Amazon is river number one). This 1D array is passed through
OASIS3-MCT to NEMO without any regridding. NEMO uses a river number ancillary
file to determine which grid boxes recieve the river outflow for each river and
uses this to convert the 1D river outflow to a 2D river outflow field. This
fresh water then gets put into the ocean, raising local sea surface heights and
reducing salinity.

However not all rivers end up at the ocean. Some rivers arrive into lakes
with no outflow point; or dry basins and simply evaporate away. These points
are classed as inland basin flow points. In Momentum we transfer river water
arriving into an inland basin flow point through the OASIS3-MCT coupler back
to JULES (embedded within LFRic). JULES then adds this water back into soil
moisture.

.. _fig-coupling_schematic:

.. figure:: /_static/1/coupling_schematic.png
   :width: 650px
   :alt: Schematic showing the three submodels (Atmosphere, Ocean and Rivers)
   and what they pass through the OASIS3-MCT coupler.

   Schematic showing the three submodels that are run as separate executables
   (Atmosphere, Ocean and Rivers) and what they pass through the OASIS3-MCT coupler.
