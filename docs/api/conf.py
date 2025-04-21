import sys
import os

sys.path.insert(0, os.getcwd())
extensions = [
    "sphinx_ext_mystmd", 
    "sphinx.ext.autodoc", 
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "matplotlib.sphinxext.plot_directive",
    "sphinx.ext.napoleon"
]
exclude_patterns = [".*", "_build"]
numfig = True

plot_formats = [('png', 90)]
highlight_language = 'python'