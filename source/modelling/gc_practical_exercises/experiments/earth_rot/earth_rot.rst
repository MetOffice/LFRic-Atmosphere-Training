*********************************
Halving the rotation of the Earth
*********************************

In this experiment, you will halve the rotation rate of the Earth to observe
its effect on the model climate.

Step 1: Navigate to the application directory
=============================================
Start by changing into the ``lfric_atm`` application directory:

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console

         cd app/lfric_atm

   .. tab-item:: Monsoon

      .. code-block:: console

         cd app/lfric_atm

Step 2: Edit the configuration file
===================================
1. Open ``rose-app.conf`` in a text editor of your choice.
2. Search for the ``omega`` key (located under the ``[namelist:planet]``
   section).
3. Change the value from ``7.292116E-5`` (Earth's rotation rate) to ``3.646058E-5``
   (half of Earth's rotation rate), as highlighted below.

.. tab-set::

   .. tab-item:: Met Office

      .. code-block:: console
         :caption: trunk/app/lfric_atm/rose-app.conf
         :emphasize-lines: 4

         [namelist:planet]
         cp=1005.0
         gravity=9.80665
         omega=3.646058E-5
         p_zero=100000.0
         radius=6371229.0
         rd=287.05
         scaling_factor=1.0

   .. tab-item:: Monsoon

      .. code-block:: console
         :caption: trunk/app/lfric_atm/rose-app.conf
         :emphasize-lines: 4

         [namelist:planet]
         cp=1005.0
         gravity=9.80665
         omega=3.646058E-5
         p_zero=100000.0
         radius=6371229.0
         rd=287.05
         scaling_factor=1.0

Step 3: Run the model and check the output
==========================================

Now that you have halved the rotation rate of the Earth, run the model using
what you have learnt in the previous exercises. After the model has completed,
check the output files to observe the impact of the halved rotation rate on
the model climate. You can use tools like ``ncdump``, ``xconv``, or ``python`` to inspect
the contents of the output NetCDF files and verify the changes.

You should now have successfully completed the halved Earth rotation experiment!
