import random
import pygame
from items import Items


class Block:
    def __init__(self, screen: pygame.Surface, microbit_x, microbit_y, score_update):
        self.screen = screen
        self.microbit_x = microbit_x
        self.microbit_y = microbit_y
        self.x = 0
        self.y = 600
        self.score_update = score_update
        self.self_surface = pygame.surface.Surface((40, 10))
        pygame.draw.rect(self.self_surface, "blue", (self.x, self.y, 40, 10))
        self.self_mask = pygame.mask.from_surface(self.self_surface)

    def draw(self):
        self.screen.blit(self.self_surface, (self.x, self.y))

    def update(self, microbit_x, microbit_y, Items: [Items]):
        self.self_mask = pygame.mask.from_surface(self.self_surface)
        self.microbit_x = microbit_x
        self.microbit_y = microbit_y
        # self.y = self.microbit_y
        self.x = self.microbit_x

        for item in Items:
            if item.duck_mask.overlap(
                self.self_mask, (self.x - item.x, self.y - item.y)
            ):
                self.score_update(1)
                item.reset()
