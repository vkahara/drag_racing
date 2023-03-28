
import pygame
from pygame.locals import *
import player
import enemy
import camera
import sys
import os

# initialize pygame, create a screen and set its size to 640x640
# set window caption 
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Drag Racing!")

camera = camera.Camera()
player = player.Player((220, 550), "ford_scorpio")
enemy = enemy.Enemy((420, 550), "mitsubishi_evo")

all_sprites = pygame.sprite.RenderPlain()
all_sprites.add(camera)
all_sprites.add(player)
all_sprites.add(enemy)
clock = pygame.time.Clock()

race_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:        
                player.control(player.get_speed())
                camera.control(player.get_speed() * 10)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.control(0)
                camera.control(0)
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:        
                player.set_nitrous_on(True)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.set_nitrous_on(False)
                          
    screen.fill((33,170,33))
    all_sprites.draw(screen)
    all_sprites.update() 
    pygame.display.flip()    
    clock.tick(28)
            


        