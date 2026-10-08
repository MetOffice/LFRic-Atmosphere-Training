.. _isambard3-getting-started:

***************************
Using Isambard 3
***************************

`Isambard 3`_ is a Grace (aarch64) supercomputer run by the Bristol Centre for
Supercomputing. The **Isambard 3** tab in this course uses a pre-built LFRic
environment for Isambard 3 and a separate Python environment for analysis.

Before starting a practical on Isambard 3, read the official
`Isambard documentation`_. It is the source of truth for the current service
configuration, access and login.

Getting access
==============

Accounts for this course are provided through the University of Exeter, a
Momentum partner. To get access, ask your University of Exeter contact for
this training to add you to the Isambard 3 project used by the course. You
then log in with the ``clifton`` tool described in the official
`login guidance <Isambard login_>`_:

.. code-block:: bash

   # On your own computer
   clifton auth                # sign in; the certificate lasts 12 hours
   clifton ssh-config write    # once, after you are added to a project
   ssh <PROJECT>.3.isambard

Replace ``<PROJECT>`` with the project short name shown by ``clifton``.

Where to run commands
=====================

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Type of work
     - Where to run it
   * - Editing files, cloning repositories, Rosie commands, starting Cylc
       workflows, ``rose edit``
     - A login node. You land on one at random each time you log in.
   * - Compiling and running LFRic Atmosphere
     - A compute node, through Slurm. The practicals give the commands.
   * - The Jupyter notebooks and plotting in this course
     - A login node. These workloads are small enough to run there.

The LFRic environment
=====================

The LFRic build and workflow tools (compiler, MPI, XIOS, PSyclone, Rose and
Cylc) come from a pre-built environment built with `lfric-env-isambard`_.

Your University of Exeter contact will tell you the directory where the
course's environments are installed. Once, after you first log in, save it in
``~/.bashrc`` so that every new terminal knows it, then log in again:

.. code-block:: bash

   # Replace <DIRECTORY> with the directory you were given
   echo 'export LFRIC_TRAINING_PREFIX=<DIRECTORY>' >> ~/.bashrc

Load the environment in every new terminal before building or running the
model:

.. include:: /include/isambard3-lfric-env.rst

Check that it works:

.. code-block:: bash

   rose --version; cylc --version; psyclone --version

The Python analysis environment
===============================

The Python packages used for analysis and the Jupyter notebooks (Iris,
GeoVista, iris-esmf-regrid, JupyterLab, ...) are in a separate conda
environment. It is activated with ``micromamba``, which is provided alongside
it, so you do not need to install conda yourself:

.. include:: /include/isambard3-python-env.rst

You can have both environments active at the same time: load the module first,
then activate the Python environment.

.. _isambard3-mosrs:

Using MOSRS and Rosie
=====================

Some practicals check out a workflow from the Met Office Science Repository
Service (MOSRS) with ``rosie``. You need your own MOSRS account for this; if
you do not have one, see :ref:`mosrs-overview`.

With the LFRic environment loaded, cache your MOSRS password so that
``rosie`` and ``svn`` do not ask for it each time:

.. code-block:: bash

   mosrs-cache-password

The first time, the command lists any one-off settings it needs in
``~/.subversion`` and ``~/.gnupg``, with the exact lines to add. Add them and
run it again.

.. note::

   The password is cached on the login node where you ran the command, and
   you land on a login node at random each time you log in. If ``rosie`` asks
   for your password again, run ``mosrs-cache-password`` again.

.. _isambard3-jupyterlab:

Running JupyterLab
==================

JupyterLab runs on the login node, and you open it in the browser on your own
computer through an SSH tunnel. Because you land on a login node at random, the
server listens on that login node's internal address rather than on
``localhost``.

1. **Choose a port.** Pick a number between 1024 and 65535 that nobody else is
   using, for example ``28765``. Other users share the login nodes, so do not
   just use the example. Check that nothing is already listening on it:

   .. code-block:: bash

      PORT=28765   # replace with your own choice
      ss -ltn | grep ":$PORT " || echo "port $PORT is free"

2. **Start JupyterLab on Isambard 3**, with the Python environment active and
   from the directory the practical tells you:

   .. code-block:: bash

      jupyter lab --no-browser --port="$PORT" \
          --ip="$(hostname -s).hsn.cm.i3.isambard.ac.uk"

   The output contains a URL such as:

   .. code-block:: text

      http://login01.hsn.cm.i3.isambard.ac.uk:28765/lab?token=0123abcd...

   Note the host (``login01.hsn.cm.i3.isambard.ac.uk``), the port, and the
   token. If your port turned out to be busy, JupyterLab picks the next free
   one; use the port shown in the URL.

3. **Open the tunnel from your own computer**, in a new terminal, copying
   ``PORT`` and ``HOST`` from the URL:

   .. code-block:: bash

      # On your own computer
      PORT=28765
      HOST=login01.hsn.cm.i3.isambard.ac.uk
      ssh -T -L "localhost:$PORT:$HOST:$PORT" <PROJECT>.3.isambard

   The command prints nothing when it works. Leave it running.

4. **Open** ``http://localhost:<PORT>/lab?token=<TOKEN>`` in your browser.

When you have finished, stop JupyterLab with :kbd:`Control-c` in the Isambard 3
terminal, then stop the tunnel. See also the official
`Jupyter guidance <Isambard Jupyter_>`_.

.. _isambard3-cylc:

Cylc workflows and login nodes
==============================

A Cylc workflow's scheduler runs on the login node where you started it, and
submits the workflow's tasks to Slurm. You can monitor and control it from any
login node: ``cylc tui``, ``cylc pause``, ``cylc play`` (to resume),
``cylc stop`` and ``cylc cat-log`` all work.

The exception is a scheduler that has died without shutting down cleanly, for
example because its login node was restarted. Its workflow then still looks
like it is running. From a different login node, restarting it fails:

.. code-block:: text

   ERROR - Cannot determine whether workflow is running on login01.head.cm.i3.isambard.ac.uk.
   CRITICAL - Cannot tell if the workflow is running

This happens because Cylc checks the old login node over SSH, which Isambard 3
does not allow. If you are sure the workflow is not running (``cylc ping
<workflow>`` fails), remove its stale contact file and start it again:

.. code-block:: bash

   rm ~/cylc-run/<workflow>/runN/.service/contact
   cylc play <workflow>

Important points
================

* Anyone who has your Jupyter token can run code as you. Do not share it, and
  stop JupyterLab when you are not using it.
* GitHub repositories can be cloned over HTTPS without an SSH key.
* Rosie commands need your own MOSRS account; see :ref:`isambard3-mosrs`.
* Do not place passwords, authentication codes, tokens, or private connection
  details in course files, terminal transcripts, issues, or pull requests.

Getting help
============

For problems with your Isambard 3 account, login or the service, use the
`Isambard documentation`_ and the BriCS helpdesk. For problems with the
course's LFRic or Python environments on Isambard 3, ask your University of
Exeter contact, or start a discussion on the course's GitHub Discussions.
