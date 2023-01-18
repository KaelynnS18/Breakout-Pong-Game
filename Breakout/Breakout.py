import pygame
pygame.init()
pygame.display.set_caption('Breakout')
surface = pygame.display.set_mode((1300,650))
color = (255,0,0)
pygame.draw.rect(surface, color, pygame.Rect(650, 550, 100, 30),  2)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False