class Agent:
    def __init__(self, goal, state, policy):
        self.goal = goal
        self.state = state
        self.policy = policy

    def goal_reached(self):
        # The convergence condition for this specific example
        return "treasure" in self.state.inventory

    def should_stop(self):
        return self.state.resolved