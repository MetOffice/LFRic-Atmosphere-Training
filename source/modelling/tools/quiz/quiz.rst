*****************
Tools review quiz
*****************

This quiz reviews how the modelling tools introduced in this section fit into a typical workflow.

.. quizdown::

    ---
    primary_color: orange
    secondary_color: lightgray
    text_color: black
    shuffle_questions: false
    ---

   ## Why do Momentum prediction and projection systems need workflow tooling?

   1. [ ] Because each model run is a single independent command with no dependencies
       > Incorrect. The tools are needed because model workflows involve many related jobs and dependencies.
   1. [x] Because many jobs run across repeated cycles, with dependencies between tasks and cycles
       > Correct! Numerical Weather Prediction and climate workflows contain many jobs, repeated cycles, and dependencies that need to be managed.
   1. [ ] Because workflow tools replace the need for model configurations
       > No. Workflow tools organise execution, but configurations still define how applications are run.
   1. [ ] Because all model output is manually copied between tasks
       > Incorrect. The point of workflow tooling is to automate and organise this kind of process.

   ## A workflow has several model, pre-processing, and post-processing tasks that must run in a controlled order. Which tool is responsible for orchestrating that execution?

   1. [ ] GitHub
       > GitHub supports repository hosting, pull requests, review, and traceability; it does not orchestrate model workflow tasks.
   1. [x] Cylc
       > Correct! Cylc is the workflow engine used to automate groups of tasks and their dependencies.
   1. [ ] Rose
       > Rose manages application configuration, but Cylc orchestrates the workflow execution.
   1. [ ] A pull request
       > A pull request supports review and traceability for a change; it does not run the workflow.

   ## What does it mean for Cylc to sit at the highest-level programming layer in these workflows?

   1. [x] It coordinates when workflow tasks run and how they depend on one another
       > Correct! Cylc organises the execution of models, pre-processors, and post-processors.
   1. [ ] It stores every source-code change made to the model
       > That is a version-control and repository-management concern.
   1. [ ] It defines every science parameter inside each application
       > Application settings are handled through configurations, not by Cylc alone.
   1. [ ] It replaces the model code with a graphical interface
       > Incorrect. Cylc manages workflow execution; it does not replace the model code.

   ## You need to define application inputs, file installation behaviour, and environment variables in a human-readable form. Which tool is the best fit?

   1. [ ] Cylc, because it is the workflow engine
       > Cylc can run tasks, but Rose is the tool described here for managing application configurations.
   1. [x] Rose, because Rose configurations encapsulate application settings and related assets
       > Correct! Rose configurations define application behaviour such as execution settings, file installation, and environment variables.
   1. [ ] Pull requests, because pull requests contain runtime settings
       > Pull requests can document and review changes, but they are not application configuration files.
   1. [ ] A post-processing task, because configuration is only needed after the model runs
       > Incorrect. Configuration is needed to define how applications run in the first place.

   ## How do Rose and Cylc normally complement each other in LFRic model experiments?

   1. [ ] Rose schedules tasks, while Cylc stores source code and pull requests
       > Incorrect. This reverses or misplaces the roles of the tools.
   1. [x] Rose manages application configuration, while Cylc organises workflow execution
       > Correct! Rose defines how applications are configured, and Cylc manages the workflow that runs them.
   1. [ ] Rose and Cylc both do the same job, so only one can be used
       > No. The section explains that Rose configurations may be used with the Cylc workflow engine.
   1. [ ] Cylc validates Rose metadata but does not run tasks
       > Incorrect. Cylc is introduced as the workflow engine for running organised groups of tasks.

   ## Why is version control important for model and configuration development?

   1. [ ] It removes the need to document scientific changes
       > Incorrect. Version control supports traceability, but documentation remains important.
   1. [ ] It prevents anyone else from reviewing changes
       > No. The material describes collaborative development and review.
   1. [x] It allows changes to be tracked, reviewed, and linked to the work they address
       > Correct! Branches, commits, pull requests, review discussion, and documentation make development traceable.
   1. [ ] It is only used for operational forecasts, not science configurations
       > Incorrect. The section describes version control for source code, documentation, and configuration files.

   ## A regional-model configuration is being updated for a specific scientific purpose through a pull request. What practice best supports reproducibility and traceability?

   1. [ ] Make the change locally and rely on memory to explain it later
       > Incorrect. That would make the change difficult to reproduce or review.
   1. [x] Track the change in version control, explain it in the pull request, and link to the relevant documentation
       > Correct! Version control, documentation, and review discussion make the change easier to understand, reproduce, and maintain.
   1. [ ] Avoid review because regional configurations are always local
       > No. The section describes collaboration and review for regional model development.
   1. [ ] Store the configuration outside the repository so it is easier to edit
       > Incorrect. Keeping configuration changes in version control supports reproducibility.

   ## In a GitHub-style workflow, what is the main role of a pull request?

   1. [ ] Running model tasks at specific clock cycles
       > That is part of the workflow-engine role described for Cylc.
   1. [ ] Editing Rose metadata through a graphical interface
       > That is part of the Rose configuration tooling, not the role of a pull request.
   1. [x] Proposing a change, collecting review, recording discussion, and linking to supporting information before merge
       > Correct! Pull requests provide a traceable place to review a branch and connect the change to evidence and documentation.
   1. [ ] Replacing documentation because pull requests are permanent
       > Incorrect. Pull requests support traceability, but they do not replace clear documentation.

   ## Which summary best describes the tools introduced in this section?

   1. [x] GitHub supports repository traceability and review; Rose manages application configurations; Cylc orchestrates workflow execution.
       > Correct! This captures the broad responsibilities introduced across the tools pages.
   1. [ ] GitHub runs task graphs; Rose stores pull requests; Cylc manages repository access.
       > Incorrect. This mixes up the responsibilities of the tools.
   1. [ ] GitHub is only for visualisation; Rose is only for source-code review; Cylc is only for plotting.
       > No. These are not the roles described in the section.
   1. [ ] All three tools are interchangeable ways to edit the same configuration file.
       > Incorrect. The tools have related but distinct roles.
