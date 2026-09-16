"""
projects.py - v0.1 STUB.

Project definitions are reserved for the construction-project system.
The current prototype uses a simplified global project_progress value.
"""

import copy
from dataclasses import dataclass
from typing import List


@dataclass
class Project:
    name: str
    cost: int
    duration: int
    progress: int = 0
    maintenance: int = 2
    risk: int = 5
    completed: bool = False


STANDARD_PROJECTS: List[Project] = [
    Project("Drainage Upgrade", cost=120, duration=6, risk=8),
    Project("Road Repair", cost=90, duration=4, risk=6),
    Project("Pump Station", cost=150, duration=8, risk=10),
    Project("Bridge Repair", cost=110, duration=5, risk=7),
    Project("Public Transport", cost=200, duration=10, risk=12),
    Project("Flood Control", cost=180, duration=9, risk=9),
]


def get_projects() -> List[Project]:
    """Return fresh project definitions for a new game."""
    return copy.deepcopy(STANDARD_PROJECTS)
