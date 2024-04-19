"""
This is conf.py

Notes
-----

Configuration file for the Sphinx documentation builder.

For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html.

Project information
https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

"""

'''
Basic
'''
project = 'Data Architecture Hub'
project_copyright = '2024, ...'
author = '...'
release = '0.1'




'''
General configuration
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
https://myst-parser.readthedocs.io/en/v0.15.1/sphinx/intro.html#install-a-new-sphinx-extension-and-use-its-functionality
'''
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.mathjax',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    'myst_parser',
    'sphinx_rtd_theme'
]

myst_enable_extensions = [
    'amsmath',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'html_admonition',
    'html_image',
    'replacements',
    'smartquotes',
    'strikethrough',
    'substitution',
    'tasklist',
    'attrs_block',
    'attrs_inline'
]


'''
https://myst-parser.readthedocs.io/en/latest/configuration.html
'''
myst_heading_anchors = 4


'''
Mathematics
'''
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'
myst_dmath_double_inline = True


'''
Paths that contain templates, relative to this directory.
'''
templates_path = ['_templates']


'''
List of patterns, relative to source directory, that match files and
directories to ignore when looking for source files.
This pattern also affects html_static_path and html_extra_path.
'''
exclude_patterns = []


'''
Options for HTML output
https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
'''

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

html_css_files = ['css/generic.css',
                  'css/figures.css',
                  'https://unpkg.com/tabulator-tables/dist/css/tabulator.min.css']

html_js_files = ['https://code.jquery.com/jquery-3.7.0.min.js',
                 'https://code.highcharts.com/stock/highstock.js',
                 'https://code.highcharts.com/stock/modules/data.js',
                 'https://code.highcharts.com/stock/modules/exporting.js',
                 'https://code.highcharts.com/stock/modules/export-data.js',
                 'https://code.highcharts.com/stock/modules/accessibility.js',
                 'https://code.highcharts.com/highcharts.js',
                 'https://code.highcharts.com/modules/networkgraph.js',
                 'https://viewer.diagrams.net/js/viewer-static.min.js'
                 ]

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#343131',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_logo = ''
