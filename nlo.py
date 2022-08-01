import pygame


class Nlo(pygame.sprite.Sprite):
    """клас одного прибульця"""

    def __init__(self, screen):
        """ініціалізуємо і задаємо позицію"""
        super(Nlo, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/nlo.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вивід нло на екран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """переміщає нло"""
        self.y += 0.1
        self.rect.y = self.y

