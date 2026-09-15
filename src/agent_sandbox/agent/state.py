from dataclasses import dataclass, field
from typing import Dict, List
from agent_sandbox.environment.world import World

@dataclass
class AgentState:
    current_room: str = "hall"
    known_items: Dict[str, List[str]] = field(default_factory=dict)
    inventory: List[str] = field(default_factory=list)
    steps_taken: int = 0
    max_steps: int = 20
    goal_item: str = "treasure"

    def update_from_observation(self, world: World, observation: str):
        self.current_room = world.agent_location
        self.inventory = list(world.agent_inventory)
        for line in observation.splitlines():
            line = line.strip()
            if line.startswith("You see:"):
                items_part = line[len("You see:"):].strip()
                items = [x.strip() for x in items_part.split(",")] if items_part and "nothing special" not in items_part else []
                self.known_items[self.current_room] = items