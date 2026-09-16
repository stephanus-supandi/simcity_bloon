"""
commentary.py - The BLOON Commentary Engine.
Observes the city and says the quiet part, quietly.
"""

from city import City


def get_commentary(city: City) -> str:
    """Return one contextual observation, prioritized by severity of stupidity."""
    if city.is_catastrophic():
        return "Excellent. You have successfully simulated government."
    if city.bureaucracy > 120:
        return "Bureaucracy has begun issuing permits to itself."
    if city.bureaucracy > 90:
        return "Bureaucracy has achieved escape velocity."
    if city.budget < 100:
        return "The treasury is experiencing spiritual emptiness."
    if city.flood_risk > 90:
        return "Congratulations. The city has become an aquatic city."
    if city.flood_risk > 75:
        return "Fish have been observed in the underpass. This is now a stocking opportunity."
    if city.traffic > 90:
        return "Vehicles are now considered permanent architecture."
    if city.traffic > 75:
        return "A family has celebrated two birthdays in the same traffic jam."
    if city.satisfaction < 20:
        return "Citizens have discovered the comment section."
    if city.satisfaction > 85:
        return "Public satisfaction is suspiciously high. An audit has been scheduled."
    if city.infrastructure < 30:
        return "The infrastructure is held together by habit and one very dedicated bridge."
    if city.infrastructure > 80:
        return "Infrastructure is excellent. Somewhere, a form has been filed incorrectly."
    if city.project_progress < 10:
        return "Project progress is technically nonzero. Legally, that counts."
    return "The city continues. No reason given. None required."


def get_monthly_summary(city: City, revenue: int, cost: int) -> str:
    """Short fiscal note for the monthly report panel."""
    net = revenue - cost
    if net >= 0:
        return (
            "Revenue Rp " + str(revenue) + " B / Costs Rp " + str(cost)
            + " B - Surplus. Finance is confused but silent."
        )
    return (
        "Revenue Rp " + str(revenue) + " B / Costs Rp " + str(cost)
        + " B - Deficit of Rp " + str(abs(net))
        + " B. This has been noted. Noted is all it will ever be."
    )
