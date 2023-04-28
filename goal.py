import pygame
import os

# create class Goal
# set goal image and initial position
# the goal moves downwards when player moves forward in sync with background

class Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "goal.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (320, -4300)
        self.goal_y = 0
        
    def control(self, speed):
        self.goal_y = speed * 18
        print(self.rect)
        
    def update(self): 
        self.rect.y = self.rect.y + self.goal_y 