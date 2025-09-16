***************************************************
Coupling remove influence of evaporation from ocean
***************************************************
* cd ``app/coupled/file``
* open ``namcouple``
* Observe namcouple file - what is it setting?
* adjust definition of coupling for ``lf_evap``

.. code-block:: text
   :caption: trunk/app/coupled/file/namcouple
   :emphasize-lines: 1, 8

   lf_evap OTotEvap 466 3600 2 atmos_restart.nc   EXPORTED
    24576 1 1442 1207 lfric tor1 SEQ=+2
    P  0  P  2
    #
    MAPPING
    ##
    rmp_lfric_to_tor1_nomask_CONSERVE_DSTAREA.nc
    0.0 0
    #

.. note:: Note on the namcouple file......