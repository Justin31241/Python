import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

red = (255, 0, 0)
white = (255, 255, 255)

player_speed = 20

player_y = 500
player_radius = 20
player_x = player_radius

opponent_y = 500
opponent_radius = 20
opponent_x = 1000 - player_radius

ball_x = 500
ball_y = 500
ball_radius = 10
ball_speed_x = -player_speed / 6
ball_speed_y = random.uniform(-1, 1) * (player_speed / 6)

colliders = []
obstacle_circles = []

def check_collisions():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    
    paddle_was_hit = False

    for c in colliders:
        c_x, c_y = c['pos']
        c_radius = c['radius']

        distance = math.hypot(c_x - ball_x, c_y - ball_y)
        radi_sum = c_radius + ball_radius

        if distance <= radi_sum and distance != 0:
            
            overlap = radi_sum - distance
            dx = ball_x - c_x
            dy = ball_y - c_y
            
            ball_x += (dx / distance) * overlap
            ball_y += (dy / distance) * overlap

            nx = dx / distance
            ny = dy / distance
            
            dot = ball_speed_x * nx + ball_speed_y * ny
            
            ball_speed_x -= 2 * dot * nx
            ball_speed_y -= 2 * dot * ny
            
            if c.get('is_paddle', False):
                  ball_speed_x *= 1.05
                  ball_speed_y *= 1.05
                  paddle_was_hit = True
    
    return paddle_was_hit


def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y
    global obstacle_circles 
    
    ball_x = 500
    ball_y = 500
    ball_speed_x = -player_speed / 6 * random.choice([1, -1])
    ball_speed_y = random.uniform(-1, 1) * (player_speed / 6)
    
    obstacle_circles.clear() 


def add_circle():
    circle_y = random.randint(200, 800)
    circle_x = random.randint(300, 700) 
    obstacle_circles.append({'pos': (circle_x, circle_y), 'radius': 20})

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_x - ball_radius < 0 or ball_x + ball_radius > 1000:
        reset_ball() 

    if ball_y - ball_radius <= 0:
        ball_y = ball_radius
        ball_speed_y *= -1
    elif ball_y + ball_radius >= 1000:
        ball_y = 1000 - ball_radius
        ball_speed_y *= -1

    keys = pygame.key.get_pressed()

    if keys != False:
        if keys[pygame.K_UP]:
            player_y -= player_speed
        elif keys[pygame.K_DOWN]:
            player_y += player_speed
    
    player_y = max(player_radius, min(player_y, 1000 - player_radius))
    
    if ball_y > opponent_y + 10:
        opponent_y += player_speed * 0.6
    elif ball_y < opponent_y - 10:
        opponent_y -= player_speed * 0.6

    opponent_y = max(opponent_radius, min(opponent_y, 1000 - opponent_radius))
    
    screen.fill((0, 0, 0))

    colliders.clear()
    colliders.append({'pos': (player_x, player_y), 'radius': player_radius, 'is_paddle': True})
    colliders.append({'pos': (opponent_x, opponent_y), 'radius': opponent_radius, 'is_paddle': True})
    
    colliders.extend(obstacle_circles)

    for c in colliders:
        pygame.draw.circle(screen, white, (int(c['pos'][0]), int(c['pos'][1])), c['radius'])

    pygame.draw.circle(screen, red, (int(ball_x), int(ball_y)), ball_radius)

    if check_collisions():
        add_circle() 

    pygame.display.flip()

pygame.quit()