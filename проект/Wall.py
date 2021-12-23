import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        wall_pixels = pygame.image.load('anim/wall_plesen.png')

        for i in range(0, 1000, 70):
            self.image.blit(wall_pixels, (i, 0))
        for i in range(0, 1000, 70):
            self.image.blit(wall_pixels, (0, i))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
