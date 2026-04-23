# AGENTS.md

## Purpose

This repository publishes the LFRic Atmosphere self-learning training site.
It is primarily a Sphinx documentation project with a bundled copy of the
`iris-mesh-tutorial` notebooks for learner delivery.

## Repository map

- `README.md`: contributor setup, dependency policy, and the canonical local
  build instructions.
- `pyproject.toml`: reference dependency manifest for the `uv` workflow and CI.
  This repository is not currently installable as a Python library. Do not add
  `requirements.txt` files or commit lockfiles here.
- `pixi.toml`: completely optional conda-first alternative environment
  definition. Keep it aligned with the docs and notebook stack when relevant,
  but treat `uv` as the reference workflow unless the user explicitly asks to
  prefer Pixi.
- `Makefile`: thin wrapper around `sphinx-build -M ...`.
- `source/`: Sphinx documentation sources.
- `source/index.rst`: root toctree for the published training site.
- `source/conf.py`: Sphinx extensions, theme settings, GitHub edit links, and
  custom static assets.
- `source/_static/`: images, CSS, JS, and video referenced by the docs.
- `source/_templates/`: custom sidebar/footer templates.
- `notebooks/iris-mesh-tutorial/`: local training-delivery copy of the upstream
  `scitools-classroom/iris-mesh-tutorial` project.
- `.github/workflows/deploy_pages.yml`: CI path used for the published site.

## Environment and setup

- Supported Python is `>=3.11,<3.13`; GitHub Pages CI currently builds with
  Python `3.11`.
- Preferred docs setup:

  ```bash
  uv sync --python 3.11
  source .venv/bin/activate
  ```

- Optional Pixi setup:

  ```bash
  pixi install
  pixi run html
  ```

- Optional extras are defined in `pyproject.toml`:
  - `dev` for contributor tooling such as `pre-commit`
  - `notebooks` for local notebook work
  - `mesh_tutorials` for the bundled mesh tutorial workflow
- `pixi.toml` intentionally flattens these into one optional environment
  instead of mirroring the `pyproject.toml` extras one-for-one. Keep the
  matching version constraints aligned across the two files when relevant.
- Some matching constraints are written differently because the tools use
  different version-spec syntaxes. In particular, Pixi / Conda-style entries
  such as `0.5.3.*` and `1.14.4.*` are the tooling-compatible form of the same
  effective pin represented in `pyproject.toml` as `==0.5.3` and `==1.14.4`;
  treat that as a syntax difference, not a real environment difference.
- Although `pyproject.toml` contains `[project]` metadata, the repository is
  not currently an installable Python package. Do not recommend
  `pip install .` or `pip install -e .` as the normal setup route.
- The mesh tutorial regridding practicals need `esmpy`. The repository
  currently references it in `notebooks/README.md`, the bundled mesh tutorial
  setup instructions, `source/mesh_overview/exercises/practical_exercises.rst`,
  and the Pixi `mesh-import-check` task. GitHub Pages CI does not install or
  use `esmpy`; the deploy workflow still builds with `uv sync` and
  `uv run make clean html`.
- The regridding package name differs by ecosystem: use `esmf-regrid` for the
  PyPI / `pyproject.toml` dependency and `iris-esmf-regrid` for the Conda /
  `pixi.toml` dependency.
- `sphinxcontrib-quizdown` is not available on conda-forge. Keep it under
  Pixi's `[pypi-dependencies]` as a Git-sourced package rather than moving it
  into `[dependencies]`.
- Dependency policy in `README.md` is explicit: `uv` remains the reference
  workflow, while `pixi.toml` is an optional alternative.

## Editing guidance

- Keep changes learner-focused and introductory. The audience is new to LFRic
  Atmosphere and related workflows.
- Most content is authored in reStructuredText. Preserve heading hierarchy,
  directive indentation, and existing toctree structure.
- When adding or moving pages, update the relevant `index.rst` or other
  containing toctree so the page is reachable in the built site.
- Put new images or downloadable static assets in `source/_static/` and
  reference them from the relevant `.rst` page.
- If you change navigation or page chrome, inspect the full set of related
  files together:
  - `source/conf.py`
  - `source/_templates/globaltoc.html`
  - `source/_templates/show-accessibility.html`
  - `source/_static/nav-collapse.css`
  - `source/_static/nav-collapse.js`
- Notebook content under `notebooks/iris-mesh-tutorial/notebooks/` is stored as
  plain `.ipynb` files, not as paired Jupytext sources.
- Keep notebook diffs tight. Avoid unnecessary execution-count churn or large
  output blobs unless the output is intentionally part of the training
  material.
- Helper code for the mesh tutorial lives under
  `notebooks/iris-mesh-tutorial/notebooks/support/`.
- The mesh tutorial copy is downstream training material. Keep LFRic-specific
  adaptations in this repository, but treat generic improvements as upstream
  candidates for `scitools-classroom/iris-mesh-tutorial`.

## Validation

- Standard local validation for doc changes:

  ```bash
  uv run make clean html
  ```

- Useful extra checks when touching RST structure or links:

  ```bash
  uv run sphinx-lint source
  uv run make linkcheck
  ```

- The deployed site is built from `main` by GitHub Actions using:

  ```bash
  uv sync
  uv run make clean html
  ```

- For notebook changes, there is no dedicated notebook CI in this repository.
  Smoke-test the changed notebook or helper code locally where practical.
- For the mesh tutorial, launch Jupyter from
  `notebooks/iris-mesh-tutorial/notebooks/` so local paths and imports match
  the training instructions.

## Working norms for agents

- Prefer small, reviewable documentation edits over broad rewrites.
- Match existing terminology: "Momentum", "LFRic Atmosphere", "science
  configurations", and "working practices" all have established meanings in the
  training content.
- Do not change dependency-management conventions casually. If new dependencies
  are necessary, update `pyproject.toml` and keep the README setup instructions
  consistent with that change. If the change also affects the optional Pixi
  environment, update `pixi.toml` too.
- Do not add packaging boilerplate or treat this repository as a distributable
  Python library unless the user explicitly asks for that change.
- Do not commit generated `build/` output, virtual environments, or notebook
  checkpoint files; those are already ignored.
