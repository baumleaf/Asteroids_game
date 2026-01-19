import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    containers: tuple = ()

    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            pygame.math.Vector2.rotate(self.velocity,random_angle)
            pygame.math.Vector2.rotate(self.velocity,-random_angle)
            self.radius -= ASTEROID_MIN_RADIUS 
            self.draw(screen)
