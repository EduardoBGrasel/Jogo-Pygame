import pygame
from sys import exit

pygame.init() #iniciar o pygame

screen = pygame.display.set_mode((800, 400)) #difinir o tamanho da tela 
pygame.display.set_caption('Corredor') #definir o nome da janela
clock = pygame.time.Clock() #criar uma instancia de relogio para limitar o fps

test_surface = pygame.Surface((100,200)) #superficie de teste
test_surface.fill('Red') #preecher a superifice com uma cor

while True: #loop principal
    for event in pygame.event.get(): #recuperar um evento
        if event.type == pygame.QUIT: #caso o evento seja QUIT, fechar o jogo
            pygame.quit()
            exit()
    
    screen.blit(test_surface, (200, 100)) #colocar o test_superficie no na tela, em tal posição ()

    pygame.display.update() #atualizar o display
    clock.tick(60) #limitar o fps
