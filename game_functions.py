import sys
import pygame

def check_keydown_events(event, ship):
    '''Response a pressionamento de tecla'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    '''Responde ao soltar de teclas'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ship):
    '''Responde a eventos de pressionamento de teclado e mouse'''
    '''Respond keyboards ans mice press events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            

def update_screen(ai_settings, screen, ship):
    '''Atualiza as imagens na tela e altera para a nova tela'''
    '''Updates the images on the screen and switches to the new screen'''
    # Redesenha a tela a cada passagem de laço
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()