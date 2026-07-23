.. The [namelist:planet] excerpt used by the Earth rotation experiment.
.. To use it: .. include:: /include/snippets/planet-namelist.rst

.. code-block:: ini
   :caption: app/lfric_atm/rose-app.conf
   :emphasize-lines: 4

   [namelist:planet]
   cp=1005.0
   gravity=9.80665
   omega=3.646058E-5
   p_zero=100000.0
   radius=6371229.0
   rd=287.05
   scaling_factor=1.0
