1. Introduction to LFRic Atmosphere
===================================

.. toctree::
   :name: intro
   :maxdepth: 2

Seamless Modelling
------------------
Since the 1990's the Met Office strategy has been to develop a single model family used for prediction across a range of timescales​. This means the same dynamical core and, where possible, the same parameterization schemes are used across a broad range of spatial and temporal scales​. The image below shows Met Office prediction and projection systems configured for applications on different scales, ranging from a few days to hundreds of years​.

.. figure:: /_static/intro_seamless.png
   :width: 650px

   Spatial and temporal scales of Met Office prediction and projection systems.

The seamless modelling approach approach, first introduced with the Unified Model, is used for LFRic Atmosphere the atmospheric model of Momenetum, The Unified Earth Environment Prediction Framework.

Componenents, Science Configurations, and Systems
--------------------------------------------------
Componenets of the `Momentum  <https://www.metoffice.gov.uk/research/approach/modelling-systems/momentum>`_ Framework, like the the atmospheric model LFRic Atmosphere, are combined to prediction and projection systems, like the ones mentioned in the grafic in the seamless modelling section. Science Configurations are rigorously tested and define the exact setup for the individual model components. These configurations are distinguished between regional and global configurations. Additionally, there are coupled Science Configurations which detail multi-model setups, e.g. an atmosphere – ocean model.

.. figure:: /_static/intro_components.png
   :width: 650px
   :alt: Components of prediction and projection systems

   Key functional components needed to build prediction and proejection systems with the Momentum Framework.

The development approach of Momentum uniquely separates the development of components, Science Configurations, and systems. Each has its own release cycle, but they build on each other. The naming and numbering convention for Momentum Science Configurations is a continuation from the Unified Model software ecosystem to reflect the gradual introduction of the framework into research and operations. The Global Coupled Science Configuration GC6 and the Regional Atmosphere and Land configuration RAL4 will both use the LFRic Atmosphere model and mark the first Science Configurations built with Momentum.

LFRic Atmosphere features and history
-------------------------------------
LFRic Atmosphere has been `developed <https://www.metoffice.gov.uk/research/news/2019/gungho-and-lfric>`_ by the Met Office and partners to replace the Unified Model. LFRic Atmosphere inherited its physics parameterisations from the Unified Model. It uses the land surface model `JULES <https://jules.jchmr.org/about>`_, radiative transfer code `SOCRATES <https://code.metoffice.gov.uk/trac/socrates>`_, Cloud and Aerosol Interacting Microphysics `CASIM <https://code.metoffice.gov.uk/trac/monc/wiki/CASIMDocStart>`_ and the chemistry and aerosols model `UKCA <https://www.metoffice.gov.uk/research/approach/collaboration/jwcrp/ukca>`_. LFRic Atmosphere uses same the terrain follwoing vertical coordinates as the UM but has a cubed sphere mesh, a new mixed finite-element dynamical core GungHo and a new coding infrastructure structucture.

.. figure:: /_static/lfric_mesh_and_vertical_grid.png
   :width: 650px
   :alt: lfric mesh and vertical grid

   Cubed sphere mesh and terrain following verstical coordinates used by LFRic Atmosphere.

BHF ToDo: delete / resue the following:

The need for next generation modelling systems
----------------------------------------------
The Met Office, as well all `Momentum Parnters <https://www.metoffice.gov.uk/research/approach/collaboration/momentum-partnership>`_  have run the Unified Model since 1990's. We’re continually improving our weather and climate models to meet the societal demands for increased accuracy. 
This has been achieved through a combination of approaches:

* Increasing the resolution of our models to capture finer scale features and hence improve accuracy. Currently we run our global model at 10 kilometres but we would like to run it at higher resolutions.
* Including additional components in weather and climate models and perhaps coupling them to other existing forecast models, for example pulling in an iceberg model or a lake model.
* Increasing the size of ensembles to improve predictability.
* Introducing more complicated science

.. image:: /_static/intro_improvement.png
   :width: 650px

This has made our models much more accurate but also more complex and computationally expensive and the systems we use need upgrading for the super computers of the future. 

We’ve been able to deliver these improvements largely due to the ongoing miniaturization of technology, increasing the computational power of the supercomputers our models run on by utilising more powerful chips and processors.

This has been due to 2 well known phenomena:

* **Moore’s law**: The number of transistors on a microchip roughly doubles every two years, whereas it’s cost is halved over the same timeframe.

.. image:: /_static/intro_moore.png
   :width: 650px

* **Dennard scaling**: The performance per watt of computing grows exponentially at roughly the same rate.

.. image:: /_static/intro_denard.png
   :width: 650px

Together, these have resulted in increasingly powerful supercomputers, which in turn has allowed us to create increasingly accurate models, truly probabilistic forecasts and better coupling of models.


.. image:: /_static/intro_timeline.png
   :width: 650px


          
.. note:: 
