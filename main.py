
import pygame
from pygame.locals import *
import player
import enemy
import camera
import cars_module
import goal
import sys
import os

# initialize pygame, create a screen and set its size to 640x640
# set window caption
pygame.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption("Drag Racing!")
clock = pygame.time.Clock()

# define small and big fonts and set them to system default font
small_font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 60)

# function to display text to screen
def draw_text(text, font, color, surface, x, y):
    text_object = font.render(text, 1, color)
    text_rect = text_object.get_rect()
    text_rect = (x, y)
    surface.blit(text_object, text_rect)

# start menu function contains start menu as a separate game loop
# start menu draws text and menu background to screen
# start menu is used to select player car
def start_menu():
    car_preview = 0
    car_preview_image = pygame.image.load(
        (os.path.join("images", "ford_scorpio.png")))
    car_preview_image = pygame.transform.scale(car_preview_image, (168, 354))
    while True:
        for event in pygame.event.get():
            global chosen_car  # global variable chosen car is assigned value in the menu
            garage_background = pygame.image.load(
                os.path.join("images", "garage_background.png"))
            garage_background = pygame.transform.scale(
                garage_background, (640, 640))
            screen.blit(garage_background, (0, 0))
            draw_text("select car", big_font, (0, 0, 0), screen, 215, 530)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if car_preview < (len(cars_module.cars_dict)-1):
                        car_preview += 1
                    else:
                        car_preview = car_preview - \
                            (len(cars_module.cars_dict)-1)

                if event.key == pygame.K_LEFT:
                    car_preview -= 1
                    if car_preview < 0:
                        car_preview = car_preview + \
                            (len(cars_module.cars_dict)-1)

                if event.key == pygame.K_RETURN:
                    chosen_car = cars_module.get_car_key(car_preview)
                    return

        car_preview_image = pygame.image.load(
            (os.path.join("images", cars_module.cycle_images(car_preview))))
        car_preview_image = pygame.transform.scale(
            car_preview_image, (168, 354))

        screen.blit(car_preview_image, (235, 150))

        draw_text((cars_module.cycle_names(car_preview)),
                  small_font, (0, 0, 0), screen, 260, 570)
        pygame.display.update()
        clock.tick(15)


def mainloop():
    all_sprites.draw(screen)

    draw_text("Ready", big_font, (255, 0, 0), screen, 250, 240)
    pygame.display.update()
    pygame.time.wait(3000)

    draw_text("Set", big_font, (255, 255, 0), screen, 250, 280)
    pygame.display.update()
    pygame.time.wait(3000)

    draw_text("go", big_font, (0, 180, 0), screen, 250, 320)
    pygame.display.update()
    pygame.time.wait(1000)

    game_over = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.control(player.get_speed())
                    camera.control(player.get_speed() * 35)
                    goal.control(player.get_speed())

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player.control(0)
                    camera.control(0)
                    goal.control(0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.set_nitrous_on(True)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.set_nitrous_on(False)

        # check if player touches goal line
        if player.rect.colliderect(goal.rect):
            game_over = True

        if game_over:
            draw_text(("GAME OVER!"), big_font, (0, 0, 255), screen, 240, 240)
            draw_text(("Game closes automatically in 5 seconds!"),
                      small_font, (0, 200, 0), screen, 180, 320)

            pygame.display.update()
            pygame.time.wait(5000)
            pygame.quit()

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(28)


start_menu()  # run start_menu loop

# create instance of player, player takes position and global variable chosen car
# player selects instance of car from cars_module based on chosen car variable
player = player.Player((220, 550), chosen_car)
camera = camera.Camera()
goal = goal.Goal()
enemy = enemy.Enemy((420, 550), "ford_scorpio")

all_sprites = pygame.sprite.RenderPlain()
all_sprites.add(camera)
all_sprites.add(goal)
all_sprites.add(player)
all_sprites.add(enemy)
mainloop()  # run main loop
