import pygame
pygame.init()
#screen
pygame.display.set_caption('Breakout')
surface = pygame.display.set_mode((1300,650))
#paddle
RED = (255,0,0)
pygame.draw.rect(surface, RED, pygame.Rect(650, 550, 100, 30))
pygame.display.flip()
#circle
BLUE = (0, 0, 255)
pygame.draw.circle(surface, (BLUE), [650, 325], 15)
 # Draws the surface object to the screen.
pygame.display.update()
#loop preventing finish
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False