import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y, radius)
        self.velocity = 0
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            velocity1 = self.velocity.rotate(angle) * 1.2
            velocity2 = self.velocity.rotate(-angle) * 1.2
            radius_new = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position[0],self.position[1], radius_new)
            asteroid2 = Asteroid(self.position[0],self.position[1], radius_new)
            asteroid1.velocity = velocity1
            asteroid2.velocity = velocity2


    def update(self, dt):
        self.position += self.velocity * dt

