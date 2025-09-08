************************************
Rose - managing model configurations
************************************

.. image:: /_static/rose.png
   :align: right
   :width: 200px

* Rose is a tool for writing, editing, updating, and running configurations of applications
* Rose allows top-level configuration of applications for workflows used for LFRic and UM model experiments
* Developed by the Met Office, but not LFRic specific (i.e. used for NEMO as well)

**Rose configurations** are directories containing a Rose configuration file along with other optional assets which define behaviours such as execution, file installation, and environment variables.

Rose configurations may be used standalone or in combination with the Cylc workflow engine.

**Why Use Rose Configurations?**

With Rose configurations, the inputs and environment required for a particular purpose can be encapsulated in a simple human-readable configuration. Configuration settings can have metadata associated with them which may be    used for multiple purposes including automatic checking and transforming. Rose configurations can be edited either using a text editor or with the rose config-edit GUI which makes use of metadata for display and on-the-fly validation purposes.


.. note:: More information and training material: https://metomi.github.io/rose/doc/html/tutorial/rose/metadata.html