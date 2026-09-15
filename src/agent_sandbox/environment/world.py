from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class World:
    rooms: Dict[str, Dict] = field(default_factory=dict)
    agent_location: str = "hall"
    agent_inventory: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self.rooms:
            self.rooms = {
                "hall": {
                    "description": "You are in the hall. Doors lead to the kitchen and the study.",
                    "neighbors": {"north": "kitchen", "east": "study"},
                    "items": [],
                },
                "kitchen": {
                    "description": "You are in the kitchen. It smells of tea.",
                    "neighbors": {"south": "hall"},
                    "items": ["key"],
                },
                "study": {
                    "description": "You are in the study. There is a locked chest here.",
                    "neighbors": {"west": "hall"},
                    "items": ["treasure"],
                },
            }

    def move(self, direction: str) -> str:
        room = self.rooms[self.agent_location]
        neighbors = room["neighbors"]
        if direction not in neighbors:
            return f"You can't go {direction} from here."
        self.agent_location = neighbors[direction]
        return f"You move {direction} to the {self.agent_location}."

    def look(self) -> str:
        room = self.rooms[self.agent_location]
        desc = room["description"]
        items = room["items"]
        item_text = "You see: " + ", ".join(items) if items else "You see nothing special."
        return f"{desc}\n{item_text}"

    def take(self, item: str) -> str:
        room = self.rooms[self.agent_location]
        if item not in room["items"]:
            return f"There is no {item} here."
        room["items"].remove(item)
        self.agent_inventory.append(item)
        return f"You take the {item}."

    def inventory(self) -> str:
        if not self.agent_inventory:
            return "You are carrying nothing."
        return "You are carrying: " + ", ".join(self.agent_inventory)