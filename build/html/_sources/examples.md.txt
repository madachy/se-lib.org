---
myst:
  html_meta:
    "description": "Systems Engineering Library (se-lib) Examples"
    "keywords": "se-lib, systems engineering, system modeling, python modeling library, PyML, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation"
---

## Examples

These examples generate diagrams to be displayed from a Python console or Jupyter Notebook.  After importing se-lib, model elements can be specified as simple lists.  Element relationships are designated as lists of tuple pairs. The output filenames are optional and used here to generate the included SVG images.
 
### Use Case Model

Actors and use cases are first specified in lists.  The interactions between actors and use cases are identified by their tuple pairs and drawn accordingly on the diagram.
   
```{code-block} python
import selib as se

# system model
system_name = "Course Portal"
actors = ['Student', 'Instructor']
use_cases = ['Post Discussion', 'Take Quiz', 'Create Quiz']
interactions = [('Student', 'Post Discussion'), ('Instructor', 'Post Discussion'), ('Student', 'Take Quiz'), ('Instructor', 'Create Quiz')]
use_case_relationships = []

# create diagram
se.use_case_diagram(system_name, actors, use_cases, interactions, use_case_relationships, filename=system_name+'use case diagram.pdf')
 ```
 
<div style="text-align: center">
<object data="_images/Course_Portal_use_case_diagram.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{Course_Portal_use_case_diagram.svg}
```


### Sequence Model
 
A sequence diagram can be constructed per the following.

```
# system model
system_name = "Battle Simulator"
actors = ['Battle Planner']
objects = ['main']
actions = [
('Battle Planner', 'main', 'run()'),
('main', 'Battle Planner', 'request for side 1 name'),
('Battle Planner', 'main', 'side 1 name'),
('main', 'Battle Planner', 'request for side 2 name'),
('Battle Planner', 'main', 'side 2 name'),
('main', 'Battle Planner', 'request for side 1 starting level'),
('Battle Planner', 'main', 'side 1 starting level'),
('main', 'Battle Planner', 'request for side 1 lethality coefficient'),
('Battle Planner', 'main', 'side 1 lethality coefficient'),
('main', 'Battle Planner', 'request for side 2 starting level'),
('Battle Planner', 'main', 'side 2 starting level'),
('main', 'Battle Planner', 'request for side 2 lethality coefficient'),
('Battle Planner', 'main', 'side 2 lethality coefficient'),
('main', 'Battle Planner', 'time history of troops and victor'),
]

# create diagram
se.sequence_diagram(system_name, actors, objects, actions, filename=system_name+"_sequence_diagram")
```

<div style="text-align: center">
<object data="_images/Battle_Simulator_sequence_diagram.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{Battle_Simulator_sequence_diagram.svg}
```

### Context Model

```
# system model
system_name = "Python Interpreter with PyML"
external_actors = ["User", "OS", "Graphviz"]
# create context diagram
se.context_diagram(system_name, external_actors, filename="pyml_context_diagram_offline")
```

<div style="text-align: center">
<object data="_images/pyml_context_diagram_offline.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{pyml_context_diagram_offline.svg}
```

### Work Breakdown Structure

```
# project work breakdown structure
wbs_decompositions = [
('Skateboard', 'Hardware'), ('Skateboard', 'Software'), ('Skateboard', 'Integration and Test'),
                ('Hardware', 'Board'), ('Hardware', 'Wheels'), ('Hardware', 'Mounting'),
                ('Software', 'OS'), ('Software', 'GPS Driver'), ('Software', 'Route Tracking'),
                ('Integration and Test', 'Fixed Platform'), ('Integration and Test', 'Street Testing')]

# create diagram
se.wbs_diagram(wbs_decompositions, filename="skateboard_wbs")
```

<div style="text-align: center">
<object width="700px" data="_images/skateboard_wbs.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{skateboard_wbs.svg}
```

### Critical Path Analysis

A critical path can be computed from a set of tasks with associated time durations and dependencies as below.

```
# tasks, durations and dependencies
tasks = [('A', {'Duration': 3}),
         ('B', {'Duration': 5}),
         ('C', {'Duration': 2}),
         ('D', {'Duration': 3}),
         ('E', {'Duration': 5})]

task_dependencies = [('A', 'C'),
                ('B', 'C'),
                ('A', 'D'),
                ('C', 'E'),
                ('D', 'E')]

# create diagram
se.critical_path_diagram(tasks, task_dependencies, filename="critical_path")
```

<div style="text-align: center">
<object data="_images/critical_path.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{critical_path.svg}

```   

### Design Structure Matrix

```
tasks = ['Make Board', 'Acquire Wheels', 'Assemble', 'Test']
task_dependencies = [('Make Board', 'Assemble'), ('Acquire Wheels', 'Assemble'), ('Assemble', 'Test'), ('Test', 'Assemble')]
se.design_structure_matrix(tasks, task_dependencies, filename="skateboard_task_dsm_with_feedback")
```


<div style="text-align: center">
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<!-- Generated by graphviz version 2.40.1 (20161225.0304)
 -->
<!-- Title: dsm Pages: 1 -->
<svg width="387pt" height="121pt"
 viewBox="0.00 0.00 387.00 121.00" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<g id="graph0" class="graph" transform="scale(1 1) rotate(0) translate(4 117)">
<title>dsm</title>
<polygon fill="#ffffff" stroke="transparent" points="-4,4 -4,-117 383,-117 383,4 -4,4"/>
<!-- dsm -->
<g id="node1" class="node">
<title>dsm</title>
<polygon fill="none" stroke="#000000" points="8.5,-87.5 8.5,-108.5 105.5,-108.5 105.5,-87.5 8.5,-87.5"/>
<polygon fill="none" stroke="#000000" points="105.5,-87.5 105.5,-108.5 181.5,-108.5 181.5,-87.5 105.5,-87.5"/>
<text text-anchor="start" x="108.5" y="-94.3" font-family="Times,serif" font-size="14.00" fill="#000000">Make Board</text>
<polygon fill="none" stroke="#000000" points="181.5,-87.5 181.5,-108.5 278.5,-108.5 278.5,-87.5 181.5,-87.5"/>
<text text-anchor="start" x="184.5" y="-94.3" font-family="Times,serif" font-size="14.00" fill="#000000">Acquire Wheels</text>
<polygon fill="none" stroke="#000000" points="278.5,-87.5 278.5,-108.5 340.5,-108.5 340.5,-87.5 278.5,-87.5"/>
<text text-anchor="start" x="281.5" y="-94.3" font-family="Times,serif" font-size="14.00" fill="#000000">Assemble</text>
<polygon fill="none" stroke="#000000" points="340.5,-87.5 340.5,-108.5 371.5,-108.5 371.5,-87.5 340.5,-87.5"/>
<text text-anchor="start" x="343.5" y="-94.3" font-family="Times,serif" font-size="14.00" fill="#000000">Test</text>
<polygon fill="none" stroke="#000000" points="8.5,-66.5 8.5,-87.5 105.5,-87.5 105.5,-66.5 8.5,-66.5"/>
<text text-anchor="start" x="22" y="-73.3" font-family="Times,serif" font-size="14.00" fill="#000000">Make Board</text>
<polygon fill="#000000" stroke="transparent" points="105.5,-66.5 105.5,-87.5 181.5,-87.5 181.5,-66.5 105.5,-66.5"/>
<polygon fill="none" stroke="#000000" points="105.5,-66.5 105.5,-87.5 181.5,-87.5 181.5,-66.5 105.5,-66.5"/>
<polygon fill="none" stroke="#000000" points="181.5,-66.5 181.5,-87.5 278.5,-87.5 278.5,-66.5 181.5,-66.5"/>
<polygon fill="none" stroke="#000000" points="278.5,-66.5 278.5,-87.5 340.5,-87.5 340.5,-66.5 278.5,-66.5"/>
<polygon fill="none" stroke="#000000" points="340.5,-66.5 340.5,-87.5 371.5,-87.5 371.5,-66.5 340.5,-66.5"/>
<polygon fill="none" stroke="#000000" points="8.5,-45.5 8.5,-66.5 105.5,-66.5 105.5,-45.5 8.5,-45.5"/>
<text text-anchor="start" x="11.5" y="-52.3" font-family="Times,serif" font-size="14.00" fill="#000000">Acquire Wheels</text>
<polygon fill="none" stroke="#000000" points="105.5,-45.5 105.5,-66.5 181.5,-66.5 181.5,-45.5 105.5,-45.5"/>
<polygon fill="#000000" stroke="transparent" points="181.5,-45.5 181.5,-66.5 278.5,-66.5 278.5,-45.5 181.5,-45.5"/>
<polygon fill="none" stroke="#000000" points="181.5,-45.5 181.5,-66.5 278.5,-66.5 278.5,-45.5 181.5,-45.5"/>
<polygon fill="none" stroke="#000000" points="278.5,-45.5 278.5,-66.5 340.5,-66.5 340.5,-45.5 278.5,-45.5"/>
<polygon fill="none" stroke="#000000" points="340.5,-45.5 340.5,-66.5 371.5,-66.5 371.5,-45.5 340.5,-45.5"/>
<polygon fill="none" stroke="#000000" points="8.5,-24.5 8.5,-45.5 105.5,-45.5 105.5,-24.5 8.5,-24.5"/>
<text text-anchor="start" x="29" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">Assemble</text>
<polygon fill="none" stroke="#000000" points="105.5,-24.5 105.5,-45.5 181.5,-45.5 181.5,-24.5 105.5,-24.5"/>
<text text-anchor="start" x="138" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">X</text>
<polygon fill="none" stroke="#000000" points="181.5,-24.5 181.5,-45.5 278.5,-45.5 278.5,-24.5 181.5,-24.5"/>
<text text-anchor="start" x="224.5" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">X</text>
<polygon fill="#000000" stroke="transparent" points="278.5,-24.5 278.5,-45.5 340.5,-45.5 340.5,-24.5 278.5,-24.5"/>
<polygon fill="none" stroke="#000000" points="278.5,-24.5 278.5,-45.5 340.5,-45.5 340.5,-24.5 278.5,-24.5"/>
<polygon fill="none" stroke="#000000" points="340.5,-24.5 340.5,-45.5 371.5,-45.5 371.5,-24.5 340.5,-24.5"/>
<text text-anchor="start" x="350.5" y="-31.3" font-family="Times,serif" font-size="14.00" fill="#000000">X</text>
<polygon fill="none" stroke="#000000" points="8.5,-3.5 8.5,-24.5 105.5,-24.5 105.5,-3.5 8.5,-3.5"/>
<text text-anchor="start" x="44.5" y="-10.3" font-family="Times,serif" font-size="14.00" fill="#000000">Test</text>
<polygon fill="none" stroke="#000000" points="105.5,-3.5 105.5,-24.5 181.5,-24.5 181.5,-3.5 105.5,-3.5"/>
<polygon fill="none" stroke="#000000" points="181.5,-3.5 181.5,-24.5 278.5,-24.5 278.5,-3.5 181.5,-3.5"/>
<polygon fill="none" stroke="#000000" points="278.5,-3.5 278.5,-24.5 340.5,-24.5 340.5,-3.5 278.5,-3.5"/>
<text text-anchor="start" x="304" y="-10.3" font-family="Times,serif" font-size="14.00" fill="#000000">X</text>
<polygon fill="#000000" stroke="transparent" points="340.5,-3.5 340.5,-24.5 371.5,-24.5 371.5,-3.5 340.5,-3.5"/>
<polygon fill="none" stroke="#000000" points="340.5,-3.5 340.5,-24.5 371.5,-24.5 371.5,-3.5 340.5,-3.5"/>
</g>
</g>
</svg>
</div>


### Requirements Diagram

```
# Intelligence, Surveillance, & Reconnaissance Unmanned Underwater Vehicle (ISR UUV) un-numbered requirements
requirements = [("ISR UUV", "Performance"),
                ("Performance", 
                ("The UUV shall be capable of completing a mission of 6 hours duration.", 
                "The UUV shall be capable of a top speed of 14 knots.", 
                "The UUV shall be capable of surviving in an open ocean environment to a depth of 1500 meters.", 
                "The UUV shall avoid detection.")),
                ("ISR UUV", "Communication"),
                ("Communication", 
                ("Mission parameters shall be uploadable to the UUV",
                "The UUV shall receive remote commands",
                "The UUV shall commence its mission when commanded",
                "The UUV shall be capable of transmitting data in a host ship compatible format",
                "The UUV shall indicate that it is ready for recovery")),]

# draw requirements diagram as horizontal tree left -> right
se.requirements_diagram(requirements, rankdir='LR', filename="uuv_requirements_tree")
```

<div style="text-align: center">
<object data="_images/uuv_requirements_tree.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{uuv_requirements_tree.svg}
 
```
 
### Fault Tree

```
lamp_circuit_fault_tree = [("Missing Indication", "and", ["Resistor Fails", "Capacitor Fails", "Both Lamps Out"]),
           ('Both Lamps Out', 'or', ['Lamp 1 Fails', 'Lamp 2 Fails', 'Lamp 3 Fails']),
           ('Resistor Fails', 'basic', []),
           ('Capacitor Fails', 'basic', []),
           ('Lamp 1 Fails', 'BASIC', []),
           ('Lamp 2 Fails', 'basic', []),
           ('Lamp 3 Fails', 'basic', []),
                          ]

se.fault_tree_diagram(lamp_circuit_fault_tree, filename="lamp_circuit_fault_tree")
```

<div style="text-align: center">
<object data="_images/lamp_circuit_fault_tree.png" width=500px>
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{lamp_circuit_fault_tree.svg}

```  

### Read Fault Tree from Excel

Portion of example Excel file *aav_fault_tree.xlsx*:

![aav_fault_tree_excel.png](_images/aav_fault_tree_excel.png)

```
# read fault tree from Excel file into list of nodes
fault_tree_list = se.read_fault_tree_excel('aav_fault_tree.xlsx')

# create fault tree diagram
se.fault_tree_diagram(fault_tree_list)

```

![aav_fault_tree.png](_images/aav_fault_tree.png)

### Causal Diagram

```
# causal relationships
relationships = [('Available personnel',"Workforce gap", "-"),
    ('Required personnel',"Workforce gap", "+"),
    ("Workforce gap", "Hiring rate", "+"),
    ("Hiring rate", "Available personnel", "+"),
                ]

# draw diagram
se.causal_diagram(relationships)
```

<div style="text-align: center">
<object data="_images/workforce_gap_cld.svg">
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{workforce_gap_cld.svg}

```  

### System Dynamics Model

```
# Rayleigh curve staffing model

init_model(start=0, stop=6, dt=.2)

add_stock("cumulative_effort", 0, inflows=["effort rate"])
add_flow("effort rate", "learning_function * (estimated_total_effort - cumulative_effort)")
add_auxiliary("learning_function", "manpower_buildup_parameter * time")
add_auxiliary("manpower_buildup_parameter", .5)
add_auxiliary("estimated_total_effort", 15)

run_model()
plot_output('cumulative_effort', 'effort rate', "learning_function")
```

<div style="text-align: center">
<object data="_images/rayleigh_curve_model_output.png" width=450px>
</object>
</div>

```{eval-rst}
.. raw:: latex

   \includesvg[]{rayleigh_curve_model_output.png}

```  
