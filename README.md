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

The reference contributor environment is defined in `pyproject.toml` and
managed with `uv`.
This repository is not currently installable as a Python library, so
contributor setup should use `uv` rather than `pip install .` or
`pip install -e .`.

#### `uv` setup (recommended)

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

#### `pixi` setup (completely optional alternative)

If you prefer a conda-first workflow, the repository also provides a
`pixi.toml` manifest. This is a completely optional alternative setup. The
`uv` workflow above remains the reference contributor path and the one mirrored
by the GitHub Pages deploy workflow. A separate build-only GitHub Actions
workflow also exercises the Pixi path.

The Pixi environment is intentionally flat: it installs the documentation,
notebook, mesh tutorial, and development tooling dependencies together in one
environment, using conda-forge packages where available. The current
`pixi.toml` targets the standard Linux, macOS, and Windows platforms.

Install `pixi` if needed, then create the environment:

```bash
pixi install
```

Run the common checks:

```bash
pixi run html
pixi run clean-html
pixi run lint
pixi run linkcheck
```

Use `pixi run html` for incremental rebuilds and `pixi run clean-html` when you
want the same clean HTML build used by the reference `uv` workflow.

### Dependency Policy

- `uv` with `pyproject.toml` remains the reference workflow for contributors
  and the GitHub Pages deploy workflow.
- `pixi.toml` is a completely optional alternative environment definition.
  Keep it working when dependency changes affect the docs or notebook stack;
  the repository also has a build-only GitHub Actions workflow that exercises
  this path.
- Treat these files as environment manifests for this repository, not as a
  signal that the repository is a distributable Python package.
- If dependency updates are needed, update constraints in `pyproject.toml` and,
  when relevant, the corresponding entries in `pixi.toml`.

### Building Training Materials

The training materials are based on [Sphinx](https://www.sphinx-doc.org) and can be built using the provided Makefile on any desired target format. However, we aim to display the content as HTML pages, and any contributions should ensure these are produced correctly.

To build the LFRic Atmosphere training materials in HTML format run the following command:

```bash
# Reference uv workflow without activating .venv:
uv run make clean html

# If you have already activated .venv:
make clean html

# Optional pixi alternatives:
pixi run clean-html
pixi run html
```

With Pixi, `clean-html` matches the clean build above and `html` keeps the
faster incremental rebuild path.

That concludes the process! You’ll find the generated HTML files within the “build” folder.

### Pull Request (PR) Process

1. Create a well-documented PR with a description of changes.
1. Request reviews from the the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk) or other maintainers.
1. Respond to feedback and make changes if required.
1. Wait for approval and merging.

## Contacts

If you want to get in contact with us don't hesitate to email the [Momentum Partnership Team](mailto:Momentum_Partnership@metoffice.gov.uk).
