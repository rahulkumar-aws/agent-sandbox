"""
Runnable entry point for the Deterministic Agent.
Maps to scenarios like: 'Example: get treasure'
"""
from agent_sandbox.environment.world import World
from agent_sandbox.agent.agent import Agent
from agent_sandbox.agent.policy import choose_action
from agent_sandbox.agent.state import AgentState
from agent_sandbox.runtime.runner import Sandbox, Task, run_episode
from agent_sandbox.tools.actions import execute_action

def main():
    # 1. Initialize the Environment
    world = World(name="Treasure Room")
    
    # 2. Define the Goal and Initial State
    goal = "get treasure"
    initial_state = AgentState(inventory=[], history=[])
    
    # 3. Initialize the Agent
    agent = Agent(
        goal=goal,
        state=initial_state,
        policy=choose_action
    )
    
    # 4. Set up the Runtime (Sandbox and Task)
    task = Task(description="Find and collect the hidden treasure.")
    sandbox = Sandbox(environment=world, tools=[execute_action])
    
    # 5. Execute the Control Loop
    print(f"🎯 Starting execution for goal: {agent.goal}")
    final_state = run_episode(agent, sandbox, task)
    
    print(f"\n[Final Outcome]: {final_state.resolved}")

if __name__ == "__main__":
    main()