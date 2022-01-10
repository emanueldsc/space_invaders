class Settings():
    '''Uma classe para armazenar todas as configurações da invasão Alienigena.'''
    '''A class to store the all configurations of Aliens Invasion'''
    
    def __init__(self) -> None:
        '''inicializa as configuraçõess do jogo'''
        '''Initialize the game configurations'''
        # Configurações de tela
        # Screen configurations
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # Configuração do projeteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
