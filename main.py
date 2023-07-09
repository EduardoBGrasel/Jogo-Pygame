import pygame
from sys import exit

pygame.init() #iniciar o pygame

screen = pygame.display.set_mode((800, 400)) #difinir o tamanho da tela 
pygame.display.set_caption('Corredor') #definir o nome da janela
clock = pygame.time.Clock() #criar uma instancia de relogio para limitar o fps
test_font = pygame.font.Font('font/PixelType.ttf', 50) #criar uma fonte (tipo da fone, tamanho da fonte)

#test_surface = pygame.Surface((100,200)) #superficie de teste
#test_surface.fill('Red') #preecher a superifice com uma cor

sky_surface = pygame.image.load('graphics/Sky.png').convert() #carregar uma imagem
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'Black') #renderizar a fonte (texto, AA, cor)

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #carregar a lesma1
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() #carregar o player
player_rect = player_surf.get_rect(midbottom = (80, 300)) #recupera a área do jogador e aplica um retangulo



while True: #loop principal
    for event in pygame.event.get(): #recuperar um evento
        if event.type == pygame.QUIT: #caso o evento seja QUIT, fechar o jogo
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('ai')
    
    screen.blit(sky_surface, (0, 0)) #colocar o test_superficie no na tela, em tal posição ()
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
   
    snail_rect.left -= 3 #mover a lesma
    if snail_rect.right < 0:
        snail_rect.left = 800 #retornar a lesma
    screen.blit(snail_surface, (snail_rect))
    player_rect.right += 1  #mover o player
    screen.blit(player_surf, (player_rect))

    #if player_rect.colliderect(snail_rect): #checa se existe colisão entre o player e a lesma
    #mouse = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse)):
     #   print('ai') 



    pygame.display.update() #atualizar o display
    clock.tick(60) #limitar o fps
