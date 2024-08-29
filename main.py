# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()

    while True:
        dt = clock.tick(60) / 1000
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # player.update(dt)
        for updatable in updatables:
            updatable.update(dt)
        # player.draw(screen)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
