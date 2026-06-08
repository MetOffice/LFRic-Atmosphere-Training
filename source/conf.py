import sys
import os
from collections.abc import Mapping
from types import MappingProxyType

from docutils import nodes
from sphinx.application import Sphinx
from sphinx.errors import ExtensionError

sys.path.append(os.path.abspath('../lib/'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Momentum Training - LFRic'
copyright = 'Met Office'
author = 'Met Office'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Keep pydata_sphinx_theme out of extensions. It is selected below with
# html_theme; loading it as a general extension also runs its HTML-only hooks
# for non-HTML builders such as linkcheck, where app.builder.theme is absent.
extensions = [
    'sphinx_design',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx_toolbox.collapse',
    'sphinxcontrib.quizdown',
    'sphinxcontrib.video',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Figure numbering --------------------------------------------------------
numfig = True


def validate_figure_labelling(
    app: Sphinx,
    doctree: nodes.document,
    *,
    unnumbered_images_by_doc: Mapping[str, frozenset[str]] = MappingProxyType({
        'index': frozenset({'_static/momentum_logo.png'}),
    }),
) -> None:
    """Enforce the site-wide figure labelling policy.

    Content figures should have consistent numbering, captions, cross-reference
    targets, and accessible descriptions. Sphinx can number figures once
    ``numfig`` is enabled, but only if content uses ``figure`` directives with
    explicit labels and captions.

    This hook runs while Sphinx reads each doctree and fails the build when:

    * a ``figure`` directive has no ``fig-*`` label;
    * a ``figure`` directive has no caption; or
    * an image-backed ``figure`` directive has no alt text; or
    * an unallowlisted ``image`` directive remains outside a figure.

    ``unnumbered_images_by_doc`` intentionally defaults to an immutable narrow
    allowlist for decorative images that should not be numbered. Keys are Sphinx
    docnames and values are normalized image URIs.
    """

    def node_location(node: nodes.Node) -> str:
        location = getattr(node, 'source', '<unknown source>')
        line = getattr(node, 'line', None)
        return f'{location}:{line}' if line else location

    def image_uri(image: nodes.image) -> str:
        return image.get('uri', '').lstrip('/')

    errors: list[str] = []

    for figure in doctree.findall(nodes.figure):
        image = next(figure.findall(nodes.image), None)
        uri = image_uri(image) if image else '<missing image>'
        names = figure.get('names', [])
        if not any(name.startswith('fig-') for name in names):
            errors.append(
                f"{node_location(figure)}: figure for '{uri}' is missing "
                "a '.. _fig-<name>:' label (placed above the figure)."
            )
        if not any(isinstance(child, nodes.caption) and child.astext().strip()
                   for child in figure.children):
            errors.append(
                    f"{node_location(figure)}: figure for '{uri}' is missing "
                'a caption.'
            )
        if image is not None and not image.get('alt', '').strip():
            errors.append(
                f"{node_location(figure)}: figure for '{uri}' is missing "
                'alt text.'
            )

    for image in doctree.findall(nodes.image):
        if isinstance(image.parent, nodes.figure):
            continue
        uri = image_uri(image)
        allowed = unnumbered_images_by_doc.get(app.env.docname, frozenset())
        if uri not in allowed:
            errors.append(
                f"{node_location(image)}: image directive for '{uri}' must "
                'be converted to a labelled figure or explicitly allowlisted.'
            )

    if errors:
        message = 'Figure labelling validation failed:\n'
        message += '\n'.join(f'- {error}' for error in errors)
        raise ExtensionError(message)


def setup(app: Sphinx) -> dict[str, str | bool]:
    """Register local Sphinx validation hooks."""
    app.connect('doctree-read', validate_figure_labelling)
    return {'version': '1.0', 'parallel_read_safe': True}

# -- layout -----------------------------------------------------------------
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#

# Hide the link which shows the rst markup
html_show_sourcelink = False

html_theme_options = {
    "navigation_with_keys": True,
    "use_edit_page_button": True,
    # Keep the header minimal: branding + utilities only.
    "navbar_start": ["navbar-logo"],
    "navbar_center": [],
    "navbar_end": ["search-button", "theme-switcher"],
    # Expand navigation in the left sidebar so top-level sections are visible.
    "show_nav_level": 3,
    # Keep section trees visible in the sidebar (collapsible), instead of
    # collapsing everything to the current page context.
    "collapse_navigation": False,
    "logo": {
        "text": "Momentum Training",
        },
    "footer_center": ["show-accessibility"],
    # Remove the right-side "On this page" panel globally.
    "secondary_sidebar_items": []
}

html_sidebars = {
    # Use a global site navigation tree on the left for all pages.
    "**": ["globaltoc.html"],
    "index": []
}

# Provides the Edit on GitHub link in the generated docs.
html_context = {
    "display_github": True,
    "github_user": "MetOffice",
    "github_repo": "LFRic-Atmosphere-Training",
    "github_version": "main",
    "doc_path": "source"
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_css_files = ['nav-collapse.css', 'accessibility.css']
html_js_files = ['nav-collapse.js', 'accessibility.js']

# These URLs are valid learner-facing targets, but cannot be checked reliably
# from public CI: Cylc Review is an internal hostname and the OASIS site serves
# an incomplete certificate chain to Python/OpenSSL linkcheck clients.
linkcheck_ignore = [
    # an example (but non-existing) link appears in
    # source/lfric_infrastructure/practical_stem_test.rst
    'https://github.com/MetOffice/momentum_user_training.example_lfric_workflow/issues/2',
    # anti-bot checks can intermittently return 415 in CI
    r'^https?://abilitynet\.org\.uk(?:/.*)?$',
    # inaccessible from GH Actions, probably anti-bot
    r'^https?://agupubs\.onlinelibrary\.wiley\.com(?:/.*)?$',
    # internal to Met Office
    r'^https?://cylchub(?:/.*)?$',
    # private repos
    r'^https?://github\.com/MetOffice/jules(?:/.*)?$',
    r'^https?://github\.com/MetOffice/LFRic-Atmosphere-Training(?:/.*)?$',
    # opening in Chrome is OK, but in Python it would complain
    # "unable to get local issuer certificate".
    # Possibly related to certifi
    r'^https?://oasis\.cerfacs\.fr(?:/.*)?$',
    r'^https://www.sciencedirect.com/science/article/pii/S0743731518305306$',
    r^'https?://code\.metoffice\.gov\.uk(?:/.*)?$'
]

# Add hyperlinks include file to avoid repeated links.
rst_epilog = open('hyperlinks.rst.include', 'r').read()

# Mapping to other Sphinx projects we want to import references from.
intersphinx_mapping = {
    'cylc': (
        'https://cylc.github.io/cylc-doc/stable/html', None
    ),
    'rose': (
        'http://metomi.github.io/rose/doc/html', None
    ),
    'simulation_systems': (
        'https://metoffice.github.io/simulation-systems/', None
    ),
    'psyclone': (
        'https://psyclone.readthedocs.io/en/stable/', None
    ),
}
