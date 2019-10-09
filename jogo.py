#sudo apt-get install python-pygame
import pygame
import time
import random

#iniciar o pygame
pygame.init()

#display
display_width = 640
display_height = 480

#cores
branca = (255,255,255)
preto = (0,0,0)
amarelo = (255,255,0)

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
hx_change = 0
hy_change = 0

#FUNCOES DO JOGO
def apaga_tela():
	gameDisplay.fill(branca)

def desenha_heroi(x,y):
	gameDisplay.blit(heroi,(x,y))

def desenha_limites():
	pygame.draw.line(gameDisplay,preto,(20,20),(display_width-20,20),1)
	pygame.draw.line(gameDisplay,preto,(20,20),(20,display_height-20),1)
	pygame.draw.line(gameDisplay,preto,(20,display_height-20),
		(display_width-20,display_height-20),1)
	pygame.draw.line(gameDisplay,preto,(display_width-20,20),
		(display_width-20,display_height-20),1)

def desenha_ouros(ouros):
	for ouro in ouros:
		ouroX = ouro[0]
		ouroY = ouro[1]
		pygame.draw.circle(gameDisplay,amarelo,(ouroX,ouroY),13,0)

def ultrapassou_limiteX(meuX_futuro):
	if meuX_futuro<20 or meuX_futuro>display_width-45:
		return True
	return False

def ultrapassou_limiteY(meuY_futuro):
	if meuY_futuro<20 or meuY_futuro>display_height-45:
		return True
	return False

def criar_ouros():
	ouros = []
	for i in range(10):
		x = random.randint(50,display_width-40)
		y = random.randint(50,display_height-40)
		ouros.append([x,y])
	return ouros

####LOGICA PRINCIPAL
fim = False
ouros = criar_ouros()
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
				hx_change = - 5
			elif evento.key == pygame.K_RIGHT:
				hx_change = + 5
			elif evento.key == pygame.K_UP:
				hy_change = - 5
			elif evento.key == pygame.K_DOWN:
				hy_change = + 5
        if evento.type == pygame.KEYUP:
			if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
				hx_change = 0
			if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
				hy_change = 0
        
    #apaga a tela
	apaga_tela()
    #desenha ouro
	desenha_ouros(ouros)
    #desenha o heroi
	if(not ultrapassou_limiteX(hx+hx_change)):
		hx = hx + hx_change
	if(not ultrapassou_limiteY(hy+hy_change)):
		hy = hy + hy_change
	desenha_heroi(hx,hy)
    #desenha limites
	desenha_limites()	
    #atualiza tela
	pygame.display.update()
	clock.tick(60)
####FIM DA LOGICA PRINCIPAL

#fecha a tela e o jogo
pygame.quit()
quit()