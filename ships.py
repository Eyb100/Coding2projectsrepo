import pygame
import numpy as np
import math
import utils

class Ship:
    def __init__(self, x, y, surface):
        # Position of the tip of the ship
        self.pos = np.array([x, y])
        # Rotation angle of the ship relative to the tip of the ship
        self.angle = 0.0
        # Additional properties goes here:


        # Leave the rest of these properties
        self.surface = surface
        self.radius = 20
        self.color = (0, 0, 0)
        self.collided = False
        self.velocity = (0,0)

    # Update properties of the ship
    def update(self, mouse_pos, asteroids, game_status):
    # Set target position based on mouse position
        target_pos = np.array(mouse_pos)

        # Calculate direction to the target
        direction = target_pos - self.pos
        distance = math.dist(self.pos, target_pos)
        # Calculate the velocity based on the distance
        max_speed = 5.0
        desired_speed = max_speed * (distance / 100)
        desired_velocity = desired_speed * direction / distance if distance > 0 else np.array([0, 0])
        # Calculate acceleration to adjust the velocity
        acceleration = (desired_velocity - self.velocity) * 0.1
        # Update velocity and position
        self.velocity += acceleration
        self.pos += self.velocity

        # Determine rotation angle of ship to point behind the cursor
        self.angle = math.atan2(-self.velocity[1], -self.velocity[0])

        # Leave the rest of the code
        # Check for collision
        if game_status == "started":
            self.collision(asteroids, game_status)

    # Draw the ship onto the canvas
    def draw(self):
        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    # Detect whether ship has collided with an asteroid
    def collision(self, asteroids, game_status):
        for asteroid in asteroids:
            if math.dist(asteroid.pos, self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 0, 0)
                self.collided = True
                break





