import pygame
from kaspersmicrobit import KaspersMicrobit
from items import Items
from block import Block
from navbar import Navbar
import math
import time


pygame.init()
screen = pygame.display.set_mode((500, 800))
clock = pygame.time.Clock()
running = True

x = 0
y = 0

score = 0
difficulty = 0
gametick = 0
GAME_LENGTH = 30 # seconds


def score_update(number: int):
    global score
    score += number


def accelerometer_data(data):
    global x
    global y

    x = min(max(0, data.x / 2), 500 - 40)
    y = min(max(0, data.y / 2), 800)


start = False


def pressed(_):
    global start
    start = True
    print("Pressed A")


screen.fill("white")
pygame.display.flip()
FONT = pygame.font.SysFont("Comic Sans MS", 50)
SMALL_FONT = pygame.font.SysFont("Comic Sans MS", 20)
with KaspersMicrobit.find_one_microbit() as microbit:
    microbit.accelerometer.notify(accelerometer_data)
    microbit.buttons.on_button_a(press=pressed)
    while not start:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        Instruction = FONT.render("Press A to start", False, "black")
        screen.blit(
            Instruction,
            (
                screen.get_width() / 2 - Instruction.get_width() / 2,
                screen.get_height() / 2 - Instruction.get_height() / 2,
            ),
        )
        pygame.display.flip()
        clock.tick(120)

    ItemList = []
    block = Block(screen, x, y, score_update)
    navbar = Navbar(screen)
    for _ in range(10):
        ItemList.append(Items(screen, x, y))
    for i in range(5, 0, -1):

        screen.fill("white")
        countdown = FONT.render(str(i), False, "black")
        screen.blit(
            countdown,
            (
                screen.get_width() / 2 - countdown.get_width() / 2,
                screen.get_height() / 2 - countdown.get_height() / 2,
            ),
        )
        time.sleep(1)
        pygame.display.flip()
        # clock.tick(120)

    end_time = time.time() + GAME_LENGTH

    while running:
        time_left = end_time - time.time()
        if time_left <= 0:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        for item in ItemList:
            item.draw()
            item.update(difficulty)
        block.draw()
        block.update(x, y, ItemList)

        navbar.draw()
        navbar.update(score, "00:{}".format(str(math.floor(time_left))))

        pygame.display.flip()

        clock.tick(120)
        gametick += 1
        if gametick % 500 == 0:
            difficulty += 1


    restart_loop = True
    while restart_loop:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        score_end = SMALL_FONT.render("Game Over. You got {} points!".format(score), False, "black")
        screen.blit(
            score_end,
            (
                screen.get_width() / 2 - score_end.get_width() / 2,
                screen.get_height() / 2 - score_end.get_height() / 2,
            ),
        )
        pygame.display.flip()
        clock.tick(120)