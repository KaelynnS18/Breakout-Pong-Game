import pygame
pygame.init()
clock = pygame.time.Clock()

screen_height = 650
screen_width = 1300
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
paddle_x = 650
paddle_y = 600
paddlemove = 5
ballx = 650
bally = 325
ballmove_x = 5
ballmove_y = 5
screen_left = 40
screen_right = screen_width - 40
screen_top = 40
screen_bottom = screen_height - 40

screen = pygame.display.set_mode((screen_width, screen_height))
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
        paddle_x += paddlemove

    screen.fill(BLACK)

    paddle = pygame.draw.rect(screen, RED, pygame.Rect(paddle_x, paddle_y, 100, 30))

    ball = pygame.draw.circle(screen, (BLUE), [ballx, bally], 15)

    if paddle.colliderect(ball):
        ballmove_y = ballmove_y * -1
        ballx = ballx + 10

    ballx = ballmove_x + ballx
    bally = ballmove_y + bally
    if ballx < screen_left:
        ballmove_x = ballmove_x * -1

    if ballx > screen_right:
        ballmove_x = ballmove_x * -1

    if bally < screen_top:
        ballmove_y = ballmove_y * -1

    if bally > screen_bottom:
        ballx = 650
        bally = 325 

    
        


#add ball movement, and walls

    pygame.display.update()
    clock.tick(50)