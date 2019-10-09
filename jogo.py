#sudo apt-get install python-pygame
import pygame
import time

#iniciar o pygame
pygame.init()

#display
display_width = 640
display_height = 480

#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill((255,255,255))

#atualiza tela
pygame.display.update()
pygame.display.set_caption("SESCOMP GAME")

#clock
clock = pygame.time.Clock()

####LOGICA PRINCIPAL
fim = False
#loop do jogo
while not fim:
	#lendo uma lista de eventos [eve1,eve2,even3...]
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			fim = True
		#imprimindo evento
		print(evento)
	pygame.display.update()
	clock.tick(60)

####FIM DA LOGICA PRINCIPAL

#fecha a tela e o jogo
pygame.quit()
quit()