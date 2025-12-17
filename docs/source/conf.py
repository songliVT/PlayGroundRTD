import importlib.util
assert importlib.util.find_spec("sphinx_design"), "sphinx_design not installed in RTD build"


# Configuration file for the Sphinx documentation builder.

def setup(app):
    app.add_css_file("css/custom.css")

# -- Project information

project = 'PlantscHub'
copyright = '2025, SongLiLab'
author = 'SongLiLab'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    "myst_parser",
    "sphinx_needs",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_design',
]

myst_enable_extensions = [
    "colon_fence",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_theme_options = {
    # Sidebar behavior
    "collapse_navigation": True,   # collapse siblings by default
    "sticky_navigation": True,     # keep sidebar visible on scroll
    "navigation_depth": 3,         # how many levels to show in the nav
    "titles_only": False,          # show page titles + sections
    # Branding (optional)
    "logo_only": False,
    "display_version": False,
}

html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css", # icons
    "css/custom.css"
]

needs_types = [
    dict(directive="publication", title="Publication", prefix="PUB", color="#BFD8D2", style="node"),
]

needs_extra_options = ["category", "doi", "year", "code", "sra"]

needs_default_layout = "clean"

needs_statuses = [
    dict(name="published", description="Published paper", color="#4CAF50"),
]
needs_default_status = "published"

needs_table_classes = ["rtd-exclude-wy-table"]

# Make DOI values clickable (only if they look like real DOIs)
needs_string_links = {
    "doi_link": {
        "regex": r"^(?P<value>10\.\d{4,9}/.+)$",
        "link_url": "https://doi.org/{{value}}",
        "link_name": "{{value}}",
        "options": ["doi"],
    },
    # Code link: if code is a URL, show just the word "Code"
    "code_link": {
        "regex": r"^(?P<value>https?://.+)$",
        "link_url": "{{value}}",
        "link_name": "Code",
        "options": ["code"],
    },
    "sra_link": {
        "regex": r"^(?P<value>(SRP|ERP|DRP)\d+)$",
        "link_url": "https://www.ncbi.nlm.nih.gov/sra/?term={{value}}",
        "link_name": "SRA",
        "options": ["sra"],
    }
}