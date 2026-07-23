.. _Cylc Workflows: https://cylc.github.io/cylc-doc/stable/html/tutorial/introduction.html


Practical exercises
===================

Building and running the model is usually done using `Cylc Workflows`_.

The following exercises demonstrate how to run simplified development
set-ups and tests. These workflows demonstrate how model and workflow
development fit together. Model applications for global and regional modelling
will follow later in this training.

Prerequisites
-------------

Before beginning the practical exercises, read
:ref:`lfric-platform-prerequisites`. In particular, check that you have access
to a supported LFRic build environment, the required source repositories,
Rose/Cylc workflow tooling, and the source-control tools used by your site.

In addition, ensure the practical setup route for your site provides:

* Git and GitHub access for the repositories used in the practicals.
  Active LFRic Atmosphere development is moving through GitHub-hosted
  repositories.
* Access to any Met Office or partner-specific services required by your site.
  Some legacy workflows and documentation still refer to MOSRS/SRS, Rosie,
  Trac, Subversion, or FCM while the wider migration to GitHub is in progress.
* FCM (Flexible Configuration Management), if your local workflow or platform
  still uses FCM-based build or extract steps.

Setup Instructions
++++++++++++++++++

Use the tab that matches your platform before starting the practicals.

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      1. Load the Met Office LFRic module stack described in
         :ref:`lfric-platform-prerequisites` so the required build and workflow
         tools are available.
      2. Make sure you have access to the GitHub repositories used in the
         practicals.
      3. If a practical still requires MOSRS/SRS access, contact
         scientific_partnerships@metoffice.gov.uk to request an account.

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      1. Load the Monsoon3 LFRic module stack described in
         :ref:`lfric-platform-prerequisites` so the required build and workflow
         tools are available.
      2. Make sure you have access to the GitHub repositories used in the
         practicals. Clone over HTTPS rather than SSH, following
         `Git on Monsoon3`_.
      3. Complete the site-supported MOSRS authentication setup before running
         any Rosie commands.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      1. Follow your site's supported LFRic platform instructions to make the
         required build and workflow tools available.
      2. Make sure you have access to the GitHub repositories used in the
         practicals through your site's normal access route.
      3. If a practical or local platform still requires MOSRS/SRS access,
         contact your local institutional sponsor. If unsure, email
         scientific_partnerships@metoffice.gov.uk with your affiliate
         institution and the reason you require access.

.. toctree::

   practical_command_line.rst
   practical_standard_suite.rst
   practical_stem_test.rst
