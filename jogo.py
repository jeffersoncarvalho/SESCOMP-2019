#sudo apt-get install python-pygame
import pygame
import time

#iniciar o pygame
pygame.init()

#display
display_width = 640
display_height = 480

#cores
branca = (255,255,255)

#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(branca)

#atualiza tela
pygame.display.update()
pygame.display.set_caption("SESCOMP GAME")

#clock
clock = pygame.time.Clock()

#dados do heroi
heroi = pygame.image.load("emoji.png")
hx = 50
hy = 150

#FUNCOES DO JOGO
def apaga_tela():
	gameDisplay.fill(branca)

def desenha_heroi(x,y):
	gameDisplay.blit(heroi,(x,y))

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
        #evento do teclado
        if evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_LEFT:
				hx = hx - 5
			elif evento.key == pygame.K_RIGHT:
				hx = hx + 5
			elif evento.key == pygame.K_UP:
				hy = hy - 5
			elif evento.key == pygame.K_DOWN:
				hy = hy + 5
    #apaga a tela
	apaga_tela()
    #desenha o heroi
	desenha_heroi(hx,hy)
    #atualiza tela
	pygame.display.update()
	clock.tick(60)
####FIM DA LOGICA PRINCIPAL

#fecha a tela e o jogo
pygame.quit()
quit()