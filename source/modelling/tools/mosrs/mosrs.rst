.. _mosrs-overview:

*******************
MOSRS/SRS Overview
*******************

The Met Office Science Repository Service (MOSRS) and the wider
Science
Repository Service (SRS) have historically hosted Met Office science
code,
workflow repositories, Trac tickets, wiki pages, and Rosie workflow
metadata.
Many older Rose/Cylc workflows, documents, and examples still refer
to this
ecosystem.

.. TODO: Rewrite SRS content
   See:
   https://github.com/MetOffice/LFRic-Atmosphere-Training/issues/103

.. important::

   **SRS to GitHub**

   Most active development is now moving to GitHub.

   SRS is expected to become read-only for some or all repositories
   later in
   2026, although it is expected to remain available in read-only
   form for a
   long time.

   Some workflow dependencies remain, particularly around unique
   suite IDs,
   Rosie-style discovery, and archive locations. These are expected
   to migrate
   later than straightforward code repositories.

   For this training, SRS/MOSRS content is retained where it is still
   relevant
   to current practicals, legacy workflows, or background context.

Why MOSRS/SRS is still mentioned
================================

The training is being updated during a transition period. Some LFRic
and
Momentum material now points to GitHub, while some older workflows and
supporting services still use MOSRS/SRS terminology.

.. note::

   If you think something has become outdated please raise a ticket
   at https://github.com/MetOffice/LFRic-Atmosphere-Training

You may still see references to:

* Subversion repositories and FCM keywords;
* Trac tickets and wiki pages;
* Rosie workflow IDs;
* Rose suites that install code from older repository locations;
* MASS archive paths that include suite or experiment identifiers;
* internal documentation that has not yet been moved to GitHub-hosted
  docs.

These references are not a recommendation to start new work in
MOSRS/SRS where
a GitHub repository is available. They are included because learners
may still
encounter them in current workflows, older examples, or internal
support
material.

How to interpret the transition
===============================

.. list-table::
   :header-rows: 1

   * - Area
     - Current course guidance
   * - Active code development
     - Use GitHub where the repository has migrated. Work through
       branches,
       commits, pull requests, reviews, and automated checks.
   * - Existing MOSRS/SRS code or documentation
     - Treat it as legacy or transitional unless project guidance says
       otherwise.
   * - Trac tickets
     - In migrated projects, create GitHub issues for new work. Older
       Trac
       tickets may still be useful historical references.
   * - Rose/Cylc workflows
     - Follow the practical instructions. Some workflows are already
       stored in
       GitHub; others may still depend on Rosie, FCM, or SRS-era
       assumptions.
   * - Archive and discovery metadata
     - Be aware that Rosie IDs and MASS archive paths do not map
       directly to
       GitHub repositories and branches. This is one reason workflow
       migration
       is being handled carefully.
   * - External partners
     - Some internal Met Office links may not be accessible. Use the
       public
       GitHub material where available and follow your local access
       route for
       restricted repositories or services.

Workflow migration context
==========================

Normal code repositories and Rose/Cylc workflows have different
migration
challenges. Historic Rosie workflows have used short identifiers not
only for
version control, but also for experiment tracking, discovery,
metadata, plot
labelling, and archive locations. GitHub repositories, branches,
commits, and
tags provide a different model.

The expected direction is to use fewer, better-named workflow
repositories,
with Git branches and commits used for ordinary development. New
repositories
or forks may still be needed when a workflow has a genuinely separate
long-term
line of development.

Where a workflow relies heavily on Rosie IDs, Rosie discovery
metadata, or
MASS archive paths based on suite names, migration may require
additional
project-specific guidance. This is why the course still mentions
MOSRS/SRS in
places even though GitHub is the primary direction for active
development.

What you should do in this course
=================================

For the practical exercises:

* follow the checkout instructions exactly;
* use GitHub where the instructions clone a GitHub repository;
* do not replace GitHub instructions with old MOSRS/SRS equivalents;
* treat MOSRS/SRS references as legacy context unless the practical
  explicitly
  tells you to use them;
* ask your project contact or local support route if you need access
  to
  restricted Met Office services.

