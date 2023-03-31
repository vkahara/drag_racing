
import pygame
from pygame.locals import *
import player
import enemy
import camera
import cars_module
import sys
import os

# initialize pygame, create a screen and set its size to 640x640
# set window caption 
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Drag Racing!")

clock = pygame.time.Clock()

#define small and big fonts and set them to system default font
small_font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 60)

#function to display text to screen
def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect = (x, y)
    surface.blit(text_object, text_rect)
    
#start menu function contains start menu as a separate game loop
#start menu draws text and menu background to screen
#start menu is used to select player car

def start_menu():
    car_preview = 0
    car_preview_image = pygame.image.load((os.path.join("images", "ford_scorpio.png")))
    car_preview_image = pygame.transform.scale(car_preview_image, (84,177))
    while True:
        for event in pygame.event.get():
            global chosen_car #global variable chosen car is assigned value in the menu
            
            garage_background = pygame.image.load(os.path.join("images", "garage_background.png"))
            garage_background = pygame.transform.scale(garage_background, (640,640))
            screen.blit(garage_background, (0,0))
    
            draw_text("select car", big_font, (0,0,0), screen, 200 , 200)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if car_preview < (len(cars_module.cars_dict)-1):
                        car_preview += 1
                    else:
                        car_preview = car_preview - (len(cars_module.cars_dict)-1)
                    
                if event.key == pygame.K_RETURN:   
                    print("test") 
                    chosen_car = cars_module.get_car_key(car_preview)
                    print(chosen_car)
                    return
                
        car_preview_image = pygame.image.load((os.path.join("images", cars_module.cycle_images(car_preview))))
        car_preview_image = pygame.transform.scale(car_preview_image, (84,177))        
        screen.blit(car_preview_image, (320, 320))      
        
        draw_text((cars_module.cycle_names(car_preview)), small_font, (0,0,0), screen, 260, 550)
        pygame.display.update()
        clock.tick(15)

start_menu()
print(chosen_car)
# create instance of player, player takes position and global variable chosen car
# player selects instance of car from cars_module based on chosen car variable
player = player.Player((220, 550), chosen_car)
camera = camera.Camera()
enemy = enemy.Enemy((420, 550), "ford_scorpio")

all_sprites = pygame.sprite.RenderPlain()
all_sprites.add(camera)
all_sprites.add(player)
all_sprites.add(enemy)



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
    
    
            


        