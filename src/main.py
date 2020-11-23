import sys, pygame, pymunk

pygame.init()
FPS_lock = 60
size = width, height = 1000, 700
speed = [3, 3]
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
    # print(fps)
    fps_text = font.render(fps, True, pygame.Color("coral"))
    return fps_text


space = pymunk.Space()
gravity_sideways = 20
gravity_downwoards = 400
space.gravity = (gravity_sideways, gravity_downwoards)

before_x = 100
before_y = 50

def create_apple(space):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (100, 50)
    shape = pymunk.Circle(body, 30)
    space.add(body, shape)
    return shape

pygame.draw.line(screen, (255, 255, 255), (before_x - 50, before_y), (before_x - 50, before_y + 500), 2)
pygame.draw.line(screen, (255, 255, 255), (before_x - 50, before_y + 500), (before_x + 500, before_y + 500), 2)

def draw_apple(apples):
    global before_x, before_y
    # global before_x, before_y
    for apple in apples:
        pos_x = int(apple.body.position.x)
        pos_y = int(apple.body.position.y)
        # pygame.draw.circle(screen, (255, 255, 255), (pos_x, pos_y), 2)
        if before_x >= 100000:
            return
        pygame.draw.line(screen, (255,50,100),(before_x, before_y),(pos_x,pos_y),2)
        # global before_x, before_y
        before_x = pos_x
        before_y = pos_y


apples = []
apples.append(create_apple(space))

drawing = False
last_mouse_position = ()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                drawing = False
                print("UN-KLIK")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not drawing:
                drawing = True
                print("KLIK")
                last_mouse_position = pygame.mouse.get_pos()
            else:
                drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                mouse_position = pygame.mouse.get_pos()
                pygame.draw.line(screen, (255, 50, 120), last_mouse_position, mouse_position, 2)
                last_mouse_position = mouse_position


    ballrect = ballrect.move(speed)

    keys = pygame.key.get_pressed()
    # print(keys)
    if keys[pygame.K_LEFT]:
        speed = [-4, 0]
    if keys[pygame.K_RIGHT]:
        speed = [4, 0]
    if keys[pygame.K_UP]:
        speed = [0, -4]
    if keys[pygame.K_DOWN]:
        speed = [0, 4]


    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # screen.fill((50,20,30))

    # screen.blit(ball, ballrect)

    draw_apple(apples)

    screen.blit(update_fps(), (10, 10))
    clock.tick(FPS_lock)
    space.step(1/50)
    # pygame.display.update()
    gravity_sideways = gravity_sideways * 1.1
    space.gravity = (gravity_sideways, gravity_downwoards)
    # clock.tick()


    pygame.display.flip()
