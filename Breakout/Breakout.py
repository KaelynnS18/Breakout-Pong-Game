import pygame
pygame.init()
#screen
pygame.display.set_caption('Breakout')
surface = pygame.display.set_mode((1300,650))
#paddle
k1 = 650
k2 = 600
paddlemove = 5
RED = (255,0,0)
paddle = pygame.draw.rect(surface, RED, pygame.Rect(650, 600, 100, 30))
pygame.display.flip()
#circle
BLUE = (0, 0, 255)
ball = pygame.draw.circle(surface, (BLUE), [650, 325], 15)
pygame.display.flip()
#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#key press to move paddle
key_input = pygame.key.get_pressed()
if key_input [pygame.K_LEFT]:
    paddle.move(-paddlemove, 0)
if key_input [pygame.K_RIGHT]:
    paddle.move(paddlemove, 0)
 # Draws the surface object to the screen.
pygame.display.update()