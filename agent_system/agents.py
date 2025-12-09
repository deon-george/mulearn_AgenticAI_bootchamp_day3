from .templates import (
    PLANNER_PROMPT, 
    RESEARCHER_PROMPT, 
    CODER_PROMPT_API, 
    CODER_PROMPT_CSV, 
    EVALUATOR_PROMPT
)
from .utils import call_llm

class Agent:
    def __init__(self, name):
        self.name = name

    def run(self, **kwargs):
        raise NotImplementedError

class PlannerAgent(Agent):
    def __init__(self):
        super().__init__("Planner")

    def run(self, goal: str, mode: str) -> str:
        prompt = PLANNER_PROMPT.format(goal=goal, mode=mode)
        return call_llm(prompt)

class ResearchAgent(Agent):
    def __init__(self):
        super().__init__("Researcher")

    def run(self, plan: str) -> str:
        prompt = RESEARCHER_PROMPT.format(plan=plan)
        return call_llm(prompt)

class CodingAgent(Agent):
    def __init__(self):
        super().__init__("Coder")

    def run(self, goal: str, plan: str, research: str, mode: str) -> str:
        if mode == 'api':
            prompt_template = CODER_PROMPT_API
        else:
            prompt_template = CODER_PROMPT_CSV
            
        prompt = prompt_template.format(goal=goal, plan=plan, research=research)
        return call_llm(prompt)

class EvaluationAgent(Agent):
    def __init__(self):
        super().__init__("Evaluator")

    def run(self, code: str) -> str:
        prompt = EVALUATOR_PROMPT.format(code=code)
        return call_llm(prompt)
