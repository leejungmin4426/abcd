import pygame

pygame.init()

# Initial position and size of the ball
ball = pygame.Rect(400 // 2 - 16 // 2, 300 // 2 - 16 // 2, 16, 16)

# Ball speed and movement directions
ball_speed_x = 0
ball_speed_y = 0
to_x = 0
to_y = 0

# Create the screen
screen = pygame.display.set_mode((400, 300))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game loop

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x = -2
            elif event.key == pygame.K_RIGHT:
                to_x = 2
            if event.key == pygame.K_UP:
                to_y = -2
            elif event.key == pygame.K_DOWN:
                to_y = 2

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0  # Stop horizontal movement
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0  # Stop vertical movement

    # Update the ball's speed
    ball_speed_x = to_x
    ball_speed_y = to_y

    # Move the ball by updating its position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Fill the screen with a color (black in this case)
    screen.fill((0, 0, 0))

    # Draw the ball (a red rectangle)
    pygame.draw.rect(screen, (0, 0, 255), ball)

    # Update the screen display
    pygame.display.flip()

    # Set the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
