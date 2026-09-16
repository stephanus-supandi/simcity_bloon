"""
characters.py - Fictional municipal archetypes.
Any resemblance to actual engineers, bureaucrats, or contractors is
statistically inevitable and legally denied.
"""

import random


CHARACTERS = {
    "THE MANAGER": [
        "Let's circle back on this.",
        "What's the timeline? Don't answer. I don't want to know the timeline.",
        "This is a great opportunity for synergy.",
        "I need this by yesterday, which has passed, so we're already late.",
        "Who approved this? Rhetorical. Nobody approves anything. That's the system.",
    ],
    "THE ENGINEER": [
        "The drainage capacity is insufficient.",
        "That is not how soil works. That is not how ANY of this works.",
        "We can fix it, or we can fix it on paper. Budget only allows one.",
        "The pump is rated for water, not for this.",
        "I have a degree. The degree has given up.",
    ],
    "THE BUREAUCRAT": [
        "Please submit Form 17B.",
        "Form 17B requires Form 17A. Form 17A requires Form 17B.",
        "The stamp is with someone who is on leave. The leave is indefinite.",
        "This was approved, but in a meeting that never happened.",
        "I don't make the rules. I make the forms about the rules.",
    ],
    "THE CONTRACTOR": [
        "We can finish next month.",
        "The materials are 'in transit'. The transit has no origin or destination.",
        "This is within tolerance. The tolerance is very wide.",
        "Rain delayed us. It was not raining. We were delayed anyway.",
        "The price changed. Prices do that.",
    ],
    "THE CITIZEN": [
        "The road in front of my house has been 'under construction' since 2021.",
        "My motorcycle is now part of the flood control system.",
        "I attended a public hearing. The public hearing was not public.",
        "The app crashed. The pothole did not.",
        "Please fix the traffic. Or the flood. Or anything. I'm flexible now.",
    ],
}


EXCHANGES = [
    ("THE CONTRACTOR", "We can finish next month.", "THE GAME", "That was three months ago."),
    ("THE ENGINEER", "The design is sound.", "THE BUREAUCRAT", "The design is also unsigned."),
    ("THE MANAGER", "Let's take this offline.", "THE ENGINEER", "'Offline' is a drainage channel. It is currently full."),
    ("THE CITIZEN", "When will the project be done?", "THE CONTRACTOR", "Soon."),
]


def get_character_line() -> tuple:
    """Return (name, line)."""
    name = random.choice(list(CHARACTERS.keys()))
    return name, random.choice(CHARACTERS[name])


def get_exchange() -> tuple:
    """Return a 4-tuple: (name1, line1, name2, line2)."""
    return random.choice(EXCHANGES)
