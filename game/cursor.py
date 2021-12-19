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
        self.pos = pygame.mouse.get_pos()

    def update(self):
        self.pos = pygame.mouse.get_pos()
        print(self.pos)