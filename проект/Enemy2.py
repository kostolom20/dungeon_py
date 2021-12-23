import pygame


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, enemy_image2, enemy_location2, enemy_speed2):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image2
        self.speed = enemy_speed2
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = enemy_location2

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top > 550 or self.rect.top < 200:
            self.speed[1] = -self.speed[1]
