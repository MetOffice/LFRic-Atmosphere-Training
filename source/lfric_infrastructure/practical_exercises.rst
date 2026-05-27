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

Before beginning the practical, ensure you have access to the following tools:

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
1. Install Git and any site-specific workflow tools required on your platform.
2. Make sure you have access to the GitHub repositories used in the
   practicals.
3. If a practical or local platform still requires MOSRS/SRS access, obtain an
   account through the appropriate route:

   * Met Office staff: Contact scientific_partnerships@metoffice.gov.uk to
     request an account.
   * External users: Contact your local institutional sponsor.
   * If unsure: Email scientific_partnerships@metoffice.gov.uk with your
     affiliate institution and the reason you require access.

.. toctree::

   practical_command_line.rst
   practical_standard_suite.rst
   practical_stem_test.rst
