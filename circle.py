import pygame
ball=pygame.Rect(screen_width // 2-16 // 2, screen_height // 2-16 // 2, 16, 16)
ball_speed_x=5
ball_speed_y=-5

while True:
    clock.tick(30)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygamea.K_LEFT:
                paddle_dx=-5
            elif event.key == pygame.K_RIGHT:
                paddle_dx=5
        
        elif event.type == pygame.KEYUP:
            if event.key == pygamea.K_LEFT:
                paddle_dx=0
            elif event.key == pygame.K_RIGHT:
                paddle_dx=0

    paddle.left += paddle_dx