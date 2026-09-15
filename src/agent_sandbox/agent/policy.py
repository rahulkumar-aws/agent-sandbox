from agent_sandbox.agent.state import AgentState
from agent_sandbox.environment.world import World

def choose_action(state: AgentState, world: World) -> str:
    # 1. Stop if goal is achieved
    if state.goal_item in state.inventory:
        return "idle"
        
    # 2. Look first if we haven't mapped this room's items yet
    if state.current_room not in state.known_items:
        return "look"
        
    items_here = state.known_items.get(state.current_room, [])
    
    # 3. Take goal item or other items
    if state.goal_item in items_here:
        return f"take {state.goal_item}"
    if items_here:
        return f"take {items_here[0]}"
        
    # 4. Move, but avoid the infinite loop trap
    room = world.rooms[state.current_room]
    directions = ["north", "east", "south", "west"]
    
    # If we are in the hall and have the key, don't go back to the kitchen
    if state.current_room == "hall" and "key" in state.inventory:
        directions.remove("north")
        
    for direction in directions:
        if direction in room["neighbors"]:
            return f"move {direction}"
            
    return "look"