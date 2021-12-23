import pygame


class Enemy1(pygame.sprite.Sprite):
    def __init__(self, enemy_image1, enemy_location1, enemy_speed1):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_image1
        self.speed = enemy_speed1
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = enemy_location1

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.top > 430 or self.rect.top < 120:
            self.speed[1] = -self.speed[1]
