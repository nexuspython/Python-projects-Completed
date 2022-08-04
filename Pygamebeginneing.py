from re import T
import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((900 , 600))
pygame.display.set_caption("Nigga")
text = pygame.font.Font(None , 50)
text_surf = text.render("First Time" , True , "Black")
clock = pygame.time.Clock()
sky = pygame.image.load("Sky.jpg").convert_alpha()
ground = pygame.image.load("ground.png").convert_alpha()
snail = pygame.image.load("snail1.png").convert_alpha()
playersurface = pygame.image.load("player_walk_1.png").convert_alpha()
playerrec = playersurface.get_rect(topleft = (800 , 390))
snailrec = snail.get_rect(bottomleft = (800,475))
snail_x_pos = 800
player_x_pos = 800

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            if playerrec.collidepoint(event.pos):print("Collided")
    screen.blit(sky,(0 , -180))
    screen.blit(ground,(0 , 450))
    screen.blit(text_surf,(350 , 50))
    screen.blit(playersurface,(player_x_pos , 390))
    screen.blit(playersurface,playerrec)
    screen.blit(snail,snailrec)
    snailrec.x -=4
    if snailrec.right <= 0: snailrec.left = 900

    a = playerrec.colliderect(snailrec)

    # if a == 1:
    #     print("colided")
    # mousepos = pygame.mouse.get_pos()
    # if playerrec.collidepoint((mousepos)):
    #     print(pygame.mouse.get_pressed())
    
    # screen.blit(snail,(800 , 434))
    pygame.display.update()
    clock.tick(60)