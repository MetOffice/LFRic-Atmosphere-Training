.. The [namelist:radiative_gases] excerpt used by the CO2 experiment.
.. To use it: .. include:: /include/snippets/radiative-gases-namelist.rst

.. code-block:: ini
   :caption: app/lfric_atm/rose-app.conf
   :emphasize-lines: 8

   [namelist:radiative_gases]
   ch4_mix_ratio=9.8200e-07
   ch4_rad_opt='constant'
   !!co2_clim_fcg_levls=
   !!co2_clim_fcg_nyears=
   !!co2_clim_fcg_rates=
   !!co2_clim_fcg_years=
   co2_mix_ratio=5.6062e-04
   co2_rad_opt='constant'
