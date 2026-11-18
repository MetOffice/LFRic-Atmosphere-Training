#!/usr/bin/env bash
# Build the shared Python analysis environment for the training on Isambard 3.
#
# Installs a standalone micromamba and a dated conda environment under
# $LFRIC_PREFIX/conda, next to (but separate from) the lfric-env Spack
# installs. Users activate it with:
#
#   eval "$("$LFRIC_PREFIX/conda/bin/micromamba" shell hook --shell bash)"
#   micromamba activate "$LFRIC_PREFIX/conda/envs/lfric-training-<version>"
#
# Usage: bash etc/isambard3/build-python-env.sh [version]
#   version defaults to today's date, e.g. v2026.09.28.
set -euo pipefail

HERE=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
VERSION=${1:-v$(date +%Y.%m.%d)}
LFRIC_PREFIX=${LFRIC_PREFIX:-$PROJECTDIR/$USER/opt/$(uname -sm | tr ' ' -)}
CONDA_ROOT=$LFRIC_PREFIX/conda
ENV_PREFIX=$CONDA_ROOT/envs/lfric-training-$VERSION
MICROMAMBA=$CONDA_ROOT/bin/micromamba

if [[ -e $ENV_PREFIX ]]; then
    echo "error: $ENV_PREFIX already exists; pick a new version" >&2
    exit 1
fi

if [[ ! -x $MICROMAMBA ]]; then
    mkdir -p "$CONDA_ROOT"
    curl -fsSL "https://micro.mamba.pm/api/micromamba/linux-$(uname -m)/latest" |
        tar -xj -C "$CONDA_ROOT" bin/micromamba
fi

export MAMBA_ROOT_PREFIX=$CONDA_ROOT
"$MICROMAMBA" create --yes --prefix "$ENV_PREFIX" --file "$HERE/environment.yml"

# Record exactly what was installed, for reproducibility.
"$MICROMAMBA" env export --explicit --prefix "$ENV_PREFIX" \
    > "$ENV_PREFIX/conda-explicit.txt"

# Headless rendering defaults: login nodes have no GPU and usually no X display.
mkdir -p "$ENV_PREFIX/etc/conda/activate.d"
cat > "$ENV_PREFIX/etc/conda/activate.d/lfric-training-headless.sh" <<'EOF'
if [[ -z ${DISPLAY:-} ]]; then
    export VTK_DEFAULT_OPENGL_WINDOW=${VTK_DEFAULT_OPENGL_WINDOW:-vtkEGLRenderWindow}
    export EGL_PLATFORM=${EGL_PLATFORM:-surfaceless}
    export GALLIUM_DRIVER=${GALLIUM_DRIVER:-llvmpipe}
    export LIBGL_ALWAYS_SOFTWARE=${LIBGL_ALWAYS_SOFTWARE:-1}
fi
EOF

# Readable (not writable) by the rest of the project group.
chmod -R g+rX,g-w "$CONDA_ROOT"

echo "Built $ENV_PREFIX"
