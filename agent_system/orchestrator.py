from .agents import PlannerAgent, ResearchAgent, CodingAgent, EvaluationAgent

def run_agent_team(goal: str, mode: str) -> dict:
    """
    Orchestrates the multi-agent team to achieve the goal.
    
    Args:
        goal (str): The user's goal description.
        mode (str): 'api' or 'csv'.
        
    Returns:
        dict: A dictionary containing the outputs from each agent.
    """
    print(f"--- Starting Agent Team for goal: '{goal}' (Mode: {mode}) ---")
    
    # Initialize Agents
    planner = PlannerAgent()
    researcher = ResearchAgent()
    coder = CodingAgent()
    evaluator = EvaluationAgent()
    
    # Step 1: Planning
    print("1. Planner Agent is working...")
    plan_output = planner.run(goal=goal, mode=mode)
    
    # Step 2: Research
    print("2. Researcher Agent is working...")
    research_output = researcher.run(plan=plan_output)
    
    # Step 3: Coding
    print("3. Coding Agent is working...")
    code_output = coder.run(goal=goal, plan=plan_output, research=research_output, mode=mode)
    
    # Step 4: Evaluation
    print("4. Evaluation Agent is working...")
    review_output = evaluator.run(code=code_output)
    
    print("--- Agent Team Completed ---")
    
    return {
        "plan": plan_output,
        "research": research_output,
        "code": code_output,
        "review": review_output
    }
