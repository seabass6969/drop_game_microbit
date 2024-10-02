import random
import pygame
import os

DUCK = [
    pygame.image.load(os.path.join("assets/", "duck_a.png")),
    pygame.image.load(os.path.join("assets/", "duck_b.png")),
    # pygame.image.load(os.path.join("assets/", "duck_c.jpg")),
]


class Items:
    def __init__(self, screen: pygame.Surface, microbit_x, microbit_y):
        self.screen = screen
        self.microbit_x = microbit_x
        self.microbit_y = microbit_y
        self.own_velocity = random.randint(1, 3)
        self.image = random.choice(DUCK)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = random.randint(0, 500)
        self.y = 120
        self.duck_mask = pygame.mask.from_surface(self.image)
        self.difficulty = 0

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
        # pygame.draw.rect(self.screen, "blue", (self.x, self.y, 30, 30))

    def update(self, difficulty):
        self.y += self.own_velocity
        if self.y > 800:
            self.reset()
        self.difficulty = difficulty

    def reset(self):
        self.y = 120
        self.own_velocity = random.randint(1 + self.difficulty, 3 + self.difficulty)

        self.image = random.choice(DUCK)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.duck_mask = pygame.mask.from_surface(self.image)