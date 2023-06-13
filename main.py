import sys
import pygame
from pygame.locals import *
from random import random
from ships import Ship
from asteroid import Asteroid
import numpy as np

# SETUP
# Initialize program
pygame.init()

# Assign FPS a value
FPS = 30
FramePerSec = pygame.time.Clock()

# Setup canvas size
WIDTH = 600
HEIGHT = 600

# Keep track of game status
game_status = "init"

# Setup a 600x600 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Evasion")

# Create game objects
ship = Ship(x=WIDTH / 2, y=HEIGHT / 2, surface=DISPLAYSURF)
asteroids = [
    Asteroid(
        x=random() * WIDTH,
        y=1,
        radius=20,
        surface=DISPLAYSURF
    )
    for _ in range(0, 10)
]

# Create font to draw text with
font = pygame.font.SysFont("Verdana", 60)


# SETUP END

# EVENTS
def handle_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    global game_status
    mouse_pressed, _, _ = pygame.mouse.get_pressed()
    if mouse_pressed:
        game_status = "started"

