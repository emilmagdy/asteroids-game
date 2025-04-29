import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfeild import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock() 
    dt = 0
    player1= Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = updatables, drawables
    Shot.containers = updatables, drawables
    Asteroid.containers = updatables, drawables, asteroids
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()
    
    player1 =Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
    updatables.add(player1)
    updatables.add(asteroid_field)
    
    while True:
        dt = pygame.time.Clock().tick(60)  / 1000

        screen.fill((0, 0, 0))
        updatables.update(dt)
        for asteroid in asteroids:
            for shot in drawables:
                if isinstance(shot, Shot):
                    if shot.collide(asteroid):
                        
                        shot.kill()
                        new_asteroids = asteroid.split()
                        asteroids.add(*new_asteroids)
        
            if player1.collide(asteroid):
                print("Collision detected!")
                pygame.quit()
                return
        for drawable in drawables:
            if isinstance(drawable, Asteroid):
                drawable.draw(screen)
            elif isinstance(drawable, Shot):
                drawable.draw(screen)
            elif isinstance(drawable, Player):
                drawable.draw(screen)
        
        pygame.display.flip()
        
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return


if __name__ == "__main__":
    main()