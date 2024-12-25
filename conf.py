# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------import os
from tkinter import PhotoImage

# Obtenir le chemin absolu du dossier contenant le script ou l'exécutable
base_path = os.path.dirname(os.path.abspath(__file__))

# Construire le chemin complet vers l'image
image_path = os.path.join(base_path, 'resources', 'logo.png')

# Charger l'image
image = PhotoImage(file=image_path)
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ColorWise'
copyright = '2024, Université de Paris Cité'
author = 'DERMOUCHE Mohammed Ryad'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
