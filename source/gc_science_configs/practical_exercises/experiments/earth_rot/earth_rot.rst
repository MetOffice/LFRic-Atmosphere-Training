********************************
Reduce the rotation of the Earth
********************************
* cd ``app/lfric_atm``
* open ``rose-app-conf``
* change ``omega``

.. code-block:: fortran
   :caption: trunk/app/lfric_atm/rose-app.conf
   :emphasize-lines: 4

   [namelist:planet]
    cp=1005.0
    gravity=9.80665
    omega=7.292116E-5
    p_zero=100000.0
    radius=6371229.0
    rd=287.05
    scaling_factor=1.0