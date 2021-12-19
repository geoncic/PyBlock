import pygame
import pygame.gfxdraw

from game.constants import Constants


class Bricks(object):
    def __init__(self, all_sprites, all_bricks):
        self.all_sprites = all_sprites
        self.all_bricks = all_bricks
        self.create_brick()

    def update(self):
        pass

    def create_brick(self):
        for row in range(Constants.ROWS):
            # reset the block row list
            # iterate through each column in that row
            for col in range(Constants.COLS):
                # Set color based on position
                color = self.color_start(row, col)
                # generate x and y pos for each block and create a rectangle
                brick = Brick(row, col, color)

                self.all_sprites.add(brick)
                self.all_bricks.add(brick)

    @staticmethod
    # Create Tile Map based on four colors/players
    def color_start(row, col):
        block_y = row*Constants.BLOCK_SIZE
        block_x = col*Constants.BLOCK_SIZE

        if block_y <= Constants.BOARD_HEIGHT/2 and block_x <= Constants.BOARD_WIDTH/2:
            # color = Constants.TEAMS['RED']
            color = 'RED'
        elif block_y <= Constants.BOARD_HEIGHT/2 and block_x >= Constants.BOARD_WIDTH/2:
            # color = Constants.TEAMS['GREEN']
            color = 'GREEN'
        elif block_y >= Constants.BOARD_HEIGHT/2 and block_x <= Constants.BOARD_WIDTH/2:
            # color = Constants.TEAMS['BLUE']
            color = 'BLUE'
        elif block_y >= Constants.BOARD_HEIGHT/2 and block_x >= Constants.BOARD_WIDTH/2:
            # color = Constants.TEAMS['YELLOW']
            color = 'YELLOW'
        else:
            color = 'RED'
        return color


class Brick(pygame.sprite.Sprite):
    def __init__(self, row, col, team):
        super().__init__()
        self.width = Constants.BLOCK_SIZE
        self.height = Constants.BLOCK_SIZE
        # set color as image file name
        self.color = team
        self.file = Constants.BRICK_TEAMS[self.color]
        # print(self.color)
        self.x_pos = Constants.PLAYER_WIDTH+row*self.width
        self.y_pos = col*self.height
        self.image = pygame.image.load('assets/'+self.file).convert_alpha()
        # Scale the image based on BLOCK_SIZE
        self.image = pygame.transform.scale(self.image, (Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))
        # Create Rect
        self.rect = pygame.Rect(self.x_pos, self.y_pos, self.width, self.height)

        self.rad = int(Constants.BALL_SIZE/2)
