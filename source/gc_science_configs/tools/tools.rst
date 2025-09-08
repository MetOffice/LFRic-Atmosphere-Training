Tools for running GC model configurations
=========================================

NWP and climate models have a large numbers of jobs which are executed at regular intervals to process new data and generate new forecasts. Dependence between these forecast cycles creates a single never-ending workflow, which NWP workflow schedulers have traditionally ignored. Met Office science configurations are built on **Rose** and **Cylc (“Silk”)** to manage infinite cycling workflows efficiently even after delays in real-time operation, or in historical runs, when cycles can typically interleave for much-increased throughput.

MOSRS Overview
--------------

The Met Office Science Repository Service (MOSRS) is a platform used to manage and store scientific software and related resources developed by the Met Office and its collaborators. It provides version control, access management, and collaboration tools for a range of scientific projects, including atmospheric and climate modeling.

Key features of MOSRS include:

* **Centralized Repository:** Stores source code, documentation, and configuration files for various science projects.
* **Access Control:** Manages user permissions to ensure secure and appropriate access to resources.
* **Collaboration:** Facilitates collaboration between scientists, developers, and external partners.
* **Documentation:** Hosts comprehensive documentation for science configurations, model development, and workflows.
* **Issue Tracking:** Integrates with ticketing systems to track bugs, feature requests, and development tasks.

MOSRS is essential for ensuring reproducibility, transparency, and efficient management of scientific software and configurations within the Met Office community.

GC Model on MOSRS
-----------------

On MOSRS, the GC model and its associated science configurations are organized and maintained to support both development and operational use.

Details about the GC model on MOSRS include:

* **Repository Structure:** The GC model source code, configuration files, and documentation are stored in dedicated repositories. These repositories are organized by model version (e.g., UM-based or LFRic-based GC) and by release cycle.
* **Science Configurations:** Each GC configuration defines a specific set of model settings, parameterizations, and input data for a particular scientific or operational purpose. These configurations are version-controlled and documented within MOSRS.
* **Development Workflow:** Scientists and developers use MOSRS to collaborate on model development, propose changes, and review updates. Branching and merging workflows help manage contributions and maintain stability.
* **Release Process:** New GC model versions and configurations are released through a controlled process, with documentation and release notes stored alongside the code.
* **Documentation:** Detailed documentation is provided for each GC configuration, including scientific rationale, technical setup, and usage instructions. This ensures users can reproduce experiments and understand configuration differences.
* **Integration with Wiki Tickets:** Tasks, bug reports, and feature requests related to the GC model are tracked using the MOSRS wiki ticket system, supporting transparent and organized development.

By hosting the GC model on MOSRS, the Met Office ensures that model development is collaborative, traceable, and accessible to authorized users.

Release Process for Configurations
----------------------------------

Releasing a new GC configuration involves several coordinated steps to ensure quality, reproducibility, and traceability:

1. **Development and Testing:** Scientists and developers implement changes or new features in a development branch. Rigorous testing and validation are performed to ensure scientific correctness and technical stability.
2. **Documentation:** Comprehensive documentation is prepared, detailing the scientific rationale, technical setup, and any changes from previous configurations.
3. **Review and Approval:** The proposed configuration and its documentation are reviewed by peers or designated reviewers. Feedback is addressed before proceeding.
4. **Versioning and Tagging:** Once approved, the configuration is merged into the main repository and assigned a version number or tag for traceability.
5. **Release Notes:** Release notes summarizing the changes, new features, and known issues are published alongside the configuration.
6. **Distribution:** The released configuration is made available to users through MOSRS, with clear instructions for access and use.

Differences Between Configurations and Their Development
--------------------------------------------------------

GC configurations differ in their scientific aims, parameterizations, input data, and technical setups. For example, some configurations may target operational forecasting, while others are designed for research experiments or specific scientific studies.

Development of configurations typically involves:

* **Defining Scientific Objectives:** Each configuration is tailored to meet specific research or operational goals.
* **Selecting Parameterizations:** Choices are made regarding physical and chemical processes to include or modify.
* **Input Data Preparation:** Appropriate datasets are selected and pre-processed for the configuration.
* **Testing and Validation:** Configurations undergo testing to ensure they produce scientifically valid results.
* **Documentation:** Each configuration is documented to describe its purpose, setup, and differences from others.

Differences Between UM and LFRic GC Configurations
--------------------------------------------------

The GC model has been implemented using both the Unified Model (UM) and LFRic frameworks, resulting in distinct configuration approaches:

* **UM-based GC Configurations:** Built on the established Unified Model infrastructure, these configurations use legacy code and workflows. They are widely used for operational and research purposes and have a mature set of parameterizations and tools.
* **LFRic-based GC Configurations:** Developed using the newer LFRic infrastructure, these configurations leverage modern software engineering practices, improved scalability, and flexibility. LFRic-based configurations may differ in available features, parameterizations, and workflows as development progresses.

Key differences include the underlying model architecture, supported features, and the maturity of the configuration and workflow tools. Users should consult documentation to understand the specific capabilities and limitations of each version.

Wiki Tickets on MOSRS
---------------------

Wiki tickets on MOSRS are used to manage and track updates, bug fixes, and feature requests for the GC models. They provide a transparent and organized way for developers and scientists to coordinate work, document progress, and communicate about ongoing tasks.

Typical usage of wiki tickets for updating GC models includes:

* **Creating a Ticket:** When a new issue, enhancement, or update is needed for a GC model or configuration, a ticket is created in the MOSRS wiki ticket system. The ticket should describe the problem or proposed change, relevant background, and any supporting information.
* **Assigning and Prioritizing:** Tickets can be assigned to specific team members and prioritized based on urgency or project timelines.
* **Tracking Progress:** As work progresses, ticket comments and status updates are used to document discussions, decisions, and implementation steps. This ensures all contributors are informed and can collaborate effectively.
* **Linking to Code Changes:** Tickets are often linked to specific branches or commits in the repository, providing traceability between the ticket and the code or configuration updates.
* **Review and Closure:** Once the update is complete and reviewed, the ticket is closed with a summary of the resolution and any relevant documentation links.

Using wiki tickets ensures that updates to GC models are well-documented, reviewed, and traceable, supporting reproducible and collaborative development within the MOSRS environment.

GitHub Overview
---------------

**PENDING**

Rose - managing model configurations
------------------------------------

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

Cylc - workflow engine
----------------------

* Cylc is a general-purpose workflow engine used to automate running groups of tasks in a specified order on computers.
* Cylc workflows can be organized running tasks at specific clock cycles.
* Cylc workflows represent the highest-level programming layer for organising the execution of our models, pre- and postprocessors.

.. image:: /_static/cylc.gif
   :width: 700px

.. note::
   * Comprehensive guides and training for cylc can be found here: https://cylc.github.io/cylc-doc.
   * The cylc GitHub discourse can be used for discussions: https://cylc.discourse.group.

.. quizdown::

    ---
    primary_color: orange
    secondary_color: lightgray
    text_color: black
    shuffle_questions: false
    ---

   ## Drag and drop the directory structure of a GC workflow to locate the namcouple file.

    > namcouple is last.

    1. roses/
    2. suite-ID/
    3. app/
    4. coupled/
    5. file/
    6. namcouple

   ## What is the correct definition for a cylc workflow?

   - [ ] a system for managing repetitive processes and tasks which occur in a particular order
   - [x] a general-purpose workflow engine that also orchestrates cycling systems very efficiently
   - [ ] a system for delivering climate data to customers

   ## In what file would you find the owner of the workflow you are using?

   - [ ] rose-suite.conf
   - [x] rose-suite.info
   - [ ] rose-info.conf
   - [ ] READ.ME


.. note:: On Version Control -
