import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite): #criar um novo sprite do pygame
    def __init__(self, type):
        super().__init__() #necessario pra o pygame funcionar

        if type == 'fly': #carregando as imagens da mosca
            fly_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 210
        else: #carregando as imagens da lesma
            snail_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        
        self.animation_index = 0 #index de animação
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))
    
    def animation_state(self): #animar a lesma e a mosca
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destroy()

    def destroy(self): #caso saia da dela, deletar o sprite
        if self.rect.x <= -100:
            self.kill()

    
