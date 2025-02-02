import pygame

# 화면 크기
screen_width = 400
screen_height = 500

# 중력 가속도 (픽셀/초^2)
GRAVITY = 0.5
JUMP_STRENGTH = -10  # 점프 강도

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60

background_color = pygame.Color('white')

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        # 초기화
        self.size = (80, 80)
        self.rect = pygame.Rect(position, self.size)
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False  # 바닥에 있는지 여부

        # 애니메이션 이미지 로드
        self.animations = {
            "walk_right": self.load_images('png/Walk', 10),
            "walk_left": [pygame.transform.flip(img, True, False) for img in self.load_images('png/Walk', 10)],
            "go_up": self.load_images('png/Jump', 10)
        }

        # 기본 이미지 설정 (애니메이션의 첫 번째 프레임)
        self.image = self.animations["walk_right"][0]
        self.animation_index = 0  # 애니메이션의 현재 프레임을 추적할 변수 추가
        self.animation_speed = 0.1  # 애니메이션 속도 조정 (프레임 전환 시간)
        self.animation_timer = 0  # 애니메이션 전환 타이머

    def load_images(self, base_path, count):
        """이미지 리스트 로드 및 크기 조정"""
        images = []
        for i in range(1, 11):
            image_path = f"png/Walk{i}.png"
            try:
                image = pygame.image.load(image_path).convert_alpha()
                images.append(pygame.transform.scale(image, self.size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()
        return images

        for i in range(11, 21):
            image_path = f"png/Jump{i}.png"
            try:
                image = pygame.image.load(image_path).convert_alpha()
                images.append(pygame.transform.scale(image, self.size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()
        return images

    def update(self, dt):
        """애니메이션 및 이동 업데이트 (물리 적용)"""
        # 중력 적용
        if not self.on_ground:
            self.velocity_y += GRAVITY  # 중력에 의한 속도 증가

        # 이동
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        # 바닥에 충돌 처리
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height  # 바닥에 닿으면 고정
            self.velocity_y = 0  # 속도를 0으로 하여 멈춤
            self.on_ground = True  # 바닥에 있음을 표시
        else:
            self.on_ground = False  # 바닥에 없으면 False

        # 애니메이션 프레임 업데이트
        self.animation_timer += dt  # 시간 누적
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0  # 타이머 초기화
            self.animation_index += 1  # 애니메이션 프레임 증가
            if self.animation_index >= len(self.animations["walk_right"]):  # 마지막 프레임에 도달하면 처음으로 돌아감
                self.animation_index = 0
            if self.animation_index >= len(self.animations["go_up"]):  # 마지막 프레임에 도달하면 처음으로 돌아감
                self.animation_index = 0
        
        # 애니메이션 변경
        if self.velocity_x > 0:  # 오른쪽으로 이동 시
            self.image = self.animations["walk_right"][self.animation_index]
        elif self.velocity_x < 0:  # 왼쪽으로 이동 시
            self.image = self.animations["walk_left"][self.animation_index]
    
    def jump(self):
        """점프 기능"""
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH  # 점프 강도로 위로 속도 설정

    def draw_ground(self, surface):
        """캐릭터가 밟을 초록색 땅을 그린다"""
        ground_rect = pygame.Rect(0, self.rect.bottom, screen_width, screen_height - self.rect.bottom)
        pygame.draw.rect(surface, (0, 255, 0), ground_rect)

    def move_left(self):
        """왼쪽으로 걷는 애니메이션"""
        self.velocity_x = -5
        self.animation_index = 0  # 걷기 애니메이션의 첫 번째 프레임으로 초기화

    def move_right(self):
        """오른쪽으로 걷는 애니메이션"""
        self.velocity_x = 5
        self.animation_index = 0  # 걷기 애니메이션의 첫 번째 프레임으로 초기화

    def stop(self):
        """이동 정지"""
        self.velocity_x = 0
        self.animation_index = 0  # 멈췄을 때 첫 번째 프레임으로 설정
    
    def move_up(self):
        self.image = self.animations["go_up"][self.animation_index]
        self.animation_index = 0

def main():
    # 스프라이트 초기화
    player = AnimatedSprite(position=(100, 100))
    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # 밀리초 단위로 시간 계산

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # 키 입력 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()

                elif event.key == pygame.K_RIGHT:
                    player.move_right()

                elif event.key == pygame.K_UP:
                    player.jump()  # 점프

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.stop()  # 이동 정지

        # 업데이트 및 렌더링
        all_sprites.update(dt)
        screen.fill(background_color)
        player.draw_ground(screen)  # 초록색 땅 그리기
        all_sprites.draw(screen)
        pygame.display.update()

if __name__ == "__main__":
    main()
