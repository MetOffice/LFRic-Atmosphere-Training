#!/usr/bin/env python
"""List all intersphinx references available.

Available references configured in `source/conf.py`

> [!WARNING]
> This script contains horrible things which you shouldn't copy
> Unless your _really_ know what you are doing.
"""
import sys
from pathlib import Path
import os
from sphinx.ext.intersphinx._cli import inspect_main

OLD_CWD = Path.cwd()

source = Path(__file__).parent.parent.parent / "source"
os.chdir(source)

sys.path.append(str(source))
from conf import intersphinx_mapping   # NoQA: E402 Legit not at top of file.

for target in intersphinx_mapping.values():
    inspect_main([
        f"{target[0]}/objects.inv"
    ])

os.chdir(OLD_CWD)
