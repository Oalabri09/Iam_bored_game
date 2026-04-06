import pygame
from games.game2048.play_2048 import play_2048
from player.playerclass import Player


pygame.init()
screen = pygame.display.set_mode((800, 600))

## Images ###

background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (800, 600))

player = Player()

clock = pygame.time.Clock()


##################

world_running = True
while world_running:
    dt = clock.tick(60) / 1000  
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            world_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e: 
                result = play_2048(screen)

                if result == "QUIT_ALL":
                    world_running = False

                elif result == "BACK_TO_MAP":
                    print("Welcom Back to map!")

    player.handle_input(dt)
    screen.blit(background, (0, 0))
    player.draw(screen)

    pygame.display.flip()

pygame.quit()