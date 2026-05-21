#!/usr/bin/env python3
"""Execute every tutorial notebook headlessly and render an HTML sidecar.

The source ``.ipynb`` files are never modified: ``nbconvert`` reads each one,
executes it in memory, and writes ``<name>.html`` into ``_build/html/``. The
process exits non-zero if *any* notebook raises, so this also serves as the CI
smoke test for the notebooks.
"""
from __future__ import annotations

import os
import platform
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
NB_DIR = HERE / "notebooks"
OUT_DIR = HERE / "_build" / "html"
KERNEL = "python3"
CELL_TIMEOUT = "900"


def headless_env() -> dict[str, str]:
    """Environment for the kernel: off-screen, static, no display required."""
    env = os.environ.copy()
    env.setdefault("PYVISTA_OFF_SCREEN", "true")
    env.setdefault("PYVISTA_JUPYTER_BACKEND", "static")
    env.setdefault("MPLBACKEND", "Agg")
    if platform.system() == "Linux" and not env.get("DISPLAY"):
        # No X display: render with Mesa software GL (the `mesalib` conda dep)
        # through a surfaceless EGL context, so neither an X server nor a GPU is
        # required. (CI sets a virtual DISPLAY instead and uses GLX, skipping
        # this branch.)
        env.setdefault("VTK_DEFAULT_OPENGL_WINDOW", "vtkEGLRenderWindow")
        env.setdefault("EGL_PLATFORM", "surfaceless")
        env.setdefault("GALLIUM_DRIVER", "llvmpipe")
        env.setdefault("LIBGL_ALWAYS_SOFTWARE", "1")
        env.setdefault("EGL_LOG_LEVEL", "fatal")
    return env


def ensure_kernel() -> None:
    """Register an env-local ``python3`` kernelspec so notebooks pinned to other
    kernel names (e.g. ``lfric-mesh``) still execute against this environment."""
    subprocess.run(
        [sys.executable, "-m", "ipykernel", "install", "--sys-prefix",
         "--name", KERNEL, "--display-name", "Python 3 (iris-mesh-tutorial)"],
        check=False,
    )


def main() -> int:
    notebooks = sorted(NB_DIR.glob("*.ipynb"))
    if not notebooks:
        print(f"No notebooks found in {NB_DIR}", file=sys.stderr)
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_kernel()
    env = headless_env()

    failures: list[str] = []
    for nb in notebooks:
        print(f"\n=== executing {nb.name} ===", flush=True)
        cmd = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "html",
            "--execute",
            "--output-dir", str(OUT_DIR),
            f"--ExecutePreprocessor.kernel_name={KERNEL}",
            f"--ExecutePreprocessor.timeout={CELL_TIMEOUT}",
            str(nb),
        ]
        if subprocess.run(cmd, env=env).returncode != 0:
            failures.append(nb.name)
            print(f"--- FAILED: {nb.name}", flush=True)

    passed = len(notebooks) - len(failures)
    print(f"\n==== {passed}/{len(notebooks)} notebooks succeeded ====")
    for name in failures:
        print(f"  FAILED  {name}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
