.. _github-overview:

***************
GitHub Overview
***************

The Met Office is moving science code development to GitHub
development. LFRic Atmosphere training already uses GitHub-hosted repositories
for the practical code checkout and workflow examples, and this will become
increasingly normal as science code and workflows move away from older
Subversion and Trac-based services.

This page gives the high-level context needed for the course. It does not try
to reproduce the full Met Office Git migration guidance.

.. important::

   GitHub is the primary place to look for active development of repositories
   that have already migrated. Some older documentation, workflow material, and
   supporting services still refer to MOSRS, SRS, Rosie, Trac, Subversion, or
   FCM. Those references are retained where they are still relevant to current
   practicals, legacy workflows, or services that have not yet fully migrated.

Why GitHub?
===========

There are several reasons for the move from Subversion and Trac to Git and
GitHub:

* Git is the standard version-control system used across much of modern
  software development.
* Git supports fast local operations, lightweight branches, stashing, staging,
  and better branch-of-branch workflows.
* GitHub adds pull requests, inline review comments, suggestions, automated
  checks, project boards, issue templates, labels, and hosted documentation.
* GitHub makes collaboration with partners and external contributors more
  familiar, provided repository access and information-governance requirements
  are handled correctly.
* Moving active work to GitHub reduces reliance on legacy Subversion and Trac
  infrastructure as the Met Office science repositories transition.

For this training, the practical consequence is simple: when a repository has
moved to GitHub, expect routine development to happen through Git branches,
commits, pull requests, reviews, and automated checks.

How GitHub fits into LFRic Atmosphere work
==========================================

LFRic Atmosphere development is split across several repositories. The
:doc:`LFRic code repositories </lfric_infrastructure/code_repositories>` page
describes the main repositories and science-component links.

For a typical small code change, the workflow is:

1. Find or create an issue that describes the work.
2. Check out the relevant GitHub repository.
3. Create a branch for the change.
4. Make focused commits with clear commit messages.
5. Push the branch to your fork of the repository on GitHub.
6. Open a pull request.
7. Use review comments and automated checks to improve the change.
8. Merge only when the project working practices allow it.

In real LFRic development, follow the
:external+simulation_systems:ref:`Simulation Systems Working Practices <working_practices_index>`.
The sequence above is only the introductory mental model.

Git and GitHub core terms
=========================

Git and GitHub are related, but they are not the same thing.
`Git <https://git-scm.com/>`_ is the version-control tool that records changes
in a repository and lets you work with commits and branches on your own
machine. `GitHub <https://github.com/>`_ is a hosting and collaboration
platform for Git repositories. It adds browser-based repository views, issues,
pull requests, code review, project coordination, and automated checks.

In practice, you usually use both together: Git records and moves your local
changes, while GitHub provides the shared place where those changes are
reviewed, tested, discussed, and merged.

Git terms
---------

.. list-table::
   :header-rows: 1

   * - Term
     - What it means in this course
     - LFRic Apps example on GitHub
   * - Repository
     - A Git project containing source code, documentation, tests, workflow
       files, or supporting material.
     - `LFRic Apps repository <https://github.com/MetOffice/lfric_apps>`_
   * - Branch
     - A line of development used to keep your change separate from ``main``
       until it is ready for review.
     - `LFRic Apps branches <https://github.com/MetOffice/lfric_apps/branches>`_
   * - Commit
     - A recorded snapshot of a focused change.
     - `LFRic Apps commit history <https://github.com/MetOffice/lfric_apps/commits/main>`_

GitHub terms
------------

.. list-table::
   :header-rows: 1

   * - Term
     - What it means in this course
     - LFRic Apps example
   * - Issue
     - A GitHub item used to describe work, questions, bugs, or follow-up
       tasks. In migrated projects, issues often take the role previously
       served by Trac tickets.
     - `LFRic Apps issues <https://github.com/MetOffice/lfric_apps/issues>`_
   * - Pull request
     - A request to merge a branch. It is also the place where review
       comments, suggestions, test results, and approval decisions are
       collected.
     - `LFRic Apps pull requests <https://github.com/MetOffice/lfric_apps/pulls>`_

Change review and test evidence
===============================

Most collaborative development workflows include both human review and
automated evidence. The exact tools vary between projects, but the concepts are
the same: people check whether a change is appropriate, and automated systems
run repeatable checks that help expose mistakes.

When you contribute changes to repositories used by this training, such as
LFRic Apps, JULES, or other science-component repositories, you will usually
encounter these steps when opening a pull request back to the main repository
and target branch. The repository maintainers use the review discussion and
check results to decide whether the change is ready to merge.

.. list-table::
   :header-rows: 1

   * - Term
     - What it means in this course
   * - Review
     - The process of checking a proposed change for correctness,
       maintainability, test evidence, documentation, and consistency with
       project standards.
   * - Automated checks
     - Repeatable tests, documentation builds, style checks, or other
       validation run by an automated system. They provide evidence about a
       change, but they do not replace human review.

What learners need to know
==========================

You do not need to be a Git expert to follow this course, but you should know
the following before contributing changes:

* changes should be made on a branch, not directly on ``main``;
* commits should be small enough to review and should explain why the change
  was made;
* pull requests are the normal review route for GitHub-hosted repositories;
* automated checks are part of the evidence for a change, but passing checks do
  not replace human review;
* comments, review suggestions, and requested changes should be handled in the
  pull request so the discussion stays with the code;
* Met Office staff and partners may need specific GitHub organisation access,
  while external users should follow their own site's access instructions.

GitHub and workflows
====================

Rose suites and Cylc workflows need extra care during the migration to Git.
This is more complicated than moving a normal code repository:

* there are many historic Rosie workflows, far more than should become
  individual GitHub repositories;
* Rosie IDs have been used for experiment tracking, discovery, metadata, plot
  labelling, and archive locations;
* some workflows archive to MASS paths based on Rosie-style identifiers;
* discovery and metadata workflows need replacements in the Git/GitHub world;
* some workflows still depend on FCM, Subversion-style file installation, or
  build patterns that need migration work.

The intended direction is fewer, better-named workflow repositories, with
branches, commits, tags, and possibly forks representing normal lines of
development. Where workflows depend on Rosie IDs, MASS archive conventions, or
Rosie discovery metadata, migration may need to wait for the relevant project
guidance and tooling.

For this training, you only need the high-level rule: use the GitHub workflow
where the practical tells you to clone from GitHub, but do not assume every
historic Rose/Cylc workflow has already moved cleanly from MOSRS/SRS to
GitHub.

MOSRS/SRS during the transition
===============================

MOSRS/SRS is still mentioned in the training because some tools, examples, and
legacy workflows still depend on it. When possible, however, new development
should default to MOSRS/SRS when a GitHub repository is available.

Current transition points to keep in mind:

* most active development is moving to GitHub;
* SRS/MOSRS content may remain relevant for legacy documentation, old tickets,
  historic workflow IDs, or services that have not yet moved;
* SRS is expected to become read-only for some or all repositories later in
  2026, while remaining available in read-only form for a long period;
* workflow-specific dependencies, especially around unique suite IDs,
  discovery, and archive paths, are expected to take longer to migrate.

Access and local policy
=======================

This training includes the minimum context needed to understand why both GitHub
and MOSRS/SRS appear in the material. For repository access, authentication,
and local workflow policy, follow the instructions from your own site or
project contact.
