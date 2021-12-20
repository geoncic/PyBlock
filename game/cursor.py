import pygame


class Cursors(object):
    def __init__(self, all_sprites, cursor):
        self.all_sprites = all_sprites
        self.cursor = cursor
        self.create_cursor()

    def create_cursor(self):
        cursor = Cursor()
        self.all_sprites.add(cursor)
        self.cursor.add(cursor)


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 10
        self.height = 10
        self.pos = pygame.mouse.get_pos()
        self.x, self.y = self.pos
        self.rect = pygame.Rect(((self.x - self.width/2), (self.y - self.height/2)), (10, 10))

    def update(self):
        self.pos = pygame.mouse.get_pos()
