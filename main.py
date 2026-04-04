import math
import pygame
from Games.game2048 import Game

pygame.init()

### Constants ###
SIZE = 4
TILE_SIZE = 100
SCREEN_SIZE = SIZE * TILE_SIZE
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("MY OWN 2048")

thisgame = Game()

COLORS = {
    0: (200, 200, 200),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
}




def get_font_size(value):
    if value == 0:
        return 0
    base_size = 50
    scale = math.log2(value)
    size = base_size - scale * 4
    return max(18 , int(size))

def get_font(value):
    size = get_font_size(value)
    return pygame.font.SysFont("Arial", size)


def draw():
    #print(thisgame.board)
    screen.fill((187, 173, 160))
    for r in range(SIZE):
        for c in range(SIZE):
            value = thisgame.board[r][c]
            color = COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect( c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            if value != 0: 
                font = get_font(value)
                text = font.render(str(value), True, (0, 0, 0))
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)

def draw_game_over(screen, game):
    width, height = screen.get_size()

    overlay = pygame.Surface((width, height))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))

    #TEXT
    font = pygame.font.SysFont("Arial", 48)
    text = font.render("Game Over!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2 - 50))
    screen.blit(text, text_rect)

    #SCORE
    font_small = pygame.font.SysFont("Arial", 32)
    score_text = font_small.render(f"My Score: {game.score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width // 2, height // 2 + 10))
    screen.blit(score_text, score_rect)

    #BUTTON
    button_rect = pygame.Rect(width // 2 - 100, height // 2 + 60, 200, 50)
    pygame.draw.rect(screen, (200, 200, 200), button_rect)
    button_text = font_small.render("Play Again", True, (0, 0, 0))
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)

    return button_rect



### LOOOOOOOOOP ###
running = True
button_rect = None
while running:
    draw()
    if thisgame.is_game_over():
        button_rect = draw_game_over(screen, thisgame)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
                if not thisgame.is_game_over(): 
                    if event.key == pygame.K_LEFT:
                        thisgame.move_left()
                    if event.key == pygame.K_RIGHT:
                        thisgame.move_right()
                    if event.key == pygame.K_UP:
                        thisgame.move_up()
                    if event.key == pygame.K_DOWN:
                        thisgame.move_down()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if thisgame.is_game_over() and button_rect and button_rect.collidepoint(event.pos):
                thisgame.reset()

            








    pygame.display.flip()
pygame.quit()
