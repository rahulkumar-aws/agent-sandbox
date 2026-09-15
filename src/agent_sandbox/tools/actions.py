from agent_sandbox.environment.world import World

def execute_action(world: World, action: str) -> str:
    tokens = action.split()
    if not tokens:
        return "No action."
        
    verb = tokens[0]
    args = tokens[1:]
    
    # 🛠️ New logging to print which tool is being called
    print(f"🛠️ [Act] Invoking Tool: '{verb}' with Args: {args}")
    
    if verb == "move" and len(tokens) == 2:
        return world.move(tokens[1])
    elif verb == "look":
        return world.look()
    elif verb == "take" and len(tokens) == 2:
        return world.take(tokens[1])
    elif verb == "inventory":
        return world.inventory()
    elif verb == "idle":
        return "Agent is idle."
    else:
        return f"Unknown action: {action}"