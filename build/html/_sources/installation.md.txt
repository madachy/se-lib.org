---
myst:
  html_meta:
    "description": "Python Modeling Library (PyML) Installation"
    "keywords": "python modeling library, PyML, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation"
---

# Installation

Download the PyML library file [pyml.py](https://github.com/madachy/PyML) and copy it to your local development folder or elsewhere on your Python path. If you use the recommended [Anaconda](https://www.anaconda.com/products/individual) Python distribution it will come with all of the required packages below except for Graphviz and Pdflatex. These are required:

* Python version 3.8 and higher.
* [Graphviz](https://graphviz.org/) is required to generate diagrams. After installing Anaconda, use its Powershell Command Prompt and type ``conda install -c conda-forge python-graphviz``. With other Python environments it can be installed with ``pip install graphviz``. Also see graphviz download or graphviz on PyPI for additional instructions for different platforms.
* The *numpy* package is used for model analysis and plotting features.
* The *matplotlib* package is required to use the graphical functionality of PyML.
* *Pdflatex* is required to compile latex files and generate pdfs. It can be installed for Python or comes with standard latex distributions.

Note that diagrams can still be produced without *graphviz* installed locally by providing the generated dot markup text to online tools. Without *pdflatex*, the latex markup can be copied to other publishing tools such as *Overleaf* for refinement and/or pdf generation.