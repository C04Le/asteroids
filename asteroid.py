import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):   
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # time until asteroid can be destroyed after spawn, decreases each update
        # helps avoid having large asteroids anihilated by just 1 bullet
        self.timer = 0.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        self.timer -= dt

    def split(self, dt):
        if self.timer >= 0:
            return
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity1, velocity2 = self.velocity.rotate(random_angle), self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        new_asteroid1.velocity, new_asteroid2.velocity = velocity1 * 1.2, velocity2 * 1.2
