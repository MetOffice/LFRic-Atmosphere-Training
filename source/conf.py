import sys
import os

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
html_css_files = ['nav-collapse.css', 'admonitions.css']
html_js_files = ['nav-collapse.js']

# These URLs are valid learner-facing targets, but cannot be checked reliably
# from public CI: Cylc Review is an internal hostname and the OASIS site serves
# an incomplete certificate chain to Python/OpenSSL linkcheck clients.
linkcheck_ignore = [
    r'https://cylchub/.*',
    r'https://oasis\.cerfacs\.fr/.*',
    'https://github.com/MetOffice/jules',       # not fully public yet :(
    'https://cylchub/*',                        # inaccessible from GH Actions
    'https://github.com/MetOffice/momentum_user_training.example*',
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
