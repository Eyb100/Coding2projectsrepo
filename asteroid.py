import numpy as np
import math
import pygame
import random

class Asteroid:
    def __init__(self, x, y, radius, surface):
        #changed
        # Position of the tip of the asteroid
        self.pos = np.array([x, y])
        # Additional properties goes here:
        self.angle = random.random() * 2 * math.pi
        self.speed = random.random() * 4 + 1

        # Leave the rest of these properties
        self.surface = surface
        self.radius = radius

    def update(self, asteroids,game_status):
            # Action required!
        if game_status != "started":
            return
         #changed
        # Calculate the change in x and y coordinates based on the angle and speed
        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)
        # Update the position of the asteroid
        self.pos[0] += dx
        self.pos[1] += dy

        # Wrap asteroid around the edges so it always stays on screen
        if self.pos[0] > self.surface.get_width():
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = self.surface.get_width()

        if self.pos[1] > self.surface.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = self.surface.get_height()

 # Draw the asteroid onto the canvas
#changed
    def draw(self):
        pygame.draw.circle(self.surface, (0, 0, 255), (int(self.pos[0]), int(self.pos[1])), self.radius)
