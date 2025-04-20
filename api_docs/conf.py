project = "gdsfactory API Documentation"
author = "gdsfactory contributors"
release = "1.0.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "matplotlib.sphinxext.plot_directive",
    "sphinx_markdown_builder"
]

exclude_patterns = ["api", "Thumbs.db", ".DS_Store"]
plot_formats = ["png"]