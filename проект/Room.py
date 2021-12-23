import pygame

class Room(object):
    wall_list = None
    enemy_sprites = None
    all_text = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.all_text = pygame.sprite.Group()