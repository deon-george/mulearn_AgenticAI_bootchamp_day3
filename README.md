🚀 Multi-Agent Code Generation Framework

A lightweight multi-agent system that automatically generates Python code for:

Flask API microservices

CSV analysis scripts/notebooks

The pipeline uses four agents: Planner → Researcher → Coder → Evaluator.

🔧 Features

Generate Flask API endpoints

Generate CSV analysis code (stats + charts)

Modular agent architecture

Easy to extend

Debug logs for each agent

📦 Dependencies

Install these in your environment:

pip install flask pandas matplotlib


If you’re using a virtual environment:

python3 -m venv venv
source venv/bin/activate  # fish: source venv/bin/activate.fish
pip install -r requirements.txt


(Optional) Create a requirements.txt:

flask
pandas
matplotlib

▶️ How to Run

Clone the repo:

git clone git@github.com:deon-george/mulearn_AgenticAI_bootchamp_day3.git
cd mulearn_AgenticAI_bootchamp_day3


Make sure dependencies are installed.

Run the orchestrator:

python orchestrator.py


This will execute both demos:

Demo 1: Flask API generator

Demo 2: CSV analyzer generator

You will see:

The plan

Research notes

Generated code preview

Evaluation summary

📁 Structure
agents/          # planner, researcher, coder, evaluator
orchestrator.py  # main runner
examples/
README.md
