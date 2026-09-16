"""
city.py - The city itself. A dataclass holding numbers that slowly get worse.
"""

from dataclasses import dataclass, field

import config


@dataclass
class City:
    budget: int = config.START_BUDGET
    infrastructure: int = config.START_INFRASTRUCTURE
    satisfaction: int = config.START_SATISFACTION
    traffic: int = config.START_TRAFFIC
    flood_risk: int = config.START_FLOOD_RISK
    bureaucracy: int = config.START_BUREAUCRACY
    project_progress: int = config.START_PROJECT_PROGRESS
    month: int = 1
    meetings: int = 0
    documents_lost: int = 0
    projects_completed: int = 0
    feasibility_studies: int = 0
    log: list = field(default_factory=list)

    def apply(self, effects: dict) -> None:
        """Apply a dict of stat deltas to matching attributes."""
        for key in effects:
            delta = effects[key]
            if hasattr(self, key):
                setattr(self, key, getattr(self, key) + delta)
        self.clamp()

    def clamp(self) -> None:
        """Clamp budget and selected city statistics."""
        self.budget = max(0, self.budget)
        for attr in (
            "infrastructure",
            "satisfaction",
            "traffic",
            "flood_risk",
            "project_progress",
        ):
            value = getattr(self, attr)
            value = max(config.STAT_MIN, min(config.STAT_MAX, value))
            setattr(self, attr, value)

    def add_log(self, text: str) -> None:
        self.log.insert(0, text)
        if len(self.log) > 8:
            self.log.pop()

    def is_catastrophic(self) -> bool:
        return self.budget < 85 and self.flood_risk > 85
