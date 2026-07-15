***********************************************
Experiments with the Extraterrestrial CRM Suite
***********************************************

We will now run a couple of simulations using the ``u-dz791`` suite. This suite
is designed to model convection in hydrogen-rich atmospheres of other planets
in a highly simplified setup - the default configuration uses only the
dynamical core (GungHo).


Key features
------------
  * The dynamical core only. All parameterizations are switched off.
  * No rotation.
  * Hydrogen-dominated atmosphere. In the dynamics-only setup this is
    controlled via the gas constants: isobaric heat capacity ``cp=14300`` and
    the dry gas constant ``rd=4124.00``.
  * Initial temperature profile: isothermal (uses a branch for a corrected
    procedure - see ``dependencies.yaml``).
  * Initial vapour profile: step-wise profile with more vapour in the upper
    atmosphere to sustain compositional convection.
  * Initial wind profile: zero.


Science motivation
------------------

In the context of hydrogen-rich atmospheres, we are particularly keen to
explore how convection works in a presence of a compositional gradient, e.g. a
large vertical gradient of water vapour.

.. admonition:: Why is this interesting?

   Beyond Earth, a particularly interesting case is moist convection in
   hydrogen-dominated atmospheres. Unlike on Earth, where the mean molecular
   weight of the background gas surpasses that of water vapour,
   hydrogen-dominated atmospheres exhibit a stabilising molecular-weight
   gradient, as the condensable has a greater mean molecular weight than that
   of the background gas (`Ledoux, 1947 <https://doi.org/10.1086/144905>`_).
   Consequently, in atmospheres with non-dilute amounts of the condensable
   (>10% by mass; see e.g. `Pierrehumbert & Ding, 2016
   <https://doi.org/10.1098/rspa.2016.0107>`_), the background temperature
   gradient can no longer be solely relied on to predict convective stability.
   This effect is not as important for convection on Earth since water vapour
   only contributes up to a few percent by mass, hence lying comfortably in the
   dilute regime.


Suggested experiments
---------------------

The following practical exercises are suggested to explore the idealised setup
further. You will need to use what you learned in the running and navigating
exercises to edit and run the experiments. For analysis, you can use what you
learnt in the visualisation exercises.

.. toctree::
   :maxdepth: 1
   :caption: Contents

   rotation.rst
   back_to_earth.rst
   init_perturb.rst


.. admonition:: Example from previous studies: changing the water vapour profile

   `Habib & Pierrehumbert (2024) <https://doi.org/10.3847/1538-4357/ad04e2>`_
   use another cloud-resolving model and find that destabilizing mean molecular
   weight gradients can lead to compositional convection in otherwise thermally
   stable atmospheres. They test this using high-resolution non-condensing
   simulations for a range of background compositions and thermal profiles.
   LFRic allows us to repeat their experiments by changing the background
   composition (gas constants) and the initial profile of water vapour. Talk to
   Alex Corbett if you are interested.

.. Note::

   If you decide to test your own experiment with a code or configuration
   change, be ready to do lots of debugging! If you want an example which is
   tried and tested, use the suggested examples above.
