from agent_sandbox.agent.state import AgentState

def goal_achieved(state: AgentState) -> bool:
    return state.goal_item in state.inventory

def should_stop(state: AgentState) -> bool:
    if goal_achieved(state):
        return True
    if state.steps_taken >= state.max_steps:
        return True
    return False