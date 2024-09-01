import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(angle) * -1
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = v1 * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2.velocity = v2 * 1.2
