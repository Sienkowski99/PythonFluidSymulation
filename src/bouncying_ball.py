import sys, pygame, pymunk


pygame.init()
FPS_lock = 60
size = width, height = 1000, 700
speed = [0, 0]
black = 0, 0, 0
magenta = 255, 0, 255

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

font = pygame.font.SysFont("Arial", 18)


def update_fps():
    fps = str(int(clock.get_fps()))
    # print(fps)
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


def pitagoras(a1, b1, a2, b2):
    c_square = (abs(a1-a2)*abs(a1-a2))+(abs(b1-b2)*abs(b1-b2))
    c = pow(c_square, 1/2)
    return c

drawing = False
mouse_position = {
    "previous": None,
    "now": None
}
being_clicked = False

breaking_factor = 1.02
bounce = 0

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bounce = 0
            being_clicked = True
            mouse_position["previous"] = pygame.mouse.get_pos()
            mouse_position["now"] = pygame.mouse.get_pos()
            print("KLIK")
            last_mouse_position = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            being_clicked = False
            # mouse_position["now"] = pygame.mouse.get_pos()
            print("UN-KLIK")

            # speed = [(mouse_position["previous"][0] - mouse_position["now"][1])/100, (mouse_position["previous"][1] - mouse_position["now"][1])/100]\



            #x vector value
            x_vector = mouse_position["previous"][0] - mouse_position["now"][0]

            #y vector value
            y_vector = mouse_position["previous"][1] - mouse_position["now"][1]

            #CALCULATING X MOVEMENT
            if mouse_position["previous"][0] - mouse_position["now"][0] > 0:
                speed = [x_vector/10, speed[1]]
            elif mouse_position["previous"][0] - mouse_position["now"][0] < 0:
                speed = [x_vector/10, speed[1]]
            elif mouse_position["previous"][0] - mouse_position["now"][0] == 0:
                speed = [0, speed[1]]
            #CALCULATING Y MOVEMENT
            if mouse_position["previous"][1] - mouse_position["now"][1] > 0:
                speed = [speed[0], y_vector/10]
            elif mouse_position["previous"][1] - mouse_position["now"][1] < 0:
                speed = [speed[0], y_vector/10]
            elif mouse_position["previous"][1] - mouse_position["now"][1] == 0:
                speed = [speed[0], 0]

        elif event.type == pygame.MOUSEMOTION:
            if being_clicked:
                mouse_position["now"] = pygame.mouse.get_pos()
                screen.fill((50, 20, 30))
                line_color = (75, 215, 55)
                line_length = pitagoras(mouse_position["previous"][0], mouse_position["previous"][1], mouse_position["now"][0], mouse_position["now"][1])
                if line_length > 200:
                    line_color = (255, 150, 45)
                if line_length > 400:
                    line_color = (215, 55, 55)
                pygame.draw.line(screen, line_color, mouse_position["previous"], mouse_position["now"], 10)
            # last_mouse_position = mouse_position

    # if abs(speed[0]) < 0.001:
    #     speed = [0, speed[1]]
    # if abs(speed[1]) < 0.001:
    #     speed = [speed[0], 0]
    speed = [speed[0] / breaking_factor, speed[1] / breaking_factor]
    print(speed)

    ballrect = ballrect.move(speed)

    if not being_clicked:
        screen.fill((50, 20, 30))
    print(ballrect)
    if ballrect.left < 0 or ballrect.right > width:
        print(f"BOUNCE {bounce}")
        bounce += 1
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        print(f"BOUNCE {bounce}")
        bounce += 1
        speed[1] = -speed[1]



    screen.blit(ball, ballrect)

    # draw_apple(apples)

    screen.blit(update_fps(), (10, 10))
    clock.tick(FPS_lock)
    # pygame.display.update()
    # clock.tick()


    pygame.display.flip()
