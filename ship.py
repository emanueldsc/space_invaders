import pygame

class Ship():
    def __init__(self, ai_settings, screen) -> None:
        '''Inicializa a espaçonave e define sua posição inicial'''
        '''Initialize the spaceship and set to initial position'''
        self.screen = screen
        self.ai_settings = ai_settings
        # Carrega a imagem da espaçonave e obtem seu rect
        # Load the spaceship image and get it's rect
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        # Flags de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''Atualiza a posição da espaçonave de acordo com  a flag de movimentação'''
        '''Atualiza o valor do centro da espaçonave, e não o retangulo'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center


    def blitme(self):
        '''Desenha a espaçonave em sua posição atual'''
        self.screen.blit(self.image, self.rect)