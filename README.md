# LFRic-Atmosphere-Training

This repository hosts the materials for self-learning of the Momentum LFRic Atmosphere. This training is designed to provide an introductory level training for the LFRic Atmospheric model and its associated workflows. The training material includes an overview about the model, development working practices, visualisation of mesh data, LFRic based Science Configurations, and practical exercises for hands-on learning.

The training is structured to cater to users with different levels of expertise, from beginners to advanced users. It covers essential aspects like understanding model input and output files, navigating code repositories, and running model configurations. The goal is to make the training accessible and beneficial for all Momentum users, ensuring they can effectively use the LFRic Atmosphere model.

The LFRic Atmosphere self-learning training can be found at <https://metoffice.github.io/LFRic-Atmosphere-Training>

## Contributing & Development

The preferred way to contribute to LFRic-Atmosphere-Training is to fork the main repository, then submit a "pull request" (PR). When updating this training material, aim for clear and easy-to-understand content. Please keep in mind that this training is intended for an introductory level training.

To [create a fork](https://github.com/MetOffice/LFRic-Atmosphere-Training/fork)
under your own account. Use the following commands to clone the correct repository and create a `latest` branch pointing to the [`main` branch in this repository](https://github.com/MetOffice/LFRic-Atmosphere-Training/tree/main).

When creating new branches use the `latest` branch as the parent branch unless a feature branch exists.

```bash

# Clone your forked repository into a LFRic-Atmosphere-Training folder
git clone https://github.com/<GITHUB-USERNAME>/LFRic-Atmosphere-Training.git

cd LFRic-Atmosphere-Training

# Add the MetOffice LFRic-Atmosphere-Training repository as an upstream remote
git remote add upstream https://github.com/MetOffice/LFRic-Atmosphere-Training.git

# This gets all the updates from all your remotes (your fork and the central repository)
git fetch --all

# This creates a new branch called latest which follows upstream/main and checks it out.
git checkout upstream/main -b latest

# And to prevent accidentally pushing to upstream/main...
git remote set-url --push upstream no_push

# And to prevent pushing your origin/main branch to unwanted places...
git branch -D main
```

### Development Environment

Dependencies are defined in `pyproject.toml`. There are two possible setup methods, `uv` and `venv` + `pip`, you only need to use one.

#### Route 1: `uv` (recommended)

Install `uv` if needed:

```bash
python3 -m pip install --user uv
```

Create or update the project virtual environment (documentation dependencies only):

```bash
uv sync --python 3.11
```

Install optional extras as needed:

```bash
# Notebook and exercise dependencies
uv sync --extra notebooks

# Mesh tutorial notebook dependencies
uv sync --extra mesh_tutorials

# Development tooling (e.g., pre-commit hooks)
uv sync --extra dev

# Both optional groups
uv sync --extra notebooks --extra dev

# Mesh tutorials + development tooling
uv sync --extra mesh_tutorials --extra dev

# Everything defined in pyproject.toml optional dependencies
uv sync --all-extras
```

Activate the environment:

```bash
source .venv/bin/activate
```

If you prefer not to activate the environment, run commands with `uv run ...` instead.

#### Route 2: `venv`/`conda` + `pip`

Create and activate a virtual environment:

```bash
# With venv
/path/to/python3.11+ -m venv .venv
source .venv/bin/activate

# With Conda
conda create -n lfric-workflow python=3.12 pip
conda activate lfric-workflow
```

Install dependencies:

```bash
pip install .
```

Install optional dependencies:

```bash
pip install ".[notebooks,mesh_tutorials,dev]"
```

If you are contributing and want an editable install:

```bash
pip install -e ".[notebooks,mesh_tutorials,dev]"
```

### Dependency Policy

- Build environments from `pyproject.toml` only.
- If dependency updates are needed, update constraints in `pyproject.toml` and recreate the environment with your selected setup route.

### Building Training Materials

The training materials are based on [Sphinx](https://www.sphinx-doc.org) and can be built using the provided Makefile on any desired target format. However, we aim to display the content as HTML pages, and any contributions should ensure these are produced correctly.

To build the LFRic Atmosphere training materials in HTML format run the following command:

```bash
# If you are using uv:
uv run make clean html linkcheck

# If you are using venv + pip:
make clean html linkcheck
```

That concludes the process! You’ll find the generated HTML files within the “build” folder.

> [!NOTE]
> You may find it useful to install `sphinx-autobuild` and develop
> documentation in an editor while running
> `sphinx-autobuild source/ build/` in a terminal window.


#### Using Intersphinx Links

Intersphinx has been enabled between these docs and other key
LFRic documentation built with Sphinx. To see a full list of references
available run:

```console
./etc/bin/intersphinx_reference.py

# Or pipe to a file that you can search in your editor.
./etc/bin/intersphinx_reference.py > intersphinx.ref
```

### Pull Request (PR) Process

1. Create a well-documented PR with a description of changes.
1. Request reviews from the the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk) or other maintainers.
1. Respond to feedback and make changes if required.
1. Wait for approval and merging.

## Contacts

If you want to get in contact with us don't hesitate to email the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk).
