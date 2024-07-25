# Example file showing a circle moving on screen
import random
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
enemy = pygame.sprite.Sprite

player1_pos = pygame.Vector2(screen.get_width() / random.uniform(1.2, 2), screen.get_height() / random.uniform(1.2, 2))
player2_pos = pygame.Vector2(screen.get_width() / random.uniform(1.2, 2), screen.get_height() / random.uniform(1.2, 2))
enemy_post = pygame.Vector2(screen.get_width() / random.uniform(1.2, 2), screen.get_height() / random.uniform(1.2, 2))

# Create an instance of the Enemy

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")



    pygame.draw.circle(screen, "blue", player1_pos, 40)
    pygame.draw.circle(screen, "green", player2_pos, 20)
    pygame.sprite.Sprite()

    keys = pygame.key.get_pressed()

    # Define movement speeds
    normal_speed = 300
    slow_speed = 1

    # Determine the current speed based on whether SPACE is pressed
    current_speed = slow_speed if keys[pygame.K_SPACE] else normal_speed

    # Player 1 movement
    if keys[pygame.K_w]:
        player1_pos.y -= current_speed * dt
    if keys[pygame.K_s]:
        player1_pos.y += current_speed * dt
    if keys[pygame.K_a]:
        player1_pos.x -= current_speed * dt
    if keys[pygame.K_d]:
        player1_pos.x += current_speed * dt

    # Player 2 movement (unchanged)
    if keys[pygame.K_w]:
        player2_pos.y += random.randint(1, 350) * dt
    if keys[pygame.K_s]:
        player2_pos.y -= random.randint(1, 350) * dt
    if keys[pygame.K_a]:
        player2_pos.x += random.randint(1, 350) * dt
    if keys[pygame.K_d]:
        player2_pos.x -= random.randint(1, 350) * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()