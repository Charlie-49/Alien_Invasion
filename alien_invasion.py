import controls
import pygame
from pygame.sprite import Group
from stats import Stats
from gun import Gun
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 600))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    nlos = Group()
    controls.create_army(screen, nlos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen,gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, nlos, bullets)
            controls.update_bullets(screen, stats, sc, nlos, bullets)
            controls.update_nlos(stats, screen, sc, gun, nlos, bullets)


run()
