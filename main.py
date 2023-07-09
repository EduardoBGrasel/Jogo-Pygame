import pygame
from sys import exit

pygame.init() #iniciar o pygame

screen = pygame.display.set_mode((800, 400)) #difinir o tamanho da tela 
pygame.display.set_caption('Corredor') #definir o nome da janela
clock = pygame.time.Clock() #criar uma instancia de relogio para limitar o fps
test_font = pygame.font.Font('font/PixelType.ttf', 50) #criar uma fonte (tipo da fone, tamanho da fonte)

#test_surface = pygame.Surface((100,200)) #superficie de teste
#test_surface.fill('Red') #preecher a superifice com uma cor

sky_surf = pygame.image.load('graphics/Sky.png').convert() #carregar uma imagem
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('My game', False, 'Black') #renderizar a fonte (texto, AA, cor)

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #carregar a lesma1
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() #carregar o player
player_rect = player_surf.get_rect(midbottom = (80, 300)) #recupera a área do jogador e aplica um retangulo

score_surf = test_font.render('Score', False, (64,64,64)) #criando a palavra score
score_rect = score_surf.get_rect(center = (400, 50)) #recuperando o retanculo do score



while True: #loop principal
    for event in pygame.event.get(): #recuperar um evento
        if event.type == pygame.QUIT: #caso o evento seja QUIT, fechar o jogo
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos):
                #print('ai')
    
    screen.blit(sky_surf, (0, 0)) #colocar o test_superficie no na tela, em tal posição ()
    screen.blit(ground_surf, (0, 300)) #desenhando o chão 
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    #pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 50) //desenhar uma linha
    #pygame.draw.ellipse(screen, 'Gold', pygame.Rect(50, 200, 100, 100)) //desenhar um circulo
    screen.blit(score_surf, score_rect) #desenhando o score
   
    snail_rect.left -= 3 #mover a lesma
    if snail_rect.right < 0:
        snail_rect.left = 800 #retornar a lesma
    screen.blit(snail_surf, (snail_rect))


    player_rect.right += 1  #mover o player
    screen.blit(player_surf, (player_rect))



    #if player_rect.colliderect(snail_rect): #checa se existe colisão entre o player e a lesma
    #mouse = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse)):
     #   print('ai') 



    pygame.display.update() #atualizar o display
    clock.tick(60) #limitar o fps
