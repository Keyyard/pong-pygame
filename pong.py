import pygame

pygame.init ()

# register
ball_x = 400
ball_y = 300
ball_vx = 5
ball_vy = 2

platform_vy = 0
platform_y = 300
platform_vy2 = 0
platform_y2 = 300

points_text = 0
points = 0
def platform (vy):
    global platform_y, platform_vy
    platform_vy = 0
    if pygame.key.get_pressed()[pygame.K_w]:
        if platform_y > 0:
            platform_vy = -5
    if pygame.key.get_pressed()[pygame.K_s]:
        if platform_y < 500:
            platform_vy = 5
    platform_y += platform_vy

def platform2 (vy):
    global platform_y2, platform_vy2
    platform_vy2 = 0
    if pygame.key.get_pressed()[pygame.K_UP]:
        if platform_y2 > 0:
            platform_vy2 = -5
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if platform_y2 < 500:
            platform_vy2 = 5
    platform_y2 += platform_vy2

def ball (vx, vy):
    global ball_x, ball_y, ball_vx, ball_vy
    ball_x += ball_vx
    ball_y += ball_vy
    #borders
    if ball_y > 580 or ball_y < 20:
        ball_vy *= -1
    if ball_x > 780 or ball_x < 20:
        ball_vx *= -1
    #platform
    if ball_x < 100 and ball_y >= platform_y and ball_y <= platform_y + 100:
        ball_vx *= -1
    #platform 2
    if ball_x > 700 and ball_y >= platform_y2 and ball_y <= platform_y2 + 100:
        ball_vx *= -1

#points
def func_points ():
    global points, ball_x, ball_y, ball_vx, ball_vy, platform_y, platform_y2, points_text
        #platform
    if ball_x < 100 and ball_y >= platform_y and ball_y <= platform_y + 100:
        points = points + 1
        #platform 2
    if ball_x > 700 and ball_y >= platform_y2 and ball_y <= platform_y2 + 100:
        points = points + 1
    font = pygame.font.Font('roboto.ttf', 20)
    points_text = font.render('Points: ' + str(points), True, (255,255,255))
#renders
def render():
    screen.fill ((0, 0, 0))
    pygame.draw.circle (screen, (255, 0, 0), (ball_x, ball_y), 20)
    pygame.draw.rect (screen, (255, 255, 255), (80, platform_y, 20, 100))
    pygame.draw.rect (screen, (255, 255, 255), (700, platform_y2, 20, 100))
    screen.blit(points_text, (10, 10))

run = True

screen = pygame.display.set_mode ((800, 600))
pygame.display.set_caption ("Pong")


while run:
    pygame.time.delay (10)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
    ball (ball_vx, ball_vy)
    platform (platform_vy)
    platform2 (platform_vy2)
    func_points ()
    render ()
    pygame.display.update ()
