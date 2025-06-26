import heapq
from src.use_cases.use_case_base import UseCaseBase
from typing import List, Tuple, Dict, Any

class ActionsQueue:
    def __init__(self):
        self._queue: List[Tuple[int, int, Dict[str, Any]]] = []
        self._index = 0

    def add_action(self, action: UseCaseBase, *args: Any, delay: float = 5):
        heapq.heappush(self._queue, (action.priority, self._index, {
            'action': action,
            'args': args,
            'delay': delay
        }))
        self._index += 1

    def get_next_action(self):
        if self._queue:
            return heapq.heappop(self._queue)[2]
        return None

    def has_action(self):
        return len(self._queue) > 0

    def peek(self):
        if self.has_action():
            return self._queue[0][2]
        return None