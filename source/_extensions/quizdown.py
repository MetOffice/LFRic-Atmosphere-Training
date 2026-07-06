"""
Vendored Sphinx quizdown extension.

This file is based on ``sphinxcontrib-quizdown`` version 0.3 at commit
``d9f24a7a2305ad5b196e06597b1779c9414d1d85``.

Original copyright:
Copyright 2021 by Malte Bonart <malte@spiced-academy.com>

Original licence text is retained in
``source/_extensions/licenses/sphinxcontrib-quizdown-LICENSE.txt``.
"""

import html
import json

from docutils import nodes
from sphinx.util.docutils import SphinxDirective


class Quizdown(SphinxDirective):
    """Implement the ``quizdown`` directive."""

    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        if self.arguments:
            rel_filename, filename = self.env.relfn2path(
                self.arguments[0].strip()
            )
            self.env.note_dependency(rel_filename)
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    quizdown_text = file.read()
            except (IOError, OSError):
                return [self.state.document.reporter.warning(
                    'External quizdown file %r not found or reading '
                    'it failed' % filename,
                    line=self.lineno,
                )]
        else:
            quizdown_text = '\n'.join(self.content)
            if not quizdown_text.strip():
                return [self.state_machine.reporter.warning(
                    'Ignoring "quizdown" directive without content.',
                    line=self.lineno,
                )]

        html_raw = '<div class="quizdown">{code}</div>'.format(
            code=html.escape(quizdown_text)
        )
        return [nodes.raw(html_raw, html_raw, format='html')]


def add_quizdown_lib(app, pagename, templatename, context, doctree):
    quizdown_js = app.config.quizdown_config.setdefault(
        'quizdown_js',
        'vendor/quizdown/quizdown.js',
    )

    app.add_js_file(quizdown_js)
    config_json = json.dumps(app.config.quizdown_config)
    app.add_js_file(None, body=f'quizdown.init({config_json});')


def setup(app):
    app.add_directive('quizdown', cls=Quizdown)
    app.add_config_value('quizdown_config', {}, 'html')
    app.connect('html-page-context', add_quizdown_lib)
    return {
        'version': '0.3-vendored',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
