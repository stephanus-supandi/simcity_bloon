"""
config.py - All tunable constants for SIMCITY: JAKARTA BLOON EDITION.
"""

# --- Window ---
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
FPS = 60
TITLE = "SIMCITY: JAKARTA BLOON EDITION"
SUBTITLE = "A Municipal Management Game That Should Never Have Been Approved."

# --- Game rules ---
TOTAL_MONTHS = 12
MONTHLY_REVENUE_BASE = 90
MONTHLY_OPERATING_COST = 55
INFRA_DECAY_PER_MONTH = 2

# --- Starting city state ---
START_BUDGET = 1000
START_INFRASTRUCTURE = 55
START_SATISFACTION = 50
START_TRAFFIC = 65
START_FLOOD_RISK = 60
START_BUREAUCRACY = 70
START_PROJECT_PROGRESS = 0

# --- Stat clamps ---
# Bureaucracy is deliberately excluded from clamping.
STAT_MIN = 0
STAT_MAX = 100

# --- Colors ---
# Procedural, no assets, like a properly underfunded project.
COLOR_BG = (18, 22, 28)
COLOR_PANEL = (30, 36, 44)
COLOR_PANEL_LIGHT = (40, 48, 58)
COLOR_BORDER = (70, 80, 92)
COLOR_TEXT = (220, 225, 230)
COLOR_TEXT_DIM = (140, 150, 160)
COLOR_ACCENT = (240, 180, 60)
COLOR_GOOD = (110, 200, 130)
COLOR_BAD = (220, 90, 90)
COLOR_BUTTON = (55, 66, 80)
COLOR_BUTTON_HOVER = (75, 90, 108)
COLOR_TITLE_BG = (24, 28, 36)

# --- Layout ---
HEADER_HEIGHT = 70
FOOTER_HEIGHT = 40
LEFT_PANEL_WIDTH = 300
RIGHT_PANEL_WIDTH = 340
BUTTON_HEIGHT = 62
BUTTON_MARGIN = 8

# --- Fonts ---
# Default system font; asset-free like our budget.
FONT_TITLE = 30
FONT_HEADER = 20
FONT_BODY = 17
FONT_SMALL = 14
