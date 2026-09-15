from dataclasses import dataclass
from typing import Callable, Tuple
from agent_sandbox.environment.world import World
from agent_sandbox.agent.state import AgentState
from agent_sandbox.agent.policy import choose_action
from agent_sandbox.tools.actions import execute_action

@dataclass
class Task:
    name: str
    description: str
    is_goal: Callable[[AgentState, World], bool]
    setup: Callable[[World, AgentState], None] = lambda world, state: None

class Sandbox:
    def run_task(self, task: Task, max_steps: int = 30, verbose: bool = True) -> Tuple[World, AgentState, bool]:
        world = World()
        state = AgentState(max_steps=max_steps)
        task.setup(world, state)
        
        if verbose:
            print(f"=== Task: {task.name} ===")
            print(task.description)
            print()
            
        initial_obs = world.look()
        state.update_from_observation(world, initial_obs)
        state.steps_taken += 1
        
        if verbose:
            print(f"[Step 1] Initial observation:\n{initial_obs}\n")
        
        while state.steps_taken < state.max_steps:
            if task.is_goal(state, world):
                return world, state, True
                
            # 1. Reason
            action = choose_action(state, world)
            if verbose:
                print(f"[Step {state.steps_taken}] Agent chooses action: {action}")
                
            if action == "idle":
                break
                
            # 2. Act
            observation = execute_action(world, action)
            if verbose:
                print(f"Environment says:\n{observation}")
            
            # 3. Observe
            state.update_from_observation(world, observation)
            
            if verbose:
                print(f"Current room: {state.current_room}, Inventory: {state.inventory}\n")
                
            state.steps_taken += 1
            
        success = task.is_goal(state, world)
        return world, state, success