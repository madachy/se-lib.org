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

.. autofunction:: selib.context_diagram

critical_path_diagram
------------------------

.. autofunction:: selib.critical_path_diagram

design_structure_matrix
------------------------

.. autofunction:: selib.design_structure_matrix

fault_tree_diagram
------------------------

.. autofunction:: selib.fault_tree_diagram


sequence_diagram
------------------------

.. autofunction:: selib.sequence_diagram

.. _use_case_diagram:

use_case_diagram
------------------------

.. autofunction:: selib.use_case_diagram

wbs_diagram
------------------------

.. autofunction:: selib.wbs_diagram



Analyses
========================

fault_tree_cutsets
------------------------

.. autofunction:: selib.fault_tree_cutsets


Simulations
========================

System Dynamics
------------------------

init_sd_model
^^^^^^^^^^^^ 

.. autofunction:: selib.init_sd_model

add_stock
^^^^^^^^^^^^ 

.. autofunction:: selib.add_stock

add_flow
^^^^^^^^^^^^

.. autofunction:: selib.add_flow

add_auxiliary
^^^^^^^^^^^^
.. autofunction:: selib.add_auxiliary


plot_graph
^^^^^^^^^^^^
.. autofunction:: selib.plot_graph

save_graph
^^^^^^^^^^^^
.. autofunction:: selib.save_graph

run_model
^^^^^^^^^^^^ 
.. autofunction:: selib.run_model


set_logical_run_time
^^^^^^^^^^^^ 
.. autofunction:: selib.set_logical_run_time


get_logical_end_time
^^^^^^^^^^^^ 
.. autofunction:: selib.get_logical_end_time

draw_model_diagram
^^^^^^^^^^^^ 
.. autofunction:: selib.draw_model_diagram
