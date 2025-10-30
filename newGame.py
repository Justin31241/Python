import pygame
import random



pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True

red = 255, 0, 0

#Physics
speed = 20
ball_speed = -speed / 6
ball_direction = "Left"
acceleration = 1.2
maxSpeed = 10
x = 0
y = 0
ball_x = 500
ball_y = 500


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60) 

    if ball_direction == "Left":
        distance = (((x - ball_x)**2) + ((y - ball_y)**2))**0.5
        radi_sum = (20 + 10)
        if distance <= radi_sum:
            ball_direction = "Right"
            ball_speed -= 1
    else:
        distance = ((((1000 + x) - ball_x)**2) + ((y - ball_y)**2))**0.5
        radi_sum = (20 + 10)
        if distance <= radi_sum:
            ball_direction = "Left"
            ball_speed -= 1


    if ball_direction == "Left":
        ball_x += ball_speed
    else:
        ball_x -= ball_speed

    keys = pygame.key.get_pressed()

    if keys != False:
        if keys[pygame.K_UP]:
            new_y = (y - speed)
            if new_y < 20:
                y = 20
            else:
                y -= speed
        elif keys[pygame.K_DOWN]:
            new_y = (y + speed)
            if new_y > 980:
                y = 980
            else:
                y += speed
    

    screen.fill((0, 0, 0))

    
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 20) #Player
    pygame.draw.circle(screen, (255, 255, 255), (1000 + x, y), 20) #Opponent
    pygame.draw.circle(screen, red, (ball_x, ball_y), 10) #Ball



    pygame.display.flip()

    

    

pygame.quit()

