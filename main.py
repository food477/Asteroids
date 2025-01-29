# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import *
from shot import Shot

shots = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

AsteroidField.containers = (updatable)
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
Shot.containers = (shots, updatable, drawable)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)      
        screen.fill((0,0,0))

        for asteroid in asteroids:
            col = asteroid.col_check(player)
            if col == True:
                print("Game over!")
                sys.exit()


        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()