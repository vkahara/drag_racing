import pygame
import os

#move camera in sync with goal line when player moves

class Camera(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("images", "background.png"))
        self.image = pygame.transform.scale(self.image, (640,10000))
        self.rect = self.image.get_rect()
        self.rect.center = (320, -4300)
        self.camera_y = 0
        
    def control(self, speed):
            self.camera_y = speed
        
    def update(self): 
        self.rect.y = self.rect.y + self.camera_y