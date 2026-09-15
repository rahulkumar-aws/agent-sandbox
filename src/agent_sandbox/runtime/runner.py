"""
The Runtime Orchestrator.
Contains the Sandbox, Task definitions, and the core execution loop.
"""
from dataclasses import dataclass
from typing import List, Callable, Any

@dataclass
class Task:
    """Represents the objective the agent needs to achieve."""
    description: str

@dataclass
class Sandbox:
    """The execution environment and the tools available to the agent."""
    environment: Any
    tools: List[Callable]

def run_episode(agent, sandbox: Sandbox, task: Task, max_steps: int = 10) -> Any:
    """
    The core ReAct control loop.
    Iteratively runs Observe -> Decide -> Act until termination.
    """
    print(f"Task: {task.description}")
    
    step = 0
    while not agent.should_stop() and step < max_steps:
        step += 1
        print(f"\n--- Cycle {step} ---")
        
        # 1. Decide (Policy selects the next action based on current state)
        action_name, args = agent.policy(agent.state)
        print(f"[Decide] Emitted action: {action_name} with args: {args}")
        
        # 2. Check early termination
        if action_name == "stop":
            print("[Terminate] Agent decided to halt.")
            agent.state.resolved = True
            break
            
        # 3. Act (Execute the discrete tool against the environment)
        tool_func = next((t for t in sandbox.tools if t.__name__ == action_name), None)
        
        if tool_func:
            feedback = tool_func(sandbox.environment, **args)
        else:
            feedback = f"Error: Tool '{action_name}' not found in registered effectors."
            
        print(f"[Act] Executed {action_name}. Feedback: {feedback}")
        
        # 4. Observe (Ingest feedback back into the agent's state)
        agent.state.update_from_observation(action_name, feedback)
        
        # 5. Evaluate Termination Condition
        if agent.goal_reached():
            print("[Terminate] Goal convergence achieved!")
            agent.state.resolved = True
            break

    if not getattr(agent.state, 'resolved', False):
        print(f"\n[Terminate] Max iterations ({max_steps}) reached without convergence.")
        
    return agent.state