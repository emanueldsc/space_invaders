import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicia o jogo e cria um objeto para a tela
    # Start the game and create an object for the screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Space Invaders')
    # Define cor de fundo
    # Set background color
    ship = Ship(ai_settings, screen)
    bg_color = (230, 230, 230)
    # Cria a espaçonave

    # Inicia o laço principal do jogo
    # Start inicial game loop
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
            
run_game()