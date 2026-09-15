def choose_action(state):
    """A deterministic reasoning engine that decides the next step based on state history."""
    if not state.history:
        return "execute_action", {"action_type": "look"}
        
    last_feedback = state.history[-1]["feedback"]
    
    if "treasure" in str(last_feedback) and "treasure" not in state.inventory:
        state.inventory.append("treasure") 
        return "execute_action", {"action_type": "take", "item": "treasure"}
        
    if "treasure" in state.inventory:
        return "stop", {}
        
    return "execute_action", {"action_type": "move", "direction": "north"}