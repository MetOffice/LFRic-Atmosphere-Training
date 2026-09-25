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
import argparse
from pathlib import Path
import os
from contextlib import redirect_stdout
from io import StringIO
from sphinx.ext.intersphinx._cli import inspect_main
from subprocess import run

OLD_CWD = Path.cwd()

SOURCE = Path(__file__).parent.parent.parent / "source"
os.chdir(SOURCE)
sys.path.append(str(SOURCE))
from conf import intersphinx_mapping   # NoQA: E402 Legit not at top of file.
os.chdir(OLD_CWD)


def parse_args(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--check-for-explicit-links',
        action='store_true',
        help=(
            'Inspect intersphinx inventories directly instead of'
            ' capturing output.'
        ),
    )
    return parser.parse_args(argv)


def capture_intersphinx_reference_output():
    buffer = StringIO()
    with redirect_stdout(buffer):
        for target in intersphinx_mapping.values():
            inspect_main([
                f"{target[0]}/objects.inv"
            ])
    return buffer.getvalue()


def check_links():
    status = 0
    for target in intersphinx_mapping.values():
        url = target[0]
        res = run(['grep', '-r', url, str(SOURCE)], capture_output=True)
        out = [i for i in res.stdout.decode().split('\n') if i]
        if len(out) > 1:
            print(
                f' 😢 URL used {len(out)} times in source - use intersphinx:'
                f'\n    {url}'
            )
            status = 1
    if status == 0:
        print('🎉 No repetition in intersphinx URLs.')
    return status


def main(argv=None):
    args = parse_args(argv)
    if args.check_for_explicit_links:
        return check_links()

    sys.stdout.write(capture_intersphinx_reference_output())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

