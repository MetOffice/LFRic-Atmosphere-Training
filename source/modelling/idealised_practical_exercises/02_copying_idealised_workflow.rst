Getting Started: Copying a Workflow for the Idealised Suite
===========================================================

To begin working with the idealised suite, you first need to create your own
copy of an existing workflow.

As introduced in the *Global Modelling Practical*, you can do this using the
``rosie`` command-line tool — see there for :ref:`the difference between
copying and checking out <rosie-copy-vs-checkout>`. As in the earlier
practicals, **copy** the workflow rather than checking it out:

.. tab-set::
   :sync-group: site

   .. tab-item:: Met Office
      :sync: met-office

      .. include:: /include/snippets/rosie-copy-idealised.rst

   .. tab-item:: Monsoon
      :sync: monsoon

      .. include:: /include/monsoon3-help.rst

      .. important::

         These tutorials require you to be on a Cylc host.

      .. include:: /include/snippets/rosie-copy-idealised.rst

   .. tab-item:: Isambard 3
      :sync: isambard3

      .. include:: /include/isambard3-help.rst

      On Isambard 3, **check out** ``u-dz791`` instead of copying it, at the
      revision that has been tested there. As published, the workflow builds
      an older LFRic release and reads source code from a Met Office
      account. The launcher from lfric-env-isambard adapts your checkout to
      Isambard 3 when you run it (see :doc:`04_running_idealised_workflow`).

      .. code-block:: bash

         mosrs-cache-password
         rosie checkout u-dz791
         svn update -r 368986 ~/roses/u-dz791

      Then get the launcher, and the LFRic metadata it uses to upgrade the
      workflow. Skip the ``git clone`` if you already have it from
      :ref:`practical_3.2`:

      .. code-block:: bash

         git clone https://github.com/ickc/lfric-env-isambard.git \
               "$SCRATCHDIR/lfric-env-isambard"
         git -C "$SCRATCHDIR/lfric-env-isambard" submodule update --init \
               vendor/lfric_apps vendor/lfric_core vendor/physics/jules

      Wherever the rest of this practical says ``<suite-id>``, use
      ``u-dz791``.

   .. tab-item:: Other
      :sync: other

      .. include:: /include/other-platform-hpc.rst

      .. include:: /include/snippets/rosie-copy-idealised.rst

The command reports the new suite ID it created, and the local copy it made
under ``~/roses``. Make a note of that ID: the rest of this practical refers to
it as ``<suite-id>``.
