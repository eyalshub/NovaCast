from typing import Any, Dict, Optional

class ChatSession:
    def __init__(self, session_id: str, user_id: str):
        self.session_id = session_id
        self.user_id = user_id
        self.state: Dict[str, Any] = {}
        self.vector_memory: Optional[Dict[str, Any]] = None

    def set_state(self, key: str, value: Any) -> None:
        self.state[key] = value

    def get_state(self, key: str) -> Any:
        return self.state.get(key)

    def clear_state(self) -> None:
        self.state.clear()

    def set_vector_memory(self, memory: Dict[str, Any]) -> None:
        self.vector_memory = memory

    def get_vector_memory(self) -> Optional[Dict[str, Any]]:
        return self.vector_memory

    def clear_vector_memory(self) -> None:
        self.vector_memory = None

# This file is responsible for managing session state and vector memory for chatbot interactions.