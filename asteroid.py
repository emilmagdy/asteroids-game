import random
import pygame
from circleshape import CircleShape
from constants import *
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            
            ran_angle = random.uniform(20, 50)
            new_radius = self.radius / 2
            new_vector1 = pygame.Vector2(0, 1).rotate(ran_angle) * self.radius
            new_vector2 = pygame.Vector2(0, 1).rotate(-ran_angle) * self.radius
            
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = new_vector1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = new_vector2
            return [new_asteroid1, new_asteroid2]
        return []