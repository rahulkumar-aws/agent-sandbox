from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class AgentState:
    inventory: List[str] = field(default_factory=list)
    history: List[Dict[str, Any]] = field(default_factory=list)
    resolved: bool = False
    
    def update_from_observation(self, action: str, feedback: Any):
        self.history.append({"action": action, "feedback": feedback})