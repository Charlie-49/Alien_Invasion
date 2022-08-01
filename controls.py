import pygame, sys
from bullet import Bullet
from nlo import Nlo
import time


def events(screen, gun, bullets):
    """обробка подій"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # кнопка вправо
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, nlos, bullets):
    """обновлення екрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    nlos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, nlos, bullets):
    """обновляє позиції пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, nlos, True, True)
    if collisions:
        for nlos in collisions.values():
            stats.score += 1 * len(nlos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(nlos) == 0:
        bullets.empty()
        create_army(screen, nlos)

def gun_kill(stats, screen, sc, gun, nlos, bullets):
    """зіткнення коробля і армії"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        nlos.empty()
        bullets.empty()
        create_army(screen, nlos)
        gun.greate_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_nlos(stats, screen, sc, gun, nlos, bullets):
    """обновляє позицію нло"""
    nlos.update()
    if pygame.sprite.spritecollideany(gun, nlos):
        gun_kill(stats, screen, sc, gun, nlos, bullets)
    nlos_check(stats, screen, sc, gun, nlos, bullets)

def nlos_check(stats, screen, sc, gun, nlos, bullets):
    """чи добрались нло до кінця екрана"""
    screen_rect = screen.get_rect()
    for nlo in nlos.sprites():
        if nlo.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, nlos, bullets)
            break

def create_army(screen, nlos):
    nlo = Nlo(screen)
    nlo_width = nlo.rect.width
    number_nlo_x = int((700 - 2 * nlo_width) / nlo_width)
    nlo_height = nlo.rect.height
    number_nlo_y = int((600 - 100 - 2 * nlo_height) / nlo_height)

    for row_number in range(number_nlo_y -8):
        for nlo_number in range(number_nlo_x):
            nlo = Nlo(screen)
            nlo.x = nlo_width + (nlo_width * nlo_number)
            nlo.y = nlo_height + (nlo_height * row_number)
            nlo.rect.x = nlo.x
            nlo.rect.y = nlo.rect.height + (nlo.rect.height * row_number)
            nlos.add(nlo)

def check_high_score(stats, sc):
    """провірка нових рекордів"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))