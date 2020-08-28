import pygame

# Initialize pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 900, 600

# Window caption
pygame.display.set_caption('TicTacToe')

# Set the screen
WINDOW = pygame.display.set_mode(SIZE)

MENU_STATE = 'Menu'
PLAY_STATE = 'Play'

gamestate = MENU_STATE

# Game loop
while True:

    # Check for events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    
