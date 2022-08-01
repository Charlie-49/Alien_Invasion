import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """створюємо пулю в позиції корабля"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)
        self.color = 84, 135, 255
        self.speed = 8.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """переміщення пулі в верх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """малюємо пулю на екрані"""
        pygame.draw.rect(self.screen, self.color, self.rect)
