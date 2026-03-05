# iris-mesh-tutorial (LFRic Atmosphere Training copy)

This directory is a local training-delivery copy of:
<https://github.com/scitools-classroom/iris-mesh-tutorial>

Use this copy through the LFRic Atmosphere training guidance in:

- `source/mesh_overview/exercises/practical_exercises.rst`

## Learner quick start (this repository)

From the `LFRic-Atmosphere-Training` repository root:

```bash
conda create -n lfric-mesh python=3.12 -y
conda activate lfric-mesh
conda install -c conda-forge esmpy -y
pip install -e .[mesh_tutorials]
python -m ipykernel install --user --name lfric-mesh --display-name "Python (lfric-mesh)"
cd notebooks/iris-mesh-tutorial/notebooks
jupyter lab
```

## Directory layout

- `notebooks/`: learner-facing notebooks, ordered numerically
- `notebooks/support/`: helper scripts and assets used by notebooks
- `example_data/`: required input netCDF data

This training copy includes regridding practicals.
For `04_Regridding.ipynb`, `06_Exercise_01.ipynb` and `07_Exercise_02.ipynb`,
use the `Python (lfric-mesh)` kernel created above.

See `notebooks/README.md` for a detailed learner vs maintainer file map.

## Notes for maintainers

- Keep LFRic-specific training adaptations in this repository.
- Propose generic improvements back to upstream where appropriate.
- The supported training workflow here is `uv`.
