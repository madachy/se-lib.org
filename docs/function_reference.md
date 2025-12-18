# Function Reference

To use se-lib, first import it before using any functions:

``` python
import selib
```

These function definitions follow the convention whereby required input parameters are shown first, then optional parameters are shown with an equal sign indicating the default values. A graph here is a generic set of nodes representing system elements connected by edges shown as non-directed or directed lines.

## Diagrams


### context_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.context_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">context_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">system</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">external_systems</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">engine</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'neato'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.context_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a context diagram.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_name</strong> (<em>string</em>) – The name of the system to label the diagram.</p></li>
<li><p><strong>external_systems</strong> (<em>list of strings</em>) – Names of the external systems that interact with the system in a list.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### critical_path_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.critical_path_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">critical_path_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">tasks</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">task_dependencies</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.critical_path_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Compute and draw the critical path between dependent tasks as the longest in duration from start to finish.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>tasks</strong> (<em>list of tuples where each contains a task name and dictionary for duration time</em>) – A list of tuples where each one contains a task name and dictionary for its duration time (where keyword = “Duration” and value is a number).</p></li>
<li><p><strong>task_dependencies</strong> (<em>list of tuples</em>) – A list of tuples describing the dependency relationships between tasks. Each relationship is a tuple containing the predecessor task followed by its successor task. These must be the same named tasks in the task list input above.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – The rendered graph for display. It will be automatically displayed in Jupyter Notebooks or IPython consoles. With other Python editors it can be displayed in the associated console by typing the returned graph name (e.g., call the function with an assignment such as <code class="docutils literal notranslate"><span class="pre">critical_path</span> <span class="pre">=</span> <span class="pre">critical_path_diagram(...)</span></code> and then type <code class="docutils literal notranslate"><span class="pre">critical_path</span></code> in the console). If a filename is optionally provided, the rendered graph will also be saved as a file in the specified format. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### design_structure_matrix
<dl class="py function">
<dt class="sig sig-object py" id="selib.design_structure_matrix">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">design_structure_matrix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">elements</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">element_dependencies</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.design_structure_matrix" title="Permalink to this definition">¶</a></dt>
<dd><p>Draw a design structure matrix of system elements and their dependencies. Matrix elements may represent tasks (process activities), system parameters or attributes.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>elements</strong> (<em>list of strings</em>) – Names of the matrix elements as the row and column headings in a list.</p></li>
<li><p><strong>element_dependencies</strong> (<em>list of tuples</em>) – A list of tuples describing the relationships between elements. Each relationship is a tuple containing the relationship input element, output element and optionally a custom label (or other object) to mark the relationship in the form (“input element”, “output element”, “relationship label”). The default marking denoting a relationship is an uppercase ‘X’, therefore, the shortened tuple relationship (“input element”, “output element”) is equivalent to (“input element”, “output element”, “X”). A custom label can be specified as html code for styling of the font type, font color, cell color, etc. Images and unicode characters can be inserted this way, or other html markup for lists, tables, etc.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – The rendered graph for display. It will be automatically displayed in Jupyter Notebooks or IPython consoles. With other Python editors it can be displayed in the associated console by typing the returned graph name (e.g., call the function with an assignment such as <code class="docutils literal notranslate"><span class="pre">dsm</span> <span class="pre">=</span> <span class="pre">design_structure_matrix(...)</span></code> and then type <code class="docutils literal notranslate"><span class="pre">dsm</span></code> in the console). If a filename is optionally provided, the rendered graph will also be saved as a file in the specified format. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### fault_tree_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.fault_tree_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">fault_tree_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">ft</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.fault_tree_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a fault tree diagram.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ft</strong> (<em>list of tuples</em>) – <p>A list of the faults as a tree hierarchy. Each fault is defined in a tuple containing the fault name, type, and underlying faults (if any) in the form
<code class="docutils literal notranslate"><span class="pre">(&quot;fault</span> <span class="pre">name&quot;,</span> <span class="pre">&quot;fault</span> <span class="pre">name&quot;,</span> <span class="pre">list</span> <span class="pre">of</span> <span class="pre">fault</span> <span class="pre">branches)</span></code>
with the branches as a list in the form
<code class="docutils literal notranslate"><span class="pre">[&quot;branch</span> <span class="pre">1</span> <span class="pre">name&quot;,</span> <span class="pre">&quot;branch</span> <span class="pre">2</span> <span class="pre">name&quot;,</span> <span class="pre">...</span> <span class="pre">&quot;branch</span> <span class="pre">n</span> <span class="pre">name&quot;]</span></code>
to identify the adjoining faults. All basic events will have a blank list
<code class="docutils literal notranslate"><span class="pre">[]</span></code> since they are the bottom leaves in the tree.</p>
<p>The top event must be in the first row, but all other events can be in any order. They may begrouped by their event paths or by hierarchical levels as convenient. Event types can be conditional “and”s, conditional “or”s, or basic events (leaves). The following spellings are recognized as valid designations for event types:</p>
<p>And: “And” “and” “AND”</p>
<p>Or: “Or” “or” “OR”</p>
<p>Basic: “Basic” “basic” “BASIC”</p>
</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### sequence_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.sequence_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">sequence_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">system_name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">actors</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">objects</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">actions</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.sequence_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a sequence diagram.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_name</strong> (<em>string</em>) – The name of the system to label the diagram.</p></li>
<li><p><strong>actors</strong> (<em>list of strings</em>) – Names of the outside actors that participate in the activity sequence in a list.</p></li>
<li><p><strong>objects</strong> (<em>list of strings</em>) – Names of the system objects that participate in the activity sequence in a list.</p></li>
<li><p><strong>actions</strong> (<em>list of tuples</em>) – A chronologically ordered list describing the sequence of actions to be drawn. Each action is a tuple containing the action source, target and action name (or data/control passed) in the form (“source”, “target”, “action name”) indicating a labeled horizontal arrow drawn between them.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>

<span id="id1"></span>### use_case_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.use_case_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">use_case_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">system_name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">actors</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">use_cases</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">interactions</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">use_case_relationships</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.use_case_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Draw a use case diagram.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>system_name</strong> (<em>string</em>) – The name of the system to label the diagram.</p></li>
<li><p><strong>actors</strong> (<em>list of strings</em>) – Names of the outside actors that interact with the system in the use cases in a list.</p></li>
<li><p><strong>use_cases</strong> (<em>list of strings</em>) – Names of the use cases in a list.</p></li>
<li><p><strong>interactions</strong> (<em>list of tuples</em>) – A list of the interactions to be drawn between actors and use cases. Each interaction is a tuple containing an actor and use case in the form (“actor name”, “use case name”) indicating an arrow drawn from the actor to the use case. Interactions are graph edges.</p></li>
<li><p><strong>use_case_relationships</strong> (<em>list of tuples</em><em>, </em><em>optional</em>) – A list of the relationships, or associations to be drawn between use cases. Each relationship is a tuple containing a use case pair and type relationship in the form (“use case 1”, “use case 2”, “relationship”) indicating an arrow drawn from the first to the second use case. Relationship types are “&lt;&lt;include&gt;&gt;”, “&lt;&lt;extend&gt;&gt;” and “generalization”.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### wbs_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.wbs_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">wbs_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">decompositions</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">rankdir</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'TB'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.wbs_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Draw a work breakdown structure as a tree hierarchy. Decompositions describe the parent-child relationships.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>decompositions</strong> (<em>list of tuples</em>) – A list of tuples describing the work decomposition relationships. Each relationship is a tuple containing the parent element followed by the child element.</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
<li><p><strong>rankdir</strong> (<em>string</em><em>, </em><em>optional</em>) – The direction to display the tree from the parent node. The default <code class="docutils literal notranslate"><span class="pre">rankdir='TB'</span></code> denotes top to bottom for a vertical tree decomposition. It can diagrammed horizontally by providing rankdir=’LR’ to designate left to right.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – The rendered graph for display. It will be automatically displayed in Jupyter Notebooks or IPython consoles. With other Python editors it can be displayed in the associated console by typing the returned graph name (e.g., call the function with an assignment such as <code class="docutils literal notranslate"><span class="pre">wbs</span> <span class="pre">=</span> <span class="pre">wbs_diagram(...)</span></code> and then type <code class="docutils literal notranslate"><span class="pre">wbs</span></code> in the console). If a filename is optionally provided, the rendered graph will also be saved as a file in the specified format. PyML calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


## Analyses


### fault_tree_cutsets
<dl class="py function">
<dt class="sig sig-object py" id="selib.fault_tree_cutsets">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">fault_tree_cutsets</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">fault_tree</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.fault_tree_cutsets" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns a fault tree cutset.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ft</strong> (<em>list of tuples</em>) – <p>A list of the faults as a tree hierarchy. Each fault is defined in a tuple containing the fault name, type, and underlying faults (if any) in the form
<code class="docutils literal notranslate"><span class="pre">(&quot;fault</span> <span class="pre">name&quot;,</span> <span class="pre">&quot;fault</span> <span class="pre">name&quot;,</span> <span class="pre">list</span> <span class="pre">of</span> <span class="pre">fault</span> <span class="pre">branches)</span></code>
with the branches as a list in the form
<code class="docutils literal notranslate"><span class="pre">[&quot;branch</span> <span class="pre">1</span> <span class="pre">name&quot;,</span> <span class="pre">&quot;branch</span> <span class="pre">2</span> <span class="pre">name&quot;,</span> <span class="pre">...</span> <span class="pre">&quot;branch</span> <span class="pre">n</span> <span class="pre">name&quot;]</span></code>
to identify the adjoining faults. All basic events will have a blank list
<code class="docutils literal notranslate"><span class="pre">[]</span></code> since they are the bottom leaves in the tree.</p>
<p>The top event must be in the first row, but all other events can be in any order. They may begrouped by their event paths or by hierarchical levels as convenient. Event types can be conditional “and”s, conditional “or”s, or basic events (leaves). The following spellings are recognized as valid designations for event types:</p>
<p>And: “And” “and” “AND”</p>
<p>Or: “Or” “or” “OR”</p>
<p>Basic: “Basic” “basic” “BASIC”</p>
</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>cutsets</strong> – Returns a list of cutsets, where each is defined as a list of events.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>list of lists</p>
</dd>
</dl>
</dd></dl>


## Simulations

### System Dynamics



#### init_sd_model
<dl class="py function">
<dt class="sig sig-object py" id="selib.init_sd_model">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">init_sd_model</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">start</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stop</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">dt</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.init_sd_model" title="Permalink to this definition">¶</a></dt>
<dd><p>Instantiates a system dynamics model for simulation</p>
</dd></dl>


#### add_stock
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_stock">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_stock</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">initial</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">inflows</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">outflows</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_stock" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds a stock to the model</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the stock</p></li>
<li><p><strong>initial</strong> (<em>float</em>) – Initial value of stock at start of simulation</p></li>
<li><p><strong>inflows</strong> (<em>list of float</em>) – The names of the inflows to the stock</p></li>
<li><p><strong>outflows</strong> (<em>list of float</em>) – The names of the outflows to the stock</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### add_flow
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_flow">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_flow</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">equation</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">inputs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_flow" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds a flow to the model</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the flow</p></li>
<li><p><strong>equation</strong> (<em>str</em>) – Equation for the flow using other named model variables</p></li>
<li><p><strong>inputs</strong> (<em>list</em>) – Optional list of variable input names used to draw model diagram</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### add_auxiliary
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_auxiliary">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_auxiliary</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">equation</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">inputs</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">[]</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_auxiliary" title="Permalink to this definition">¶</a></dt>
<dd><p>Adds auxiliary equation or constant to the model</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the auxiliary</p></li>
<li><p><strong>equation</strong> (<em>str</em>) – Equation for the auxiliary using other named model variables</p></li>
<li><p><strong>inputs</strong> (<em>list</em>) – Optional list of variable input names used to draw model diagram</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### plot_graph
<dl class="py function">
<dt class="sig sig-object py" id="selib.plot_graph">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">plot_graph</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span><span class="n"><span class="pre">outputs</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.plot_graph" title="Permalink to this definition">¶</a></dt>
<dd><p>displays matplotlib graph for each model variable</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>variables</strong> (<em>str</em><em> or </em><em>list</em>) – comma separated variable name(s) or lists of variable names to plot on single graphs</p>
</dd>
<dt class="field-even">Return type<span class="colon">:</span></dt>
<dd class="field-even"><p>matplotlib graph</p>
</dd>
</dl>
</dd></dl>


#### save_graph
<dl class="py function">
<dt class="sig sig-object py" id="selib.save_graph">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">save_graph</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span><span class="n"><span class="pre">outputs</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'graph.png'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.save_graph" title="Permalink to this definition">¶</a></dt>
<dd><p>save graph to file</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>variables</strong> (<em>variable name</em><em> or </em><em>list of variable names to plot on graph</em>) – </p></li>
<li><p><strong>filename</strong> (<em>file name with format extension</em>) – </p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### run_model
<dl class="py function">
<dt class="sig sig-object py" id="selib.run_model">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">run_model</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.run_model" title="Permalink to this definition">¶</a></dt>
<dd><p>Executes the current model</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p><ul class="simple">
<li><p><em>If continuous, returns 1) Pandas dataframe containing run outputs for each variable each timestep and 2) model dictionary.</em></p></li>
<li><p><em>If discrete, returns 1) network dictionary with run statistics and 2) entity run data</em></p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>


#### set_logical_run_time
<dl class="py function">
<dt class="sig sig-object py" id="selib.set_logical_run_time">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">set_logical_run_time</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">condition</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.set_logical_run_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables a run time to be measured based on a logical condition for when the simulation should be run (like a while statement).  The logical end time will be available from the ‘get_logical_end_time()’ function in lieu of the fixed end time for a simulation.</p>
</dd></dl>


#### get_logical_end_time
<dl class="py function">
<dt class="sig sig-object py" id="selib.get_logical_end_time">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">get_logical_end_time</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#selib.get_logical_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns the logical end time as specified in a previous ‘set_logical_run_time()’ function call, in lieu of the fixed end time for a simulation.</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>logical_end_time</strong> – end time when the ‘set_logical_run_time()’’ condition expires</p>
</dd>
<dt class="field-even">Return type<span class="colon">:</span></dt>
<dd class="field-even"><p>float</p>
</dd>
</dl>
</dd></dl>


#### draw_model_diagram
<dl class="py function">
<dt class="sig sig-object py" id="selib.draw_model_diagram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">draw_model_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.draw_model_diagram" title="Permalink to this definition">¶</a></dt>
<dd><p>Draw a diagram of the current model.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. se-lib calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


### Discrete Event

#### init_de_model
<dl class="py function">
<dt class="sig sig-object py" id="selib.init_de_model">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">init_de_model</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#selib.init_de_model" title="Permalink to this definition">¶</a></dt>
<dd><p>Instantiates a discrete event model for simulation</p>
</dd></dl>


#### add_source
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_source">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_source</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">entity_name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">num_entities</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">connections</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">interarrival_time</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_source" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a source node to a discrete event model to generate entities.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>string</em>) – A name for the source.</p></li>
<li><p><strong>entity_name</strong> (<em>string</em>) – A name for the type of entity being generated.</p></li>
<li><p><strong>num_entities</strong> (<em>integer</em>) – Number of entities to generated.</p></li>
<li><p><strong>connections</strong> (<em>dictionary</em>) – A dictionary of the node connections after the source.  The node names are the keys and the values are the relative probabilities of traversing the connections.</p></li>
<li><p><strong>interarrival_time</strong> (<em>string</em>) – The time between entity arrrivals into the system.  The string may enclose a constant, random function or logical expression to be evaluated.</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### add_server
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_server">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_server</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">connections</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">service_time</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">capacity</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">1</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_server" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a server to a discrete event model.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>string</em>) – A name for the server.</p></li>
<li><p><strong>connections</strong> (<em>dictionary</em>) – A dictionary of the node connections after the server.  The node names are the keys and the values are the relative probabilities of traversing the connection.</p></li>
<li><p><strong>capacity</strong> (<em>integer</em>) – The number of resource usage slots in the server</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### add_delay
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_delay">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_delay</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">connections</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">delay_time</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a delay to a discrete event model.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>string</em>) – A name for the delay.</p></li>
<li><p><strong>connections</strong> (<em>dictionary</em>) – A dictionary of the node connections after the delay.  The node names are the keys and the values are the relative probabilities of traversing the connections.</p></li>
<li><p><strong>delay_time</strong> (<em>float</em>) – The time delay for entities to traverse.  May be a constant or random function.</p></li>
</ul>
</dd>
</dl>
</dd></dl>


#### add_terminate
<dl class="py function">
<dt class="sig sig-object py" id="selib.add_terminate">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">add_terminate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">name</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.add_terminate" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a terminate node to a discrete event model for entities leaving the system.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><p><strong>name</strong> (<em>string</em>) – A name for the terminate.</p>
</dd>
</dl>
</dd></dl>


#### run_model
<dl class="py function">
<dt class="sig sig-object py" id="id0">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">run_model</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">verbose</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">True</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#id0" title="Permalink to this definition">¶</a></dt>
<dd><p>Executes the current model</p>
<dl class="field-list simple">
<dt class="field-odd">Returns<span class="colon">:</span></dt>
<dd class="field-odd"><p><ul class="simple">
<li><p><em>If continuous, returns 1) Pandas dataframe containing run outputs for each variable each timestep and 2) model dictionary.</em></p></li>
<li><p><em>If discrete, returns 1) network dictionary with run statistics and 2) entity run data</em></p></li>
</ul>
</p>
</dd>
</dl>
</dd></dl>


#### draw_model_diagram
<dl class="py function">
<dt class="sig sig-object py" id="id4">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">draw_model_diagram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">format</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'svg'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#id4" title="Permalink to this definition">¶</a></dt>
<dd><p>Draw a diagram of the current model.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A filename for the output not including a filename extension. The extension will specified by the format parameter.</p></li>
<li><p><strong>format</strong> (<em>string</em><em>, </em><em>optional</em>) – The file format of the graphic output. Note that bitmap formats (png, bmp, or jpeg) will not be as sharp as the default svg vector format and most particularly when magnified.</p></li>
</ul>
</dd>
<dt class="field-even">Returns<span class="colon">:</span></dt>
<dd class="field-even"><p><strong>g</strong> – Save the graph source code to file, and open the rendered result in its default viewing application. se-lib calls the Graphviz API for this.</p>
</dd>
<dt class="field-odd">Return type<span class="colon">:</span></dt>
<dd class="field-odd"><p>graph object view</p>
</dd>
</dl>
</dd></dl>


#### plot_histogram
<dl class="py function">
<dt class="sig sig-object py" id="selib.plot_histogram">
<span class="sig-prename descclassname"><span class="pre">selib.</span></span><span class="sig-name descname"><span class="pre">plot_histogram</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">data</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">filename</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">xlabel</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'Data'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#selib.plot_histogram" title="Permalink to this definition">¶</a></dt>
<dd><p>Plot a histogram for a dataset and optionally save to a file.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters<span class="colon">:</span></dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>data</strong> (<em>list</em>) – A list of the data values</p></li>
<li><p><strong>filename</strong> (<em>string</em><em>, </em><em>optional</em>) – A name for the file</p></li>
<li><p><strong>xlabel</strong> (<em>string</em><em> , </em><em>optional</em>) – A label for the x-axis</p></li>
</ul>
</dd>
<dt class="field-even">Return type<span class="colon">:</span></dt>
<dd class="field-even"><p>A Matplotlib histogram</p>
</dd>
</dl>
</dd></dl>
