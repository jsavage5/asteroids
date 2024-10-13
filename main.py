import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import *
from asteroids import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    updatable.add(player)
    drawable.add(player)

    asteroids_group = pygame.sprite.Group()
    Asteroid.containers = (asteroids_group, updatable, drawable)
    updatable.add(asteroids_group)
    drawable.add(asteroids_group)


    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()
    updatable.add(asteroidfield)

    shots_group = pygame.sprite.Group()
    Shot.containers = (shots_group, updatable, drawable)
    updatable.add(shots_group)
    drawable.add(shots_group)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids_group:
            if player.collide(asteroid):
                print("Game Over!")
                pygame.time.wait(3000)
                running = False

        for asteroid in asteroids_group:
            for shot in shots_group:
                if asteroid.collide(shot):
                    asteroid.split()
                    asteroid.kill()
                    shot.kill()

        pygame.display.flip()

        dt = clock.tick(60) / 1000



    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
  main()
