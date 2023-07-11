import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time
    

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
game_active = False
start_time = 0
score = 0

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha() #carregar a lesma1
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha() #carregar o player
player_rect = player_surf.get_rect(midbottom = (80, 300)) #recupera a área do jogador e aplica um retangulo
player_gravity = 0

#player game over e inicio
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

#score_surf = test_font.render('Score', False, (64,64,64)) #criando a palavra score
#score_rect = score_surf.get_rect(center = (400, 50)) #recuperando o retanculo do score

#textos game over
game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Aperte Space para correr', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 340))



while True: #loop principal
    for event in pygame.event.get(): #recuperar um evento
        if event.type == pygame.QUIT: #caso o evento seja QUIT, fechar o jogo
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN: #caso o jogador clique no boneco, ele ira pular 
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 300:
                        player_gravity = -20
                
                    
            
            if event.type == pygame.KEYDOWN: #verificar se o alguma key foi pressionada
                if event.key == pygame.K_SPACE: #se a key for espaço
                    if player_rect.bottom == 300:
                        player_gravity = -20
        
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.left = 800
                    start_time = int(pygame.time.get_ticks() / 1000)
   
    if game_active:
        screen.blit(sky_surf, (0, 0)) #colocar o test_superficie no na tela, em tal posição ()
        screen.blit(ground_surf, (0, 300)) #desenhando o chão 
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect) #desenhando o score
        score = display_score()
    
        snail_rect.left -= 4 #mover a lesma
        if snail_rect.right < 0:
            snail_rect.left = 800 #retornar a lesma
        screen.blit(snail_surf, (snail_rect))


        #player
        player_gravity += 1
        player_rect.y += player_gravity #adicionando gravidade

        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, (player_rect))

        #colisão
        if snail_rect.colliderect(player_rect):
            game_active = False
    else: #game over 
        screen.fill((64, 129, 162)) #preenche a tela com azul
        screen.blit(player_stand, player_stand_rect) #colocar o player no centro
        screen.blit(game_name, game_name_rect) #colocar o texto pixel runner
        score_message = test_font.render(f'Seus pontos: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        if score == 0:
            screen.blit(game_message, game_message_rect) #mostrar o texto para apertar espaço
        else:
            screen.blit(score_message, score_message_rect)




    pygame.display.update() #atualizar o display
    clock.tick(60) #limitar o fps
