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

extensions = ['pydata_sphinx_theme',
              'sphinx_toolbox.collapse',
              'sphinxcontrib.quizdown',
              'sphinxcontrib.video']


templates_path = ['_templates']
exclude_patterns = []

# -- layout -----------------------------------------------------------------
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/layout.html#

# Hide the link which shows the rst markup
html_show_sourcelink = False

html_theme_options = {
    "navigation_with_keys": True,
    "use_edit_page_button": True,
    "navbar_end": ["theme-switcher"],
    "logo": {
        "text": "Momentum Training",
        },
    "footer_center": ["show-accessibility"]
}

html_sidebars = {
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
