import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Uma classe que administra projeteis disparandos pela espaçonave'''

    def __init__(self, ai_settings, screen, ship) -> None:
        super(Bullet, self).__init__()
        self.screen = screen
        # Cria um retângulo para o projétil em (0, 0) e, em seguida define a posição correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)