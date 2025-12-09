import sys
import os

# Ensure the current directory is in the path so we can import agent_system
sys.path.append(os.getcwd())

from agent_system import run_agent_team

def run_demo():
    print("========================================")
    print("DEMO 1: FLASK API MICROSERVICE")
    print("========================================")
    
    with open("agent_system/examples/example_api_goal.txt", "r") as f:
        api_goal = f.read().strip()
        
    api_result = run_agent_team(api_goal, mode="api")
    
    print("\n--- API RESULT CODE PREVIEW ---")
    print(api_result["code"][:200] + "...\n")
    print("Evaluation:", api_result["review"])

    print("\n\n========================================")
    print("DEMO 2: CSV ANALYZER NOTEBOOK")
    print("========================================")
    
    with open("agent_system/examples/example_csv_goal.txt", "r") as f:
        csv_goal = f.read().strip()
        
    csv_result = run_agent_team(csv_goal, mode="csv")
    
    print("\n--- CSV RESULT CODE PREVIEW ---")
    print(csv_result["code"][:200] + "...\n")
    print("Evaluation:", csv_result["review"])

if __name__ == "__main__":
    run_demo()
