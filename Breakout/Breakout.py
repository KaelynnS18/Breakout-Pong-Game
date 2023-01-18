#import pygame
#creating a screen, incomplete 
#background.fill((255, 0, 0))#figure out coloring, DONE
#pygame.display.flip()
#pygame.display.set_caption('Breakout')
 

#running = True
#while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
import pygame
 
# Initializing Pygame
pygame.init()
 
# Initializing surface
surface = pygame.display.set_mode((1300,650))
 
# Initializing Color
color = (255,0,0)
 
# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(650, 550, 100, 30),  2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False