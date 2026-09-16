"""
ui.py - Rendering for the BLOON municipal dashboard.
No external assets required.
"""

import pygame

import config


def fit_text(text, font, max_width):
    if font.size(text)[0] <= max_width:
        return text
    while text and font.size(text + "...")[0] > max_width:
        text = text[:-1]
    return text + "..."


class Button:
    def __init__(self, rect, label, sublabel=""):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.sublabel = sublabel

    def draw(self, surface, font, small_font, mouse_pos):
        hovered = self.rect.collidepoint(mouse_pos)
        color = config.COLOR_BUTTON_HOVER if hovered else config.COLOR_BUTTON
        pygame.draw.rect(surface, color, self.rect, border_radius=6)
        pygame.draw.rect(surface, config.COLOR_BORDER, self.rect, width=1, border_radius=6)

        max_w = self.rect.width - 24
        label = fit_text(self.label, font, max_w)
        text = font.render(label, True, config.COLOR_TEXT)
        surface.blit(text, (self.rect.x + 12, self.rect.y + 8))

        if self.sublabel:
            sublabel = fit_text(self.sublabel, small_font, max_w)
            sub = small_font.render(sublabel, True, config.COLOR_ACCENT)
            surface.blit(sub, (self.rect.x + 12, self.rect.y + 8 + font.get_height() + 4))


def make_fonts():
    return {
        "title": pygame.font.SysFont("consolas,arial", config.FONT_TITLE, bold=True),
        "header": pygame.font.SysFont("consolas,arial", config.FONT_HEADER, bold=True),
        "body": pygame.font.SysFont("consolas,arial", config.FONT_BODY),
        "body_bold": pygame.font.SysFont("consolas,arial", config.FONT_BODY, bold=True),
        "small": pygame.font.SysFont("consolas,arial", config.FONT_SMALL),
        "small_bold": pygame.font.SysFont("consolas,arial", config.FONT_SMALL, bold=True),
    }


def wrap_text(text, font, max_width):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_header(screen, fonts, month):
    pygame.draw.rect(screen, config.COLOR_TITLE_BG, (0, 0, config.WINDOW_WIDTH, config.HEADER_HEIGHT))
    pygame.draw.line(screen, config.COLOR_BORDER, (0, config.HEADER_HEIGHT), (config.WINDOW_WIDTH, config.HEADER_HEIGHT), 2)
    title = fonts["title"].render(config.TITLE, True, config.COLOR_ACCENT)
    screen.blit(title, (20, 8))
    sub = fonts["small"].render(config.SUBTITLE, True, config.COLOR_TEXT_DIM)
    screen.blit(sub, (22, 46))
    month_text = fonts["header"].render("MONTH " + str(month) + " / " + str(config.TOTAL_MONTHS), True, config.COLOR_TEXT)
    screen.blit(month_text, (config.WINDOW_WIDTH - month_text.get_width() - 20, 12))


def draw_stat_row(screen, fonts, x, y, label, value, max_val=None, color=None, width=260):
    text_color = color if color is not None else config.COLOR_TEXT
    label_surf = fonts["body"].render(label, True, config.COLOR_TEXT_DIM)
    screen.blit(label_surf, (x, y))
    value_surf = fonts["body_bold"].render(str(value), True, text_color)
    screen.blit(value_surf, (x + width - value_surf.get_width(), y))
    if max_val is not None:
        bar_w = width
        bar_h = 5
        bar_y = y + 22
        pygame.draw.rect(screen, config.COLOR_PANEL_LIGHT, (x, bar_y, bar_w, bar_h), border_radius=2)
        fill = max(0.0, min(1.0, value / float(max_val)))
        bar_color = color if color is not None else config.COLOR_GOOD
        pygame.draw.rect(screen, bar_color, (x, bar_y, int(bar_w * fill), bar_h), border_radius=2)
        return bar_h + 8
    return 4


def draw_left_panel(screen, fonts, city):
    panel = pygame.Rect(0, config.HEADER_HEIGHT, config.LEFT_PANEL_WIDTH, config.WINDOW_HEIGHT - config.HEADER_HEIGHT - config.FOOTER_HEIGHT)
    pygame.draw.rect(screen, config.COLOR_PANEL, panel)
    pygame.draw.line(screen, config.COLOR_BORDER, panel.topright, panel.bottomright, 2)

    x = 20
    y = panel.y + 16
    header = fonts["header"].render("CITY STATISTICS", True, config.COLOR_ACCENT)
    screen.blit(header, (x, y))
    y += 34

    budget_color = config.COLOR_BAD if city.budget < 150 else config.COLOR_GOOD
    y += draw_stat_row(screen, fonts, x, y, "BUDGET (Rp B)", city.budget, color=budget_color) + 30
    y += draw_stat_row(screen, fonts, x, y, "INFRASTRUCTURE", city.infrastructure, max_val=100) + 32
    y += draw_stat_row(screen, fonts, x, y, "PUBLIC SATISFACTION", city.satisfaction, max_val=100, color=config.COLOR_GOOD) + 32
    y += draw_stat_row(screen, fonts, x, y, "TRAFFIC", city.traffic, max_val=100, color=config.COLOR_BAD) + 32
    y += draw_stat_row(screen, fonts, x, y, "FLOOD RISK", city.flood_risk, max_val=100, color=config.COLOR_BAD) + 32
    y += draw_stat_row(screen, fonts, x, y, "BUREAUCRACY", city.bureaucracy, max_val=150, color=config.COLOR_ACCENT) + 32
    y += draw_stat_row(screen, fonts, x, y, "PROJECT PROGRESS", city.project_progress, max_val=100) + 40

    pygame.draw.line(screen, config.COLOR_BORDER, (x, y), (panel.width - 20, y), 1)
    y += 12
    counters = fonts["small"].render("Meetings: " + str(city.meetings) + "    Documents lost: " + str(city.documents_lost), True, config.COLOR_TEXT_DIM)
    screen.blit(counters, (x, y))
    y += 20
    counters2 = fonts["small"].render("Projects done: " + str(city.projects_completed) + "    Studies: " + str(city.feasibility_studies), True, config.COLOR_TEXT_DIM)
    screen.blit(counters2, (x, y))


def draw_center_panel(screen, fonts, event, phase, result_text, followup_text, commentary):
    x0 = config.LEFT_PANEL_WIDTH
    x1 = config.WINDOW_WIDTH - config.RIGHT_PANEL_WIDTH
    panel = pygame.Rect(x0, config.HEADER_HEIGHT, x1 - x0, config.WINDOW_HEIGHT - config.HEADER_HEIGHT - config.FOOTER_HEIGHT)
    pad = 24
    inner_w = panel.width - pad * 2
    y = panel.y + pad

    if phase == "decision":
        tag = fonts["small"].render("MUNICIPAL EVENT", True, config.COLOR_BAD)
        screen.blit(tag, (x0 + pad, y))
        y += 22
        for line in wrap_text(event.title, fonts["header"], inner_w):
            screen.blit(fonts["header"].render(line, True, config.COLOR_TEXT), (x0 + pad, y))
            y += 28
        y += 8
        for line in wrap_text(event.description, fonts["body"], inner_w):
            screen.blit(fonts["body"].render(line, True, config.COLOR_TEXT_DIM), (x0 + pad, y))
            y += 24
        y += 16
        hint = fonts["small"].render("Select a response below (keys 1-4). All responses are wrong. Some are cheaper.", True, config.COLOR_TEXT_DIM)
        screen.blit(hint, (x0 + pad, y))

    elif phase == "result":
        tag = fonts["small"].render("OUTCOME", True, config.COLOR_GOOD)
        screen.blit(tag, (x0 + pad, y))
        y += 22
        for line in wrap_text(event.title, fonts["header"], inner_w):
            screen.blit(fonts["header"].render(line, True, config.COLOR_TEXT_DIM), (x0 + pad, y))
            y += 28
        y += 8
        for line in wrap_text(result_text, fonts["body_bold"], inner_w):
            screen.blit(fonts["body_bold"].render(line, True, config.COLOR_TEXT), (x0 + pad, y))
            y += 24
        if followup_text:
            y += 14
            for line in wrap_text(followup_text, fonts["body"], inner_w):
                screen.blit(fonts["body"].render(line, True, config.COLOR_TEXT_DIM), (x0 + pad, y))
                y += 24

    if commentary:
        box_h = 104
        box = pygame.Rect(x0 + pad, panel.bottom - box_h - 18, inner_w, box_h)
        pygame.draw.rect(screen, config.COLOR_PANEL_LIGHT, box, border_radius=6)
        pygame.draw.rect(screen, config.COLOR_BORDER, box, width=1, border_radius=6)
        label = fonts["small_bold"].render("BLOON COMMENTARY", True, config.COLOR_ACCENT)
        screen.blit(label, (box.x + 12, box.y + 10))
        yy = box.y + 34
        for line in wrap_text(commentary, fonts["body"], box.width - 24)[:2]:
            screen.blit(fonts["body"].render(line, True, config.COLOR_TEXT), (box.x + 12, yy))
            yy += 23


def draw_right_panel(screen, fonts, city, monthly_note, char_a, line_a, char_b, line_b, log):
    x = config.WINDOW_WIDTH - config.RIGHT_PANEL_WIDTH
    panel = pygame.Rect(x, config.HEADER_HEIGHT, config.RIGHT_PANEL_WIDTH, config.WINDOW_HEIGHT - config.HEADER_HEIGHT - config.FOOTER_HEIGHT)
    pygame.draw.rect(screen, config.COLOR_PANEL, panel)
    pygame.draw.line(screen, config.COLOR_BORDER, panel.topleft, panel.bottomleft, 2)

    px = x + 18
    y = panel.y + 16
    header = fonts["header"].render("MUNICIPAL FEED", True, config.COLOR_ACCENT)
    screen.blit(header, (px, y))
    y += 34

    for name, line in ((char_a, line_a), (char_b, line_b)):
        n = fonts["small_bold"].render(name, True, config.COLOR_TEXT)
        screen.blit(n, (px, y))
        y += 20
        for wrapped in wrap_text(line, fonts["small"], panel.width - 36):
            screen.blit(fonts["small"].render(wrapped, True, config.COLOR_TEXT_DIM), (px, y))
            y += 18
        y += 8

    pygame.draw.line(screen, config.COLOR_BORDER, (px, y), (panel.right - 18, y), 1)
    y += 10
    for wrapped in wrap_text(monthly_note, fonts["small"], panel.width - 36):
        screen.blit(fonts["small"].render(wrapped, True, config.COLOR_TEXT), (px, y))
        y += 18

    y += 10
    header = fonts["small_bold"].render("EVENT LOG", True, config.COLOR_ACCENT)
    screen.blit(header, (px, y))
    y += 22
    for item in log[:7]:
        for wrapped in wrap_text("- " + item, fonts["small"], panel.width - 36):
            screen.blit(fonts["small"].render(wrapped, True, config.COLOR_TEXT_DIM), (px, y))
            y += 17
        y += 2


def draw_footer(screen, fonts, text):
    y = config.WINDOW_HEIGHT - config.FOOTER_HEIGHT
    pygame.draw.rect(screen, config.COLOR_TITLE_BG, (0, y, config.WINDOW_WIDTH, config.FOOTER_HEIGHT))
    pygame.draw.line(screen, config.COLOR_BORDER, (0, y), (config.WINDOW_WIDTH, y), 1)
    surf = fonts["small"].render(text, True, config.COLOR_TEXT_DIM)
    screen.blit(surf, (20, y + 12))


def draw_report(screen, fonts, city, ending, conclusion):
    screen.fill(config.COLOR_BG)
    title = fonts["title"].render("BLOON MUNICIPAL PERFORMANCE REPORT", True, config.COLOR_ACCENT)
    screen.blit(title, (config.WINDOW_WIDTH // 2 - title.get_width() // 2, 90))
    ending_surf = fonts["header"].render(ending, True, config.COLOR_TEXT)
    screen.blit(ending_surf, (config.WINDOW_WIDTH // 2 - ending_surf.get_width() // 2, 145))

    y = 205
    lines = [
        "Budget: Rp " + str(city.budget) + " B",
        "Infrastructure: " + str(city.infrastructure),
        "Public Satisfaction: " + str(city.satisfaction),
        "Traffic: " + str(city.traffic),
        "Flood Risk: " + str(city.flood_risk),
        "Bureaucracy: " + str(city.bureaucracy),
        "Projects Completed: " + str(city.projects_completed),
        "Meetings: " + str(city.meetings),
        "Documents Lost: " + str(city.documents_lost),
    ]
    for item in lines:
        surf = fonts["body"].render(item, True, config.COLOR_TEXT)
        screen.blit(surf, (config.WINDOW_WIDTH // 2 - 240, y))
        y += 30

    y += 14
    for line in wrap_text(conclusion, fonts["body"], 700):
        surf = fonts["body"].render(line, True, config.COLOR_TEXT_DIM)
        screen.blit(surf, (config.WINDOW_WIDTH // 2 - 350, y))
        y += 24

    hint = fonts["small"].render("Press R to restart or ESC to resign from public service.", True, config.COLOR_ACCENT)
    screen.blit(hint, (config.WINDOW_WIDTH // 2 - hint.get_width() // 2, y + 32))
