.. _monsoon3-where-to-run-commands:

***************************
Using Monsoon3
***************************

Monsoon3 uses separate services for access, interactive workflow management,
and HPC work.

Before starting a practical on Monsoon3, sign in to and follow the official
`Monsoon3 User Guide`_. It is the source of truth for the current service
configuration and access requirements.

.. _Monsoon3 User Guide: https://code.metoffice.gov.uk/doc/monsoon3/index.html

Where to run commands
=====================

Use the service identified by the official guidance for the type of work you
are doing:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Type of work
     - Where to run it
   * - Connecting to Monsoon3
     - Follow the official `login guidance`_ and `SSH guidance`_.
   * - Configuring repository access
     - Use the interactive workflow service and follow the official
       `MOSRS guidance`_.
   * - Copying or checking out a workflow
     - Use the interactive workflow service and follow the official
       `Rosie command guidance`_.
   * - Installing, validating, or controlling a workflow
     - Use the service specified in the official `Cylc and Rose guidance`_.
   * - Preparing or submitting HPC work
     - Follow the practical instructions and the official `PBS guidance`_.

.. _login guidance: https://code.metoffice.gov.uk/doc/monsoon3/logging_in.html
.. _SSH guidance: https://code.metoffice.gov.uk/doc/monsoon3/ssh.html
.. _MOSRS guidance: https://code.metoffice.gov.uk/doc/monsoon3/mosrs.html
.. _Rosie command guidance: https://code.metoffice.gov.uk/doc/monsoon3/rosie_commands.html
.. _Cylc and Rose guidance: https://code.metoffice.gov.uk/doc/monsoon3/cylc.html
.. _PBS guidance: https://code.metoffice.gov.uk/doc/monsoon3/pbs.html

Important points
================

* Do not assume that a service named in one part of the course can be reached
  from every other Monsoon3 service. Follow the connection route in the
  official guide. For example:
  * Github repositories should be accessed using https, not ssh.
  * Some Cylc tools and Rose edit will not work on compute nodes.
* Complete the site-supported repository authentication setup before running
  Rosie commands.
* Do not place passwords, authentication codes, tokens, or private connection
  details in course files, terminal transcripts, issues, or pull requests.

Getting help
============

If a connection or authentication step fails, check that you are using the
service and route specified in the current Monsoon3 User Guide. Do not work
around site security controls or store credentials in plain text. Use the
official `Monsoon3 support guidance`_ if the documented setup does not work.

.. _Monsoon3 support guidance: https://code.metoffice.gov.uk/doc/monsoon3/contactus.html
