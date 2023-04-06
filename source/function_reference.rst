.. meta::
   :title: Python Modeling Library (PyML) Function Reference
   :description: Python Modeling Library (PyML) Function Reference
   :keywords: python modeling library, PyML, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation

========================
Function Reference
========================

To use PyML, first import it before using any functions:

.. code-block:: python

   import pyml

These function definitions follow the convention whereby required input parameters are shown first, then optional parameters are shown with an equal sign indicating the default values. A graph here is a generic set of nodes representing system elements connected by edges shown as non-directed or directed lines.

Diagrams
========================

context_diagram
------------------------

.. autofunction:: pyml.context_diagram

critical_path_diagram
------------------------

.. autofunction:: pyml.critical_path_diagram

design_structure_matrix
------------------------

.. autofunction:: pyml.design_structure_matrix

fault_tree_diagram
------------------------

.. autofunction:: pyml.fault_tree_diagram


sequence_diagram
------------------------

.. autofunction:: pyml.sequence_diagram

.. _use_case_diagram:

use_case_diagram
------------------------

.. autofunction:: pyml.use_case_diagram

wbs_diagram
------------------------

.. autofunction:: pyml.wbs_diagram



Analyses
========================

fault_tree_cutsets
------------------------

.. autofunction:: pyml.fault_tree_cutsets


Simulations
========================
