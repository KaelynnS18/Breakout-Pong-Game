import pygame
pygame.init()
clock = pygame.time.Clock()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
paddle_x = 500
paddle_y = 300
paddlemove = 5

screen = pygame.display.set_mode((1300, 650))
pygame.display.set_caption('Breakout')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_input = pygame.key.get_pressed()
    if key_input [pygame.K_LEFT]:
        paddle_x -= paddlemove
    if key_input [pygame.K_RIGHT]:
        paddle_y += paddlemove

    screen.fill(BLACK)

    paddle = pygame.draw.rect(screen, RED, (paddle_x, paddle_y, 50, 40))

    ball = pygame.draw.circle(screen, (BLUE), [650, 325], 15)

#add ball movement, and walls

    pygame.display.update()
    clock.tick(50)