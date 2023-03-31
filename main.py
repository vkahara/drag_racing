
import pygame
from pygame.locals import *
import player
import enemy
import camera
import sys

# initialize pygame, create a screen and set its size to 640x640
# set window caption 
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Drag Racing!")

camera = camera.Camera()
player = player.Player((220, 550), "volkswagen_golf")
enemy = enemy.Enemy((420, 550), "ford_scorpio")

all_sprites = pygame.sprite.RenderPlain()
all_sprites.add(camera)
all_sprites.add(player)
all_sprites.add(enemy)
clock = pygame.time.Clock()

small_font = pygame.font.SysFont(None, 20)
big_font = pygame.font.SysFont(None, 40)

def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)
    

def start_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                return
            
            
        screen.fill((69,69,69))    
        draw_text("drag_racing", big_font, (0,0,0), screen, 20 , 20)
        pygame.display.update()
        clock.tick(15)

start_menu()
while True:
    events = pygame.event.get()
    for event in events:
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
    
    
            


        