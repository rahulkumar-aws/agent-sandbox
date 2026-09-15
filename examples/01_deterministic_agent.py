from agent_sandbox.runtime.runner import Task, Sandbox
from agent_sandbox.agent.state import AgentState
from agent_sandbox.environment.world import World

def goal_has_treasure(state: AgentState, world: World) -> bool:
    return "treasure" in state.inventory

def main():
    task = Task(
        name="Get the Treasure",
        description="Start in the hall. Obtain the treasure and hold it in your inventory.",
        is_goal=goal_has_treasure
    )
    
    sandbox = Sandbox()
    world, state, success = sandbox.run_task(task)
    
    print(f"\nTask '{task.name}' success: {success}")
    print("Final inventory:", state.inventory)
    print("Final room:", state.current_room)

if __name__ == "__main__":
    main()