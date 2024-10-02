import random
import pygame

WIDTH = 500
HEIGHT = 800


class Navbar:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.score = 0
        self.timer = ""
        self.FONT = pygame.font.SysFont("Comic Sans MS", 20)
        self.TEXT = self.FONT.render(str(self.score), False, "black")
        self.TEXT_timer = self.FONT.render(self.timer, False, "black")

    def draw(self):
        pygame.draw.rect(
            self.screen,
            (217, 217, 217),
            (0, 0, 500, 100),
            border_bottom_left_radius=20,
            border_bottom_right_radius=20,
        )
        self.screen.blit(self.TEXT, (WIDTH / 2 - self.TEXT.get_width() / 2, 5))
        self.screen.blit(
            self.TEXT_timer,
            (WIDTH / 2 - self.TEXT_timer.get_width() / 2, 10 + self.TEXT.get_height()),
        )

    def update(self, score, timer):
        self.score = score
        self.TEXT = self.FONT.render(str(self.score), False, "black")
        self.timer = timer
        self.TEXT_timer = self.FONT.render(self.timer, False, "black")
