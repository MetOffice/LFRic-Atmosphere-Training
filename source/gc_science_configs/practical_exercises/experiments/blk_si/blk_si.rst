******************
Make sea ice black
******************

* create JULES branch - See: Working Practices: Create a ticket, Working Practices: Create a branch

* adjust hard coded values for the albedo in ``src/control/shared/jules_sea_seaice_mod.F90``
  (set ``calbicev_cice``, ``albicei_cice``, ``albsnowv_cice``, ``albsnowi_cice``, ``albpondv_cice``,               ``albpondi_cice``, ``dalb_mlt_cice``, ``dalb_mlts_v_cice`` and ``dalb_mlts_i_cice`` to 0.0)

* point your LFRic build setup in ``paramerts.sh`` to you JULES branch and adjust your workflow to use your        adjusted model build

* build the model and run your experiment

.. code-block:: fortran
   :caption: src/control/shared/jules_sea_seaice_mod.F90
   :emphasize-lines: 2, 4, 6, 8, 10, 12

   ! Parameters for 4-band CICE albedo scheme used within JULES:
        albicev_cice = 0.00,                                                       &
          ! Sea ice albedo (visible)
        albicei_cice = 0.00,                                                       &
          ! Sea ice albedo (near-infrared)
        albsnowv_cice = 0.00,                                                      &
          ! Snow albedo (visible)
        albsnowi_cice = 0.00,                                                      &
          ! Snow albedo (near-infrared)
        albpondv_cice = 0.00,                                                      &
          ! Meltpond albedo (visible)
        albpondi_cice = 0.00,                                                      &
          ! Meltpond albedo (near-infrared)
        ahmax = 0.3,                                                               &
          ! Sea ice albedo in CICE multi-band scheme is constant above this
          ! thickness (metres)
        dalb_mlt_cice = -0.075,                                                    &
