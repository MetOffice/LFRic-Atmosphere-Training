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

[`uv`](https://docs.astral.sh/uv/) is the recommended tool for Python environment and dependency management in this repository.
Dependencies for building the training pages and running the tutorial notebooks are defined in `pyproject.toml`.
Environment lockfiles are intentionally not used in this repository.
This keeps setup flexible across operating systems and CPU architectures while still using the same dependency constraints.

If you cannot use `uv`, the repository can also be set up with `venv` and `pip`.

Create and activate a virtual environment:

```bash
/path/to/python3.11+ -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install .
```

Optional dependency groups can also be installed when available:

```bash
pip install ".[notebooks,dev]"
```

If you are contributing to this repository and want an editable install:

```bash
pip install -e ".[notebooks,dev]"
```

Install `uv` if needed:

```bash
python3 -m pip install --user uv
```

Create or update the project virtual environment:

```bash
uv sync --python 3.11
```
If you want to work with the tutorial notebooks, install the optional
dependencies as well: `uv sync --extra notebooks`

For development tools (e.g., pre-commit hooks), install: `uv sync --extra dev`

Now activate the virtual environment:

```bash
source .venv/bin/activate
```

If you prefer not to activate the environment, run commands with `uv run ...` instead.

### Dependency Policy

- Build environments from `pyproject.toml` only.
- Do not commit or use `.lock` files for Python environments in this repository.
- If dependency updates are needed, update constraints in `pyproject.toml` and recreate the environment with `uv sync`.

### Building Training Materials

The training materials are based on [Sphinx](https://www.sphinx-doc.org) and can be built using the provided Makefile on any desired target format. However, we aim to display the content as HTML pages, and any contributions should ensure these are produced correctly.

To build the LFRic Atmosphere training materials in HTML format run the following command:

```bash
uv run make clean html
```

That concludes the process! You’ll find the generated HTML files within the “build” folder.

### Pull Request (PR) Process

1. Create a well-documented PR with a description of changes.
1. Request reviews from the the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk) or other maintainers.
1. Respond to feedback and make changes if required.
1. Wait for approval and merging.

## Contacts

If you want to get in contact with us don't hesitate to email the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk).
