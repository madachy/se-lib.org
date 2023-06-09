---
myst:
  html_meta:
    "description": "Systems Engineering Library (se-lib) Tutorial"
    "keywords": "se-lib, systems engineering, system modeling, python modeling library, se-lib, system modeling, SysML, UML, python, systems modeling language, unified modeling language, systems engineering, requirements diagram, use case diagram, sequence diagram, context diagram, work breakdown structure, WBS, wbs diagram, critical path, critical path diagram, fault tree analysis, fault tree diagram, fault tree cutsets, system dynamics, simulation"
---
# Tutorials

<span style="font-size: 32px;">San Diego INCOSE Tutorial: Open Source Systems Modeling</span>

[Zoom Link](<https://nps-edu.zoomgov.com/j/1614484384> "Zoom Link") Passcode: CvaFqM0s$M

The tutorial will cover new open-source system modeling capabilities, and
immediately enable participants to implement them requiring only an
Internet connection. The Systems Engineering Library (*se-lib*) using Python is described at [http://se-lib.org](<http://se-lib.org> "http://se-lib.org") and can be used online or installed for offline usage.

*se-lib* lowers barriers to system modeling with an open-source tool environment
harnessing the extensive Python scientific computing ecosystem. It provides
integrated capabilities for system modeling, analysis, and automatic documentation
with SysML, other SE model types and analysis methods. The environment enables
natural integration of models, inline or external data with only a few lines of code.

Numerous examples, templates, and modeling case studies will be provided.
Students only need basic computer skills to modify the examples or create new
models. Previous knowledge of Python isn’t necessary. Examples are self-evident
since Python is highly readable and concise, so exercises will be based around
simple short code.

With *se-lib* participants will learn how to incorporate open source modeling in system engineering processes
and toolsets. They will understand how open source tools can support rapid iterative processes and
automate round-trip digital engineering when reconciling single-source truth
models.

Participants will require a laptop or other device (tablet or phone would work) and an
Internet connection (unless they install the library prior and prefer to work
offline). They will rapidly model, analyze, and automatically document systems with naturally integrated models.

## Prerequisites
1. General knowledge of system modeling methods as exemplified by SysML, other
model types, systems engineering analysis and simulation.
2. Exposure to computer programming from traditional engineering degree or on the job is helpful.

## Agenda

1. 0900 - 0915 (Madachy): Welcome and Introductions

1. 0915 - 0935 (Madachy): [Overview of *se-lib*](<http://se-lib.org/tutorials/SD INCOSE Tutorial - Open Source System Modeling.pdf> "Open Source System Modeling")
	* Usage and architecture
	* Brief introduction to Python syntax
	* Website resources

1. 0935 - 1000 (Longshore): Hands-on introduction
	* [se-lib playground](<http://se-lib.org/online/sysml.html> "SysML modeling and diagrams")
	* library installation
	* [Google Colaboratory](<https://colab.research.google.com/drive/1J0Dnb2qmoMiuJWJTAsMQ5c3F6vjn4CzQ?usp=sharing> "se-lib examples"). Open in Colab to run or save your own copy in Drive"
	* Replit
	* Anaconda


    **1000 - 1010: Break**


1. 1010 - 1130: Model library demonstrations and exercises
	* (Longshore) [SysML modeling and diagrams](<http://se-lib.org/online/sysml.html> "SysML modeling and diagrams")
	* (Madachy) Simulation
      * [System Dynamics Modeling with se-lib User's Guide v. 1.0](<http://se-lib.org/manuals/System_Dynamics_Modeling_with_se_lib_User_s_Guide _1_.pdf>)
      * [System dynamics simulation](<https://colab.research.google.com/drive/1oE5TBdF-hpJTQbQgSmPgmPoofBgOTR0B?usp=sharing>) on Google Colab
      * [Discrete event modeling and simulation](<http://se-lib.org/online/discrete_event_modeling_demo.html> "Discrete event modeling and simulation demonstrations") on se-lib playground
	* (Longshore) Fault tree analysis, diagrams, and system reliability modeling
	* (Longshore) Project management modeling
	* (Madachy) Automatic document re-generation with reconciled changes across model sets
	* (Madachy/Longshore) Model data import/export and sharing with other tools.
		* [Excel](<http://se-lib.org/examples.html#read-fault-tree-from-excel>)
		* xmile, vensim


1. 1130 - 1200 (Madachy/Longshore): Further examples, guided exercises, and extended case studies on above areas
for integrated system modeling.
	* Students will be given options for exercises based on their interests and the
opportunity to focus on their own system models.
	* If students do not have a particular problem to focus on, here are some samples:
      * [course portal problem](<http://se-lib.org/tutorials/course_portal.html> "Course Portal Problem")
      * [simulation exercises](<http://se-lib.org/tutorials/simulation_exercises.html> "Course Portal Problem")


    **1200 - 1300: Lunch**


1. 1300 - 1330: Advanced usage with Python scientific computing ecosystem and open source
communities
	* (Madachy) Introduce libraries that are building blocks of se-lib, how they interface with and
depend on each other, how to navigate and leverage their capabilities for system
modeling applications.
		* (Madachy) Matplotlib
		* (Longshore) Pandas
		* (Longshore) SciPy


1. 1330 - 1345 (Madachy / Longshore): Digital engineering and rapid change: automated model configuration management, re-execution, impact analysis and version control for round-trip digital engineering.
	* Demonstrate how all model artifacts in text files are managed with standard automated tools (e.g. GitHub for small to large teams).
		* Collaborative Modeling of Target Shooter System

1. 1345 - 1430: Future capabilities and evolution plans (Workshop Format)
	* Audience will provide input on desired features and changes
	* Written summary and wrapup

## Presenters

**Ray Madachy**

<div style="float: right; margin: 10px">
<object data="../_images/Ray_Madachy.png" width=200px>
</object>
</div>

Raymond Madachy, Ph.D., is a Professor in the Systems Engineering Department at
the Naval Postgraduate School. His research interests include system and software
cost modeling; affordability and tradespace analysis; modeling and simulation of
systems and software engineering processes; integrating systems engineering and
software engineering disciplines; and systems engineering tool environments. His research has been funded by diverse agencies across the DoD, National Security Agency, NASA, and several companies.  

He has developed widely used tools for systems and software cost estimation, and is leading development of the open-source Systems Engineering Library (se-lib).  He received the USC Center for Systems and Software Engineering Lifetime Achievement Award for “Innovative Development of a Wide Variety of Cost, Schedule and Quality Models and Simulations” in 2016.

His books include Software Process Dynamics, What Every Engineer Should Know
about Modeling and Simulation; co-author of Software Cost Estimation with
COCOMO II, and Software Cost Estimation Metrics Manual for Defense Systems. He
is writing Systems Engineering Principles for Software Engineers and What Every
Engineer Should Know about Python.

**Ryan Longshore**

<div style="float: right; margin: 10px">
<object data="../_images/LongshoreRyan_Pic900px.jpg" width=200px>
</object>
</div>

Ryan Longshore is an 18 year veteran of both the defense and electric utility industries. In his current role at Naval Information Warfare Center Atlantic (NIWC LANT), Ryan leads a diverse team of engineers and scientists developing and integrating new technologies into command and operations centers. Ryan is heavily involved in the Navy's digital engineering transformation and leads multiple efforts in the model based systems engineering and model based engineering realms.

Ryan earned a BS in Electrical Engineering from Clemson University, a MS in Systems Engineering from Southern Methodist University, and is currently pursuing his PhD in Systems Engineering from the Naval Postrgraduate School. He is a South Carolina registered Professional Engineer (PE), an INCOSE Certified Systems Engineering Professional (CSEP), and has achieved the OMG SysML Model Builder Fundamental Certification.

## Participants

Greg Bulla

Vanessa Cannon

Frank Camp

Alexandro Castaneda

Brian Flick

Cheryl Gray

Juan Hernandez Guizar

Arianna Lasche

Ariel Lu

Marilyn Luteman

Curran Meek

Gregg Morissette

Ted Mulder

Kenneth Sakaguchi

James Sanford-Luevano

Dr. Julia Taylor

John Thomas

Ted Valencia

Earl Zedd
