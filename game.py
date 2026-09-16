"""
game.py - Pygame game state machine for SIMCITY: JAKARTA BLOON EDITION.
"""

import pygame

import config
import ui
from budget import run_monthly_finance
from city import City
from commentary import get_commentary, get_monthly_summary
from characters import get_character_line
from decisions import apply_decision
from events import generate_event
from projects import get_projects


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption(config.TITLE)
        self.clock = pygame.time.Clock()
        self.fonts = ui.make_fonts()
        self.running = True
        self.reset()

    def reset(self):
        self.city = City()
        self.projects = get_projects()
        self.used_events = set()
        self.phase = "decision"
        self.current_event = None
        self.result_text = ""
        self.followup_text = ""
        self.commentary = ""
        self.monthly_note = ""
        self.buttons = []
        self.char_a, self.line_a = get_character_line()
        self.char_b, self.line_b = get_character_line()
        self.ending = ""
        self.conclusion = ""
        self.start_month()

    def start_month(self):
        city = self.city
        revenue, cost = run_monthly_finance(city)
        progress_gain = 3 if city.budget > 200 else 1
        city.apply({
            "infrastructure": -config.INFRA_DECAY_PER_MONTH,
            "project_progress": progress_gain,
            "traffic": 2,
            "flood_risk": 1,
        })
        self.monthly_note = get_monthly_summary(city, revenue, cost)
        self.current_event = generate_event(self.used_events)
        self.commentary = get_commentary(city)
        self.char_a, self.line_a = get_character_line()
        self.char_b, self.line_b = get_character_line()
        self.result_text = ""
        self.followup_text = ""
        self.phase = "decision"
        self.build_decision_buttons()

    def center_button_area(self):
        area_x = config.LEFT_PANEL_WIDTH + 20
        area_w = (config.WINDOW_WIDTH - config.RIGHT_PANEL_WIDTH
                  - config.LEFT_PANEL_WIDTH - 40)
        by = (config.WINDOW_HEIGHT - config.FOOTER_HEIGHT
              - config.BUTTON_HEIGHT - 24)
        return area_x, area_w, by

    def build_decision_buttons(self):
        self.buttons = []
        opts = self.current_event.options
        n = len(opts)
        area_x, area_w, by = self.center_button_area()
        bw = (area_w - (n - 1) * config.BUTTON_MARGIN) // n
        for i, opt in enumerate(opts):
            rect = (
                area_x + i * (bw + config.BUTTON_MARGIN),
                by,
                bw,
                config.BUTTON_HEIGHT,
            )
            self.buttons.append(ui.Button(rect, opt.label, opt.cost_text))

    def choose(self, index):
        opt = self.current_event.options[index]
        result, followup = apply_decision(self.city, opt)
        self.result_text = result
        self.followup_text = followup

        if result.startswith("INSUFFICIENT BUDGET"):
            self.commentary = (
                "The finance department would like a word. "
                "The word is 'no'."
            )
            return

        if self.city.project_progress >= 100:
            self.city.project_progress = 0
            self.city.projects_completed += 1
            self.city.add_log(
                "M" + str(self.city.month)
                + ": PROJECT COMPLETED. A ribbon is cut. The ribbon was delayed."
            )

        log_label = opt.label
        if len(log_label) > 28:
            log_label = log_label[:28] + "..."
        self.city.add_log(
            "M" + str(self.city.month) + ": "
            + self.current_event.title + " -> " + log_label
        )
        self.commentary = get_commentary(self.city)
        self.phase = "result"
        self.build_continue_button()

    def build_continue_button(self):
        area_x, area_w, by = self.center_button_area()
        if self.city.month >= config.TOTAL_MONTHS:
            label = "SUBMIT FINAL REPORT"
        else:
            label = "PROCEED TO MONTH " + str(self.city.month + 1)
        self.buttons = [
            ui.Button(
                (area_x, by, area_w, config.BUTTON_HEIGHT),
                label,
                "Time, like procurement, moves in one direction.",
            )
        ]

    def advance(self):
        if self.city.month >= config.TOTAL_MONTHS:
            self.finish_game()
        else:
            self.city.month += 1
            self.start_month()

    def finish_game(self):
        c = self.city
        score = (
            c.infrastructure
            + c.satisfaction
            + min(100, c.budget // 10)
            - c.traffic * 0.5
            - c.flood_risk * 0.5
        )

        if c.bureaucracy > 150:
            self.ending = "BUREAUCRATIC SINGULARITY"
            self.conclusion = (
                "Paperwork has collapsed inward. Forms now approve other forms. "
                "No one is in charge. Everyone has a stamp."
            )
        elif c.budget > 800 and score > 120:
            self.ending = "LEGENDARY ADMINISTRATION"
            self.conclusion = (
                "The city has money AND functioning roads. An investigation has "
                "been opened into how this happened."
            )
        elif score > 60:
            self.ending = "FUNCTIONAL"
            self.conclusion = "Technically speaking, the city still exists."
        elif score > 0:
            self.ending = "BARELY FUNCTIONAL"
            self.conclusion = (
                "The city runs on momentum, duct tape, and one overworked pump."
            )
        elif c.infrastructure < 25 or c.flood_risk > 90:
            self.ending = "PLEASE CALL AN ENGINEER"
            self.conclusion = (
                "An engineer has been called. The engineer has also called an engineer."
            )
        else:
            self.ending = "THE CITY HAS BECOME A SPREADSHEET"
            self.conclusion = (
                "All services are now delivered via Excel. Cell C47 is responsible "
                "for drainage."
            )

        self.phase = "report"
        self.buttons = []

    def handle_keydown(self, key):
        if key == pygame.K_ESCAPE:
            self.running = False
        elif self.phase == "report" and key == pygame.K_r:
            self.reset()
        elif self.phase == "result" and key in (pygame.K_RETURN, pygame.K_SPACE):
            self.advance()
        elif self.phase == "decision" and key in (
            pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4
        ):
            idx = key - pygame.K_1
            if idx < len(self.current_event.options):
                self.choose(idx)

    def handle_click(self, mouse_pos):
        for i, btn in enumerate(self.buttons):
            if btn.rect.collidepoint(mouse_pos):
                if self.phase == "decision":
                    self.choose(i)
                elif self.phase == "result":
                    self.advance()
                break

    def draw(self, mouse_pos):
        self.screen.fill(config.COLOR_BG)
        ui.draw_header(self.screen, self.fonts, self.city.month)

        if self.phase == "report":
            ui.draw_report(
                self.screen,
                self.fonts,
                self.city,
                self.ending,
                self.conclusion,
            )
        else:
            ui.draw_left_panel(self.screen, self.fonts, self.city)
            ui.draw_center_panel(
                self.screen,
                self.fonts,
                self.current_event,
                self.phase,
                self.result_text,
                self.followup_text,
                self.commentary,
            )
            ui.draw_right_panel(
                self.screen,
                self.fonts,
                self.city,
                self.monthly_note,
                self.char_a,
                self.line_a,
                self.char_b,
                self.line_b,
                self.city.log,
            )
            for btn in self.buttons:
                btn.draw(
                    self.screen,
                    self.fonts["small_bold"],
                    self.fonts["small"],
                    mouse_pos,
                )

            if self.phase == "decision":
                footer = (
                    "Keys 1-4: choose response | ESC: resign from public service"
                )
            else:
                footer = (
                    "ENTER/SPACE or click: continue | ESC: resign from public service"
                )
            ui.draw_footer(self.screen, self.fonts, footer)

        pygame.display.flip()

    def run(self):
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(mouse_pos)

            self.draw(mouse_pos)
            self.clock.tick(config.FPS)

        pygame.quit()
