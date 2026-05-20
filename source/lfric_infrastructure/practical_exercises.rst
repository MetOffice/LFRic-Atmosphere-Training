.. _Cylc Workflows: https://cylc.github.io/cylc-doc/stable/html/tutorial/introduction.html


Practical exercises
===================

Building and running the model is usually done using `Cylc Workflows`_.

The following exercises demonstrate how to run simplified development
set-ups and tests. These workflows demonstrate developing model and workflows.
Model applications for global and regional modelling will follow later
in this training.

Prerequisites
-------------

Before beginning the practical, ensure you have access to the following tools:

.. TODO - does this make sense - SVN is on its way out

* Subversion (SVN) — A version control system widely used by the Met
  Office to manage internal and shared repositories. LFRic code is also
  held in a SVN repository.
* Met Office Shared Repositories (MOSRS) — The system of shared SVN
  repositories maintained by the Met Office.
* FCM (Flexible Configuration Management) — A build, configuration, and
  version control wrapper system used by the Met Office to manage complex
  software projects.

Setup Instructions
++++++++++++++++++
1. Install SVN and FCM on your system if they are not already installed.
2. Obtain a MOSRS account if you do not already have one:

 * Met Office staff: Contact scientific_partnerships@metoffice.gov.uk to
   request an account.
 * External users: Contact your local institutional sponsor.
 * If unsure: Email scientific_partnerships@metoffice.gov.uk with your
   affiliate institution and the reason you require access.

.. toctree::

   practical_command_line.rst
   practical_standard_suite.rst
   practical_stem_test.rst
