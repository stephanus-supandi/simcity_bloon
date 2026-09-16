"""
budget.py - Revenue and spending.
"""

import config
from city import City


def monthly_revenue(city: City) -> int:
    """Revenue scales with satisfaction."""
    factor = 0.6 + (city.satisfaction / 100.0) * 0.8
    return int(config.MONTHLY_REVENUE_BASE * factor)


def monthly_operating_cost(city: City) -> int:
    """Operating costs scale with bureaucracy above 50."""
    excess = city.bureaucracy - 50
    if excess > 0:
        factor = 1.0 + excess / 150.0
    else:
        factor = 1.0
    return int(config.MONTHLY_OPERATING_COST * factor)


def run_monthly_finance(city: City) -> tuple:
    """Collect revenue, pay costs, and return (revenue, cost)."""
    revenue = monthly_revenue(city)
    cost = monthly_operating_cost(city)
    city.apply({"budget": revenue - cost})
    return (revenue, cost)
