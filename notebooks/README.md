# Local Notebook Content

This directory stores notebook material used directly by the training repository.

## Mesh tutorials

- Local copy path: `notebooks/iris-mesh-tutorial/`
- Upstream source: <https://github.com/scitools-classroom/iris-mesh-tutorial>
- The training docs page that points to this material is:
  `source/mesh_overview/exercises/practical_exercises.rst`

The copy in this repository is intended for stable delivery in training.
LFRic-specific adaptations can be made here, while general improvements should
also be proposed upstream.

## Scope of this training copy

This repository copy uses a conda-first setup for regridding practicals.
Use conda to provide the ESMF backend (`esmpy`), then install project extras.
