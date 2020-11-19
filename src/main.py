import sys, pygame

pygame.init()

size = width, height = 1000, 700
speed = [9, 9]
black = 0, 0, 0
magenta = 255, 0, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
print(ballrect)

font = pygame.font.SysFont("Arial", 18)
def update_fps():
    fps = str(int(clock.get_fps()))
    print(fps)
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)

    screen.blit(update_fps(), (10, 10))
    clock.tick()

    pygame.display.flip()
