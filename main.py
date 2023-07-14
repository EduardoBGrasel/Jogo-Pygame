import pygame
from sys import exit
from random import randint, choice
from Player import Player
from Obstacles import Obstacle

def display_score(): #mostrar o score baseado no tempo em que o jogo está rodando
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def collision_spite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False): #retorna uma lista caso tenha colisões
        obstacle_group.empty()
        return False
    else:
        return True
    

pygame.init() #iniciar o pygame

screen = pygame.display.set_mode((800, 400)) #difinir o tamanho da tela 
pygame.display.set_caption('Corredor') #definir o nome da janela
clock = pygame.time.Clock() #criar uma instancia de relogio para limitar o fps
test_font = pygame.font.Font('font/PixelType.ttf', 50) #criar uma fonte (tipo da fone, tamanho da fonte)


sky_surf = pygame.image.load('graphics/Sky.png').convert() #carregar uma imagem
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('My game', False, 'Black') #renderizar a fonte (texto, AA, cor)
game_active = False
start_time = 0
score = 0

#grupos
player = pygame.sprite.GroupSingle() #criar o player
player.add(Player())

obstacle_group = pygame.sprite.Group() #criar os obstaculos


#player game over e inicio
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha() #tela de fim de jogo
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))


#textos game over
game_name = test_font.render('Pixel Runner', False, (111, 196, 169)) #texto
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Aperte Space para correr', False, (111, 196, 169)) #texto 
game_message_rect = game_message.get_rect(center = (400, 340))

#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500) #setar um timer

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

bg_Music = pygame.mixer.Sound('audio/music.wav')
bg_Music.set_volume(0.4)
bg_Music.play()



while True: #loop principal
    for event in pygame.event.get(): #recuperar um evento
        if event.type == pygame.QUIT: #caso o evento seja QUIT, fechar o jogo
            pygame.quit()
            exit()                           
        
        else: #resetar o jogo
            if event.type == pygame.KEYDOWN and game_active == False:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
        
        if game_active: #adicionar os obstaculos
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))

            

   
    if game_active: #se o jogo estiver ativo
        screen.blit(sky_surf, (0, 0)) #colocar o test_superficie no na tela, em tal posição ()
        screen.blit(ground_surf, (0, 300)) #desenhando o chão 
        score = display_score()
    
        #player
        player.draw(screen)
        player.update()

        #obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        #colisão
        game_active = collision_spite()


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
        obstacle_rect_list = []
        player_gravity = 0


    pygame.display.update() #atualizar o display
    clock.tick(60) #limitar o fps
