==============
Home
==============

Introduction
==============


.. meta::
   :title: Python Modeling Library (PyML)
   :description: Python Modeling Library (PyML)
   :keywords: python modeling library, PyML, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation, continuous systems


Welcome to the Python Modeling Library (PyML) for systems modeling, analysis, documentation and code generation. It includes the SysML and UML modeling languages with additional capabilities enabling advanced analysis with Python libraries and language features. PyML is built with Graphviz, Matplotlib, NetworkX, NumPy and SciPy using Python as glue code with all systems modeling. It's fun to be powerful with Python.

**New Online Capability and Simulation**

The upcoming PyML v.20 can run online in a browser. Try it at the `SysML Diagram Scratchpad <http://pyml.fun/online/scratchpad.html>`_. We are also adding system dynamics modeling and simulation capability. Preview some features online at `System Dynamics Demonstrations <http://pyml.fun/online/system_dynamics.html>`_.

Inputs and Outputs
-------------------

The diagram below shows the primary inputs and outputs of PyML. This diagram was generated with PyML utilities.

.. image:: images/pyml_input_output_diagram.svg
  :width: 500

						   
			

Current Features
==================

This early release of PyML contains library functions for the following:

* Activity diagrams
* :ref:`Context diagram<context_diagram>`
* :ref:`Critical path network diagram<critical_path_diagram>`
* :ref:`Design Structure Matrix (DSM)<design_structure_matrix>`
* :ref:`Fault Tree Diagram<fault_tree_diagram>`
* :ref:`Fault Tree Cutset Analysis<fault_tree_cutsets>`
* Latex and PDF document generation utilities
* :ref:`Use case diagram<use_case_diagram>`
* :ref:`Sequence diagram<sequence_diagram>`
* :ref:`Work Breakdown Structure (WBS) diagram<wbs_diagram>`


Feedback
==================

We value your feedback.  Tell us how we can make PyML, its documentation and this website more useful. Please send comments, suggestions and interest in supporting the development to `info@pyml.fun <mailto:info@pyml.fun>`_.


Citation references, like [CIT2002]_.
Note that citations may get
rearranged, e.g., to the bottom of
the "page".
.. [CIT2002] A citation
   (as often used in journals).

Definition lists:

what
  Definition lists associate a term with
  a definition.

how
  The term is a one-line phrase, and the
  definition is one or more paragraphs or
  body elements, indented relative to the
  term. Blank lines are not allowed
  between term and definition.

link a term to def :term:`Sphinx`

link to a term in the glossary while showing different text  :term:`reStructuredText<RST>`

glosssary


.. glossary::

    Sphinx
      Sphinx is a tool that makes it easy to create intelligent and beautiful documentation. It was originally created for the Python documentation, and it has excellent facilities for the documentation of software projects in a range of languages.

    RST
      |RST| is an easy-to-read, what-you-see-is-what-you-get plain text markup syntax and parser system. It is useful for in-line program documentation (such as Python docstrings), for quickly creating simple web pages, and for standalone documents. |RST| is designed for extensibility for specific application domains. The |RST| parser is a component of Docutils.
