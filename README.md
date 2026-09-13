<div align="center">

<h1>Autonomous Customer Resolution Agent</h1>
<h3><b>Tech Zephyr 4.0 | IIT Bhubaneswar — Agentic AI Hackathon</b></h3>

<p>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://github.com/"><img src="https://img.shields.io/badge/Architecture-ReAct%20Agent-00599C?style=for-the-badge" alt="ReAct Agent"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License MIT"></a>
</p>

<p align="center">
  <b>An autonomous goal-driven agent built to resolve enterprise support cases, execute database state mutations, detect failure conditions, and dynamically adapt strategies in real time.</b>
</p>

<hr>

</div>

<h2>Problem & Solution Brief</h2>

<h3>Problem Statement</h3>
<p>Most enterprise customer service applications stop at ticket classification or generating automated text responses. When a customer issue requires mutating database states—such as processing a return, validating inventory across warehouses, or issuing refunds—traditional systems require manual human intervention.</p>

<h3>Target Users</h3>
<p>E-commerce platforms, customer support operations teams, and online retail vendors looking to automate high-volume support workflows safely.</p>

<h3>Why an Agentic Solution is Necessary</h3>
<p>Standard LLMs and basic RAG pipelines are static: they generate text based on input data, but they cannot execute multi-step database operations, evaluate dynamic system state, or adapt when an intended action fails.</p>

<p>An agentic architecture is required because customer resolution involves a dynamic decision loop:</p>
<ol>
  <li>Fetching live customer and order context.</li>
  <li>Checking policy constraints.</li>
  <li>Attempting state-changing actions (e.g., replacement).</li>
  <li><b>Detecting failures</b> (e.g., out-of-stock items) and <b>dynamically replanning</b> (e.g., falling back to a full refund).</li>
  <li>Verifying the final state in the database before closing the case.</li>
</ol>

<h3>Proposed Solution & Expected Impact</h3>
<p>We built an autonomous customer resolution agent that interfaces directly with simulated enterprise APIs (Customer DB, Inventory API, Refund API) and business policy rules. It independently executes resolution steps, catches operational failures (such as inventory shortages), adapts its strategy on the fly without human intervention, and verifies backend state changes upon completion.</p>

<hr>

<h2>System Architecture & Workflow</h2>

<pre>
                        +----------------------------+
                        |     User / Support Ticket  |
                        +--------------+-------------+
                                       |
                                       v
                        +----------------------------+
                        |      Agent Controller      |
                        | (Observe -> Plan -> Act)   |
                        +--------------+-------------+
                                       |
       +-------------------------------+-------------------------------+
       |                               |                               |
       v                               v                               v
+--------------+               +---------------+               +---------------+
| Enterprise   |               | Policy RAG    |               | Verification  |
| Tool APIs    |               | Rules         |               | Engine        |
+--------------+---------------+---------------+---------------+---------------+
| - Order DB   |               | - Replacement |               | - Confirms DB |
| - Inventory  |               |   Rules       |               |   mutations   |
| - Refund API |               | - Out-of-Stock|               |   and state   |
| - Action Endp|               |   Fallback    |               |   integrity   |
+--------------+---------------+---------------+---------------+---------------+
</pre>

<table border="1" width="100%" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th align="left">Component</th>
      <th align="left">Source File</th>
      <th align="left">Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Agent Controller</b></td>
      <td><code>agent/controller.py</code></td>
      <td>Drives the autonomous ReAct loop, managing step logs and execution state.</td>
    </tr>
    <tr>
      <td><b>Enterprise APIs & DB</b></td>
      <td><code>tools/enterprise_db.py</code></td>
      <td>Simulates live microservices for Order lookup, Inventory management, and Refund processing.</td>
    </tr>
    <tr>
      <td><b>Policy RAG Engine</b></td>
      <td><code>tools/policy_rules.py</code></td>
      <td>Retrieves business rules governing allowable resolutions and fallback paths.</td>
    </tr>
    <tr>
      <td><b>Verification Engine</b></td>
      <td><code>tools/verification.py</code></td>
      <td>Audits backend database states to verify that financial and order mutations completed accurately.</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>Repository Structure</h2>

<pre>
.
├── app.py                  # Streamlit frontend dashboard
├── main.py                 # CLI execution script demonstrating the complete agent loop
├── requirements.txt        # Python package dependencies
├── README.md               # Architecture and project documentation
├── agent/
│   ├── __init__.py
│   └── controller.py       # Autonomous agent decision-making controller
└── tools/
    ├── __init__.py
    ├── enterprise_db.py    # Enterprise database and tool endpoints
    ├── policy_rules.py     # Business rule and policy RAG layer
    └── verification.py     # State mutation verification service
</pre>

<hr>

<h2>Getting Started</h2>

<h3>Prerequisites</h3>
<ul>
  <li><b>Python 3.9</b> or higher installed on your system.</li>
</ul>

<h3>Installation & Setup</h3>

<p><b>1. Clone the repository</b></p>
<pre><code>git clone https://github.com/&lt;YourUsername&gt;/&lt;TeamName&gt;_Github_Agentic.git
cd &lt;TeamName&gt;_Github_Agentic</code></pre>

<p><b>2. Create and activate a virtual environment</b></p>
<ul>
  <li>Linux / macOS:
    <pre><code>python -m venv venv
source venv/bin/activate</code></pre>
  </li>
  <li>Windows:
    <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
  </li>
</ul>

<p><b>3. Install project dependencies</b></p>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>Running the Project</h2>

<h3>Option 1: Web Dashboard (Streamlit)</h3>
<p>To launch the interactive dashboard showing real-time agent execution logs, decision paths, and state mutations:</p>
<pre><code>streamlit run app.py</code></pre>

<h3>Option 2: Command Line Interface (CLI)</h3>
<p>To run the automated resolution script directly in the terminal:</p>
<pre><code>python main.py</code></pre>

<hr>

<h2>Failure Recovery & Dynamic Adaptation</h2>

<blockquote>
  <p><b>Hackathon Core Requirement Walkthrough:</b><br>
  This system explicitly handles dynamic failure conditions through the following verified execution sequence:</p>
</blockquote>

<ol>
  <li><b>Initial Objective:</b> The user submits a ticket for Order <code>ORD-9921</code> requesting an item replacement.</li>
  <li><b>Tool Execution:</b> The agent calls <code>execute_replacement()</code>.</li>
  <li><b>Environment Failure Triggered:</b> <code>tools/enterprise_db.py</code> returns <code>OUT_OF_STOCK</code> for <code>ITEM-55</code>.</li>
  <li><b>Autonomous Adaptation:</b> The agent catches the blocking error, retrieves fallback rules from <code>policy_rules.py</code>, updates its internal plan, and automatically invokes <code>execute_refund()</code>.</li>
  <li><b>Final Outcome Verification:</b> The agent calls <code>verify_resolution()</code> to confirm that the customer balance was updated and the order state transitioned to <code>REFUNDED</code> before completing the goal.</li>
</ol>

<hr>