# SIMCITY: JAKARTA BLOON EDITION™

> **A Municipal Management Game That Should Never Have Been Approved.**

A small Pygame simulation about budgets, infrastructure, traffic, flooding, projects, paperwork, meetings, and the slow realization that bureaucracy may be an unbounded state variable.

## What is it?

You manage a fictional city for **12 months**. Each month you collect revenue, pay operating costs, watch infrastructure decay, face a random municipal event, and choose one of four responses.

The game is deliberately satirical. Characters are fictional municipal archetypes, and the joke is aimed at administrative friction, project management, procurement chaos, infrastructure problems, and systems that keep interacting in inconvenient ways.

## Core variables

- **Budget** — financial reserve, cannot go below zero.
- **Infrastructure** — physical condition of the city, 0-100.
- **Public Satisfaction** — affects monthly revenue, 0-100.
- **Traffic** — congestion pressure, 0-100.
- **Flood Risk** — flood exposure, 0-100.
- **Bureaucracy** — administrative complexity; intentionally has no upper clamp.
- **Project Progress** — simplified prototype project progress, 0-100.

The current prototype contains a lightweight event system with fictional characters, decision effects, contextual BLOON commentary, and a final municipal performance report.

## Run it

Python 3.10+ and Pygame are required.

```bash
pip install -r requirements.txt
python main.py
```

Controls:

- **1-4** — choose a response
- **Enter / Space** — continue after an outcome
- **R** — restart from the final report
- **Esc** — resign from public service

## Architecture

```text
simcity_bloon/
├── main.py
├── game.py
├── city.py
├── budget.py
├── events.py
├── decisions.py
├── characters.py
├── commentary.py
├── projects.py
├── ui.py
├── config.py
├── requirements.txt
└── README.md
```

The code is intentionally modular so municipal subsystems can evolve independently as the prototype grows.

## BLOON logic

The design treats the city as a small coupled system rather than a collection of isolated upgrades.

Spend money and you have less reserve for emergencies. Add administrative controls and bureaucracy rises. Let maintenance slide and infrastructure degrades. Ignore traffic or flood risk and future events become harder to absorb.

In other words: optimize one thing, discover three other things.

## Roadmap

- **v0.1** — basic municipal simulation and Pygame dashboard
- **v0.2** — city map
- **v0.3** — roads and traffic simulation
- **v0.4** — construction projects and contractor flow
- **v0.5** — APBD / economy systems
- **v0.6** — flood simulation
- **v0.7** — procurement and contractor mini-game
- **v0.8** — save/load
- **v0.9** — campaign scenarios
- **v1.0** — full BLOONCITY

Planned features are not represented as completed features until they are actually implemented.

## BLOON municipal wisdom

> “Bureaucracy has achieved escape velocity.”

> “Vehicles are now considered permanent architecture.”

> “Nothing is delayed. The project is simply entering a more sophisticated scheduling phase.”

> “All services are now delivered via Excel. Cell C47 is responsible for drainage.”

## Status

**Prototype.** Small codebase. Real Pygame UI. Zero external game assets.

And the most important municipal question remains:

> **Who approved this?**

Nobody knows.

There was a meeting.
