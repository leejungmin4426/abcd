import pygame

#물리법칙(중력) 적용하기, 땅(초록색) 만들기, walk_jump2, 3차이점 문서로 정리해보기, 깃허브에 png 제외하고 업로드하기

screen_width = 400
screen_height = 500

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FPS = 60

background_color = pygame.Color('white')


class Sprite:
    def __init__(self, position):

        size = (80, 80)  # 화면 크기에 맞는 이미지 크기

        # 이미지 리스트 초기화
        stays = []
        for i in range(1, 11):
            image_path = f'png/Idle{i}.png'
            try:
                image = pygame.image.load(image_path).convert_alpha()
                stays.append(pygame.transform.scale(image, size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()

        walks = []
        for i in range(1, 11):
            image_path = f'png/Walk{i}.png'
            try:
                image = pygame.image.load(image_path).convert_alpha()
                walks.append(pygame.transform.scale(image, size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()
        
        jumps = []
        for i in range(1, 11):
            image_path = f'png/Jump{i}.png'
            try:
                image = pygame.image.load(image_path).convert_alpha()
                jumps.append(pygame.transform.scale(image, size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()
        
        self.animations={

        }
        self.images_idle_right=stays
        self.images_idle_left=[pygame.transform.flip(image, True, False) for image in stays]

        self.images_walk_right=walks
        self.images_walk_left[pygame.transform.flip(image, True, False) for image in walks]

        self.images_jump_right=jumps
        self.images_jump_left[pygame.transform.flip(image, True, False) for image in jumps]
        
        self.state=0
        #0:stay, 1:walk, 2:jump
        self.direction='right'

        self.velocity_x=0
        self.velocity_y=0

        self.index = 0

        if not self.images_idle_right:
            raise ValueError("self.images_right가 비어 있습니다. 이미지 로드에 실패했을 가능성이 있습니다.")

        self.image = self.images_idle_right[self.index]
        # 애니메이션 시간 계산

        self.animation_time = round(100 / len(self.images_idle_right), 2)

        self.current_time = 0
        # rect 초기화

        if not (isinstance(position, tuple) and len(position) == 2):
            raise ValueError("position은 (x, y) 형식의 튜플이어야 합니다.")
            
        self.rect = pygame.Rect(position, size)

#///////////////////////////////////////////////////////

        if not self.images_walk_right:
            raise ValueError("self.images_right가 비어 있습니다. 이미지 로드에 실패했을 가능성이 있습니다.")

        self.image = self.images_walk_right[self.index]
        # 애니메이션 시간 계산

        self.animation_time = round(100 / len(self.images_walk_right), 2)

        self.current_time = 0
        # rect 초기화

        if not (isinstance(position, tuple) and len(position) == 2):
            raise ValueError("position은 (x, y) 형식의 튜플이어야 합니다.")
            
        self.rect = pygame.Rect(position, size)

#/////////////////////////////////////////////////////////////////

        if not self.images_jump_right:
            raise ValueError("self.images_right가 비어 있습니다. 이미지 로드에 실패했을 가능성이 있습니다.")

        self.image = self.images_jump_right[self.index]
        # 애니메이션 시간 계산

        self.animation_time = round(100 / len(self.images_jump_right), 2)

        self.current_time = 0
        # rect 초기화

        if not (isinstance(position, tuple) and len(position) == 2):
            raise ValueError("position은 (x, y) 형식의 튜플이어야 합니다.")
            
        self.rect = pygame.Rect(position, size)

#///////////////////////////////////////////////////////////////////////

    def update(self):
        self.index += 1

        if self.index >= len(self.images_right):
            self.index = 0
        self.image = self.images_right[self.index]

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.sprite = Sprite(position)  # Sprite 객체를 사용
        # pygame.sprite.Sprite에서 요구하는 self.image와 self.rect 설정
        self.image = self.sprite.image
        self.rect = self.sprite.rect
        
    def update(self):
        self.sprite.update()
        self.image = self.sprite.image
        self.rect = self.sprite.rect

def main():
    player = AnimatedSprite(position=(100, 100))

    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.direction = "right"
                    player.state = 1

                elif event.key == pygame.K_LEFT:
                    player.direction = "left"
                    player.state = 1
                    
                elif event.key == pygame.K_UP:
                    player.direction = "right"
                    player.state = 2

                elif event.key == pygame.K_UP:
                    player.direction = "left"
                    player.state = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity_x = 0
                    player.state = 0

        all_sprites.update()

        screen.fill(background_color)

        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
