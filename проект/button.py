import pygame


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        if outline:
            pygame.draw.rect(screen, outline, (self.x, self.y, self.width + 4, self.height + 4), 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font_menu = pygame.font.SysFont('kristenitc', 60)
            text = font_menu.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isover(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
