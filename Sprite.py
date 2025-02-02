import pygame

screen_width = 400
screen_height = 500

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
FPS = 60

background_color = pygame.Color('white')


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, position):
        super(AnimatedSprite, self).__init__()

        size = (80, 80)  # 화면 크기에 맞는 이미지 크기

        # 이미지 리스트 초기화
        images = []
        for i in range(1, 11):
            image_path = f'images/png/Attack{i}.png'
            try:
                image = pygame.image.load(image_path).convert_alpha()
                images.append(pygame.transform.scale(image, size))
            except pygame.error:
                print(f"Unable to load image: {image_path}")
                quit()

        self.images = images
        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(position, size)

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]


def main():
    player = AnimatedSprite(position=(100, 100))

    all_sprites = pygame.sprite.Group(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        all_sprites.update()

        screen.fill(background_color)

        all_sprites.draw(screen)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main()
