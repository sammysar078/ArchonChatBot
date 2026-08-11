from collections import defaultdict
from typing import Dict, List

# Temporary in-memory context.
# Later we will move this to a database.
_context: Dict[int, List[dict]] = defaultdict(list)

MAX_HISTORY = 12


def add_user_message(user_id: int, text: str):
    _context[user_id].append({"role": "user", "content": text})
    if len(_context[user_id]) > MAX_HISTORY:
        _context[user_id] = _context[user_id][-MAX_HISTORY:]


def add_assistant_message(user_id: int, text: str):
    _context[user_id].append({"role": "assistant", "content": text})
    if len(_context[user_id]) > MAX_HISTORY:
        _context[user_id] = _context[user_id][-MAX_HISTORY:]


def get_context(user_id: int):
    return list(_context[user_id])


def clear_context(user_id: int):
    _context[user_id].clear()
