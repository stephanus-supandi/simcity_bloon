"""
decisions.py - Resolves player decisions into consequences.
"""

from city import City
from events import Option


def apply_decision(city: City, option: Option) -> tuple:
    """Apply an option's effects and return (result, followup)."""
    cost = option.effects.get("budget", 0)
    if cost < 0 and city.budget + cost < 0:
        return (
            "INSUFFICIENT BUDGET. The finance department has rejected the request using a stamp you didn't know existed.",
            "Consider a cheaper form of denial. Choose another response.",
        )
    city.apply(option.effects)
    return option.result, option.followup
