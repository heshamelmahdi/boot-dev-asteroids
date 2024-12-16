import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", center=self.position, radius=self.radius, width=2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        split_angle = random.uniform(20, 50)
        first_split_vector = self.velocity.rotate(split_angle)
        second_split_vector = self.velocity.rotate(-split_angle)

        split_radius = self.radius - ASTEROID_MIN_RADIUS

        first_roid = Asteroid(self.position.x, self.position.y, split_radius)
        second_roid = Asteroid(self.position.x, self.position.y, split_radius)

        first_roid.velocity = first_split_vector * 1.2
        second_roid.velocity = second_split_vector * 1.2
