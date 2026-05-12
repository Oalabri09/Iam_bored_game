import pygame
from games.game2048.play_2048 import play_2048
from games.YouTubeGame.MainRunner import play_runner
from player.playerclass import Player


pygame.init()
screen = pygame.display.set_mode((800, 600))

## Images ###

background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (800, 600))
logo_2048 = pygame.image.load("assets/2048_logo.png").convert_alpha()
logo_2048 = pygame.transform.scale(logo_2048, (100, 100))
logo_2048_rect = logo_2048.get_rect(topleft=(150, 50))


logo_runner = pygame.image.load("assets/YouTubeGame_logo.png").convert_alpha()
logo_runner = pygame.transform.scale(logo_runner, (100, 100))
logo_runner_rect = logo_runner.get_rect(topleft=(550, 50))

player = Player()
player_rect = player.rect 

clock = pygame.time.Clock()

def collision_with_2048(player_rect, logo_2048_rect):
    return player_rect.colliderect(logo_2048_rect)

def collision_with_runner(player_rect, logo_runner_rect):
    return player_rect.colliderect(logo_runner_rect)


##################

world_running = True
while world_running:
    dt = clock.tick(60) / 1000  
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e: 
                if collision_with_2048(player.rect, logo_2048_rect):
                    result = play_2048(screen)

                    if result == "QUIT_ALL":
                        world_running = False

                    elif result == "BACK_TO_MAP":
                        print("Welcome Back from 2048!")
                        
                elif collision_with_runner(player.rect, logo_runner_rect):
                    result = play_runner(screen)
                    
                    if result == "QUIT_ALL":
                        world_running = False
                    elif result == "BACK_TO_MAP":
                        print("Welcome Back from Runner!")
                    else:
                        print("Welcome Back from Runner!")

    player.handle_input(dt)
    screen.blit(background, (0, 0))
    screen.blit(logo_2048, (150, 50)) 
    screen.blit(logo_runner, (550, 50)) 
    
    player.draw(screen)

    pygame.display.flip()

pygame.quit()