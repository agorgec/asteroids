import pygame

from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen, color="white", center=self.position, radius=self.radius
        )

    def update(self, dt):
        self.position += self.velocity * dt
