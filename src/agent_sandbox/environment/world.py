from dataclasses import dataclass

@dataclass
class World:
    name: str
    current_room: str = "Entrance"
    items: dict = None

    def __post_init__(self):
        if self.items is None:
            self.items = {"Entrance": ["treasure"]}
            
    def look(self):
        return f"You are in {self.current_room}. Items here: {self.items.get(self.current_room, [])}"
        
    def take(self, item):
        room_items = self.items.get(self.current_room, [])
        if item in room_items:
            room_items.remove(item)
            return f"Picked up {item}."
        return f"{item} not found."
        
    def move(self, direction):
        return f"Moved {direction}."