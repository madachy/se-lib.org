# Home

## Introduction

Welcome to the **Systems Engineering Library (se-lib)** (previously called PyML). It provides capabilities for integrated systems modeling, simulation, analysis and diagrams covering SysML, discrete event and continuous system dynamics simulation, reliability analysis, causal analysis, project management, and more using simple Python code as the glue.

The open source Python scientific computing ecosystem enables advanced analysis with powerful libraries and language features. se-lib is built with Graphviz, Matplotlib, NetworkX, NumPy, PySD, SciPy, and SimPy.

[![GitHub](https://img.shields.io/badge/GitHub-se--lib-181717?logo=github)](https://github.com/se-lib/se-lib)
[![PyPI version](https://img.shields.io/pypi/v/se-lib)](https://pypi.org/project/se-lib/)
[![Python versions](https://img.shields.io/pypi/pyversions/se-lib)](https://pypi.org/project/se-lib/)
[![MIT license](https://img.shields.io/badge/license-MIT-green)](https://github.com/se-lib/se-lib/blob/main/LICENSE)

## Quick Start

Try se-lib instantly with these Colab notebooks in a browser, no installation required.

* [se-lib examples](https://colab.research.google.com/drive/1J0Dnb2qmoMiuJWJTAsMQ5c3F6vjn4CzQ?usp=sharing) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1J0Dnb2qmoMiuJWJTAsMQ5c3F6vjn4CzQ?usp=sharing)
* [System dynamics modeling user's guide and examples](https://colab.research.google.com/drive/1oE5TBdF-hpJTQbQgSmPgmPoofBgOTR0B?usp=sharing)
* [Discrete event modeling user's guide and examples](https://colab.research.google.com/drive/1arDDaaltEyGLomaGo5ZKVumtviloUAyG?usp=sharing)

se-lib also runs on standalone web pages for rapid experimentation and instruction.

* [SysML Diagram Scratchpad](online/scratchpad.md)
* [Discrete Event Modeling Demonstrations](online/discrete_event_modeling_demo.md)
* [se-lib playground](online/sysml.md)

## Installation

```bash
pip install se-lib
```

For more detailed installation instructions, see the [Installation](installation.md) page.

## Current Features

The current features of se-lib can be found under [Function Reference](function_reference.md).

Key capabilities include:

- **SysML Diagrams:** Context diagrams, use case diagrams, activity diagrams, requirements diagrams, block diagrams, and more
- **Discrete Event Simulation:** Model and simulate discrete event systems with queues, servers, and resources
- **System Dynamics:** Continuous simulation and causal loop diagrams
- **Reliability Analysis:** Fault tree analysis and reliability block diagrams
- **Project Management:** PERT charts, Gantt charts, critical path analysis, and design structure matrices
- **Network Analysis:** Using NetworkX for complex system relationships

## Example Usage

```python
import selib

# Create a simple SysML context diagram
selib.context_diagram(
    system="Autonomous Vehicle",
    external_systems=[
        "Driver",
        "Pedestrian", 
        "Traffic Control System",
        "Weather Service",
        "GPS Satellites"
    ],
    filename="context_diagram"
)

# Define and run a discrete event simulation
selib.init_de_model()

selib.add_source(
    name='arrivals',
    connections={'server': 1},
    num_entities=100,
    interarrival_time='random.expovariate(1/5)'
)

selib.add_server(
    name='server',
    connections={'exit': 1},
    service_time='random.expovariate(1/4)',
    capacity=1
)

selib.add_terminate(name='exit')

network, entity_data = selib.run_model()
selib.draw_model_diagram(filename='de_model')
```

## Presentations

The following was presented at the 2022 INCOSE San Diego Mini-Conference:

* [Introduction to PyML](http://pyml.fun/presentations/2022%20INCOSE%20San%20Diego%20Mini-Conference%20-%20Introduction%20to%20PyML.pdf)

## Acknowledgments

se-lib research and development is supported by these sponsors:

* [<img src="/docs/assets/CSSE-logo-300x210.png" width="30px" alt="csse_logo">](https://boehmcsse.org/) Boehm Center for Systems and Software Engineering
* Naval Postgraduate School Foundation
* Naval Postgraduate School Foundation
* Marine Corps Air Station (MCAS) Miramar

## Feedback

We value your feedback. Tell us how we can make se-lib, its documentation and this website more useful. Please send comments, suggestions and interest in supporting the development to [info@se-lib.org](mailto:info@se-lib.org).

---

© Copyright 2025, se-lib Development Team. Last updated on Dec 12, 2025.
