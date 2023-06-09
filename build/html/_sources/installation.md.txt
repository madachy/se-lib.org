---
myst:
  html_meta:
    "description": "Systems Engineering Library (se-lib) Installation"
    "keywords": "Systems Engineering Library (se-lib), python modeling library, PyML, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation"
---

# Installation

se-lib is available on [PyPI](https://pypi.org/project/se-lib/) and can be installed with ``pip install se-lib`` from a terminal, other command shell or Anaconda command shell. The current version is 0.26.6.  For more help see [Detailed Anaconda Installation](<Detailed Anaconda Installation>) instructions.


Alternatively, download the library file from [PyPI](https://pypi.org/project/se-lib/) and copy it to your local development folder or elsewhere on your Python path. If you use the recommended [Anaconda](https://www.anaconda.com/products/individual) Python distribution it will come with all of the required packages below except for Graphviz and Pdflatex. These are required:

* Python version 3.8 and higher.
* [Graphviz](https://graphviz.org/) is required to generate diagrams. After installing Anaconda, use its Powershell Command Prompt and type ``conda install -c conda-forge python-graphviz``. With other Python environments it can be installed with ``pip install graphviz``. Also see graphviz download or graphviz on PyPI for additional instructions for different platforms.
* The *numpy* package is used for model analysis and plotting features.
* The *matplotlib* package is required to use the graphical functionality of se-lib.
* *Pdflatex* is required to compile latex files and generate pdfs. It can be installed for Python or comes with standard latex distributions.

Note that diagrams can still be produced without *graphviz* installed locally by providing the generated dot markup text to online tools. Without *pdflatex*, the latex markup can be copied to other publishing tools such as *Overleaf* for refinement and/or pdf generation.

## Updating
To update from a previous version use ``pip update se-lib``, but to ensure the latest is actually installed use ``pip install se-lib==0.26.6`` which may be necessary.

The current version can be found via the ``__doc__`` method:

```{code-block}
from selib import *
print(selib.__doc__)

se-lib Version .26.6

```


## On Replit.com 

Repls are available that are pre-installed with the latest se-lib baseline, other dependent packages and executables. These can be forked into a user account to develop new scripts.  Any of these will work for this purpose:

* [Discrete Event Simulation](https://replit.com/@se3250/Discrete-Event-Modeling-Demonstrations-with-se-lib)
* [System Dynamics Simulation](https://replit.com/@se3250/system-dynamics-simulation-examples-with-se-lib)

Another method is to custom install the packages and create the environment.  In a new repl, under Tools select Packages and search for "se-lib".  Install the latest version shown as below.  


![replit_package_install.png](_images/replit_package_install.png)


Depending on which functions you want to use, you may also need to install graphviz, pysd, pandas, netCDF4 and simpy similarly.  

### Diagrams

In a custom installation, creation of diagrams will also require adding the 2 lines `pkgs.graphviz` and `pkgs.xdg-utils` to the hidden file "replit.nix" per below.  It can be accessed by selecting "Show Hidden Files" in the Files menu.

```{code-block}
:emphasize-lines: 6, 7
{ pkgs }: {
  deps = [
    pkgs.python310Full
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
    pkgs.graphviz
    pkgs.xdg-utils
  ];
```

### Updating

Updating on replit.com also uses the package installer to remove the current and re-install to the latest. To determine the current version use the same method ``__doc__`` method as above, or look in the Packager file *pyproject.toml* for the highlighted line for se-lib.  This will be the correct version vs. what the package remover may show on the next step.

```{code-block}
:emphasize-lines: 15
[tool.poetry]
name = "python-template"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10.0,<3.11"
numpy = "^1.22.2"
replit = "^3.2.4"
Flask = "^2.2.0"
urllib3 = "^1.26.12"
graphviz = "^0.20.1"
simpy = "^4.0.1"
se-lib = "0.26.4"
matplotlib = "^3.7.1"
```

To update the library for an existing repl first remove it as below after searching for "se-lib" in the package installer.  It will appear as below and may inaccurately show the current version.  The pyproject.toml is correct.  Choose to remove and it will take a few minutes.

![replit_package_remove.png](_images/replit_package_remove.png)

Then install the latest version using the same method for initial installation above.

## Detailed Anaconda Installation

[Anaconda](https://www.anaconda.com) is a widely used development environment for the Python and R programming languages. [Anaconda](https://www.anaconda.com) is available for Windows, Mac, and Linux. To get started:

* Download [Anaconda](https://www.anaconda.com)  for your operating system
* Install Anaconda according to your specific OS directions
* Open Anaconda

**Create a Custom Environment**
> The next few steps are optional. The use of a custom environment is not required. However, you may find it useful to not be working in your base (root) environment. If you are going to be regularly downloading new packages and creating back-ups you can revert to, a custom environment is highly recommended.

* Select environments
* Click create

![anaconda](_images/anacondaenv.png)

* Environment Settings
  - Name your environment
  - Select Python
  - Click create

![settings](_images/envcreate.png)

> Depending on your computer, this may take anywhere from 10 seconds to a couple minutes.

### Install selib 

On the homescreen for your environment, install the Jupyter Notebook and Powershell Prompt apps. Other apps may be installed, but are not required for this tutorial.

![navigator](_images/navigator.png)

To install se-lib:
* Launch Powershell Prompt
* Run the following command: `pip install se-lib`

To verify successfull installation:
* Open a Jupyter Notebook
* import selib and create a context diagram

```{code-block]
import selib as se

# system model
system_name = "Python Integrator with selib"
external_actors = ["User", "OS", "Graphviz"]
# create context diagram
se.context_diagram(system_name, external_actors, filename="selib_contest_diagram_offline")
```

If everything worked correctly, you should see something like the figure below:

![context_diagram](_images/context_diagram.png)

> You can ignore the warnings. You may or may not get them when running the program.

Another good test to run is a systems dynamics model. Note that we use `from selib import *` in this example. if we did not do this, we would have to put `se.` in front of each function below.
```{code-block}
from selib import *

init_sd_model(start=0, stop=10, dt=.1)
add_stock("level", 50, inflows=["rate"])
add_auxiliary("time_constant", .5)
add_auxiliary("goal", 100)
add_flow("rate", "(goal - level) / time_constant")
run_model()

plot_graph('level')
```

If everything worked correctly, you should see something similar to the figure below.

![system dynamics example](_images/sdexample.png)

