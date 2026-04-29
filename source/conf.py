import sys, os 

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

extensions = [
    'sphinx_toolbox.collapse',
    'sphinxcontrib.quizdown',
    'sphinxcontrib.video'
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
html_css_files = ['nav-collapse.css']
html_js_files = ['nav-collapse.js']

linkcheck_ignore = [
    # Ignore anchor ids: https://github.com/sphinx-doc/sphinx/issues/13620
    # TODO: Most of these should be fixable later.by removing refs to
    # trac;
    r'https?:\/\/code.metoffice.gov.uk.*#.*',
]
