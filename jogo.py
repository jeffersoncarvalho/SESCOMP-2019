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

#delay
time.sleep(2)

#fecha a tela e o jogo
pygame.quit()
quit()