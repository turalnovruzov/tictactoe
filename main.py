import pygame
import os
import time
from tictactoe import Tictactoe

X = 'X'
O = 'O'

# Initialize pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600

# Window caption
pygame.display.set_caption('TicTacToe')

# Set the screen
screen = pygame.display.set_mode(SIZE)

# Fonts
M_FONT = pygame.font.Font(os.path.join('fonts', 'OpenSans-Regular.ttf'), 40)
L_FONT = pygame.font.Font(os.path.join('fonts', 'OpenSans-Regular.ttf'), 60)
XL_FONT = pygame.font.Font(os.path.join('fonts', 'OpenSans-Regular.ttf'), 72)

# Cell properties
cell_width = 120
cell_pos = (WIDTH / 2 - cell_width * 1.5, HEIGHT / 2 - cell_width * 1.5)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# States
MENU_STATE = 'Menu'
PLAY_STATE = 'Play'

gamestate = MENU_STATE

# Player
ai_turn = None

# tictactoe
ttt = None

# Focused cell
focus = None

# Game loop
while True:

    # Background color
    screen.fill(BLACK)

    if gamestate == MENU_STATE:

        # Title
        title = L_FONT.render('Play Tic-Tac-Toe', True, WHITE)
        title_rect = title.get_rect()
        title_rect.center = (WIDTH / 2, 100)
        screen.blit(title, title_rect)
        
        # Play as X button
        playX = M_FONT.render('Play as X', True, BLACK)
        playXRect = playX.get_rect()
        playXButton = pygame.Rect(WIDTH / 2 - (230) / 2, HEIGHT / 2 - (playXRect.height + 30), 230, playXRect.height + 20)
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, WHITE, playXButton)
        screen.blit(playX, playXRect)

        # Play as O button
        playO = M_FONT.render('Play as O', True, BLACK)
        playORect = playO.get_rect()
        playOButton = pygame.Rect(WIDTH / 2 - (230) / 2, HEIGHT / 2 + 30, 230, playORect.height + 20)
        playORect.center = playOButton.center
        pygame.draw.rect(screen, WHITE, playOButton)
        screen.blit(playO, playORect)
    
    elif gamestate == PLAY_STATE:

        # Draw cells
        cells = []
        for i in range(3):
            row = []

            for j in range(3):
                rect = pygame.Rect(cell_pos[0] + j * cell_width, cell_pos[1] + i * cell_width, cell_width, cell_width)
                pygame.draw.rect(screen, WHITE, rect, 3)
                row.append(rect)
            
            cells.append(row)
        
        # Draw cell values
        board = ttt.get_board()

        for i in range(3):
            for j in range(3):
                if board[i][j]:
                    cell_value = XL_FONT.render(board[i][j], True, WHITE)
                    cell_value_rect = cell_value.get_rect()
                    cell_value_rect.center = cells[i][j].center
                    screen.blit(cell_value, cell_value_rect)
        
        print(focus)

    pygame.display.flip()


    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Menu State
        if gamestate == MENU_STATE:

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                point = event.pos
                b_ = False

                # Play as X or O
                if playXButton.collidepoint(point):
                    ai_turn = False
                    b_ = True
                elif playOButton.collidepoint(point):
                    ai_turn = True
                    b_ = True
                
                # Start Play state
                if b_:
                    gamestate = PLAY_STATE
                    ttt = Tictactoe()
                    time.sleep(0.1)
        # Play state
        elif gamestate == PLAY_STATE:

            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                point = event.pos

                # Cells
                b_ = True
                for i in range(3):
                    for j in range(3):
                        if cells[i][j].collidepoint(point):
                            focus = (i, j)
                            b_ = False
                            break
                
                if b_:
                    focus = None
