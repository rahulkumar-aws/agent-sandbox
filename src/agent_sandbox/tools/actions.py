def execute_action(environment, **kwargs):
    """The unified tool execution layer."""
    action_type = kwargs.get("action_type")
    
    if action_type == "look":
        return environment.look()
    elif action_type == "take":
        return environment.take(kwargs.get("item"))
    elif action_type == "move":
        return environment.move(kwargs.get("direction"))
        
    return f"Unknown action: {action_type}"