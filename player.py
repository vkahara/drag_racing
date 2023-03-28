import os
import pygame
import cars_module
import time

# create a player sprite class
class Player(pygame.sprite.Sprite):
    # Player takes a position value and 
    # chosen car as string
    # Initialize Player class with 
    # data attributes chosen_car, image, rect and speed
    def __init__(self, position, chosen_car):  
        #player inherits sprite
        pygame.sprite.Sprite.__init__(self) 
        
        #set attribute chosen_car's value to chosen car from cars_module
        self.chosen_car = cars_module.choose_car(chosen_car)
        
        #use os to join folder name to chosen car objects image value
        self.image = pygame.image.load(os.path.join("images",\
            getattr(self.chosen_car, "image")))
        
        self.image = pygame.transform.scale(self.image, (28,59))
        self.rect = self.image.get_rect()
        self.rect.center = position
        #set speed to chosen car objects image value 
        self.speed = getattr(self.chosen_car, "speed")
        self.movey = 0
        self.nitrous_duration = getattr(self.chosen_car, "nitrous_duration")
        self.nitrous_on = False
           
    def control(self, speed):
        self.movey = - speed
        
    def set_nitrous_on(self, set_nitrous_on):
            self.nitrous_on = set_nitrous_on
        
    def update(self):
        self.rect.y = self.rect.y + self.movey
        if self.nitrous_on and (self.nitrous_duration > 1):
            
            self.rect.y = self.rect.y + self.movey-3
            print(self.nitrous_duration)
            self.nitrous_duration -= 1
        
            
        
    def get_speed(self):
        return self.speed
    
    def get_y(self):
        return self.rect.y
    