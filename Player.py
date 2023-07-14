import pygame

class Player(pygame.sprite.Sprite): #cria uma classe sprite para o player

    def __init__(self):
        super().__init__() #necessario para o pygame funcionar
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() #carregar o player
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha() #carregar o player
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha() #carregar o player
        self.player_index = 0 #index de animação
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300)) #posição do player
        self.gravity = 0 #gravidade
    
    def player_input(self): #fazer o jogador pular caso aperte espaço
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.rect.bottom == 300:
            self.gravity = -20
    
    def apply_gravity(self): #aplicar gravidade no jogo
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animate_state(self): #animação do player
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animate_state()