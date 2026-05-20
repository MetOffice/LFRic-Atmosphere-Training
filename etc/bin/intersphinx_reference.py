#!/usr/bin/env python
"""List all intersphinx references available.

Intersphinx references are set in `source/conf.py:intersphinx_mapping`.
This scripts reads that variable and uses the intersphinx script to
provide a list of references one may use in our documentation.

https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html

Suggested usage:

./etc/bin/instersphinx_reference.py > intersphinx.ref
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
