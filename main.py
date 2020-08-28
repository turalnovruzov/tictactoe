import pygame
import os

# Initialize pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 900, 600

# Window caption
pygame.display.set_caption('TicTacToe')

# Set the screen
screen = pygame.display.set_mode(SIZE)

# Fonts
MEDIUM_FONT = pygame.font.Font(os.path.join('fonts', 'OpenSans-Regular.ttf'), 40)
LARGE_FONT = pygame.font.Font(os.path.join('fonts', 'OpenSans-Regular.ttf'), 60)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# States
MENU_STATE = 'Menu'
PLAY_STATE = 'Play'

gamestate = MENU_STATE

# Player
ai_turn = None

# Game loop
while True:

    # Check for events
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()

    if gamestate == MENU_STATE:

        # Background color
        screen.fill(BLACK)

        # Title
        title = LARGE_FONT.render('Play Tic-Tac-Toe', True, WHITE)
        title_rect = title.get_rect()
        title_rect.center = (WIDTH / 2, 100)
        screen.blit(title, title_rect)
        
        # Play as X button
        playX = MEDIUM_FONT.render('Play as X', True, BLACK)
        playXRect = playX.get_rect()
        playXButton = pygame.Rect(WIDTH / 2 - (WIDTH / 4) / 2, HEIGHT / 2 - (playXRect.height + 30), WIDTH / 4, playXRect.height + 20)
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, WHITE, playXButton)
        screen.blit(playX, playXRect)

        # Play as O button
        playO = MEDIUM_FONT.render('Play as O', True, BLACK)
        playORect = playO.get_rect()
        playOButton = pygame.Rect(WIDTH / 2 - (WIDTH / 4) / 2, HEIGHT / 2 + 30, WIDTH / 4, playORect.height + 20)
        playORect.center = playOButton.center
        pygame.draw.rect(screen, WHITE, playOButton)
        screen.blit(playO, playORect)

        # Mouse click
        if pygame.mouse.get_pressed()[0]:
            print('a')
            point = pygame.mouse.get_pos()

            # Play as X or O
            if playXButton.collidepoint(point):
                ai_turn = False
                gamestate = PLAY_STATE
            elif playOButton.collidepoint(point):
                ai_turn = True
                gamestate = PLAY_STATE

    pygame.display.flip()
