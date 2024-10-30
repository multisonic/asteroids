import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt


 