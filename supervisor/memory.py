# PATH: supervisor/memory.py

from collections import defaultdict
from typing import List


class SessionMemory:
    def __init__(self):
        self.store = defaultdict(list)

    def add(self, session_id: str, message: str):
        self.store[session_id].append(message)

    def get_context(self, session_id: str, limit: int = 5) -> List[str]:
        return self.store[session_id][-limit:]
