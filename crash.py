import pygame

# 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Example")

# 색상
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rect 객체 생성
player = pygame.Rect(100, 100, 50, 50)  # x, y, width, height
obstacle = pygame.Rect(300, 200, 50, 50)

# 속도
speed = 5

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키보드 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # 충돌 처리
    if player.colliderect(obstacle):
        print("Collision detected!")

    # 화면 그리기
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, obstacle)

    # 화면 업데이트
    pygame.display.flip()