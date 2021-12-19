import pygame
from constants import Constants


def check_collision(balls, bricks):
    for b in balls:
        col_brick = pygame.sprite.spritecollide(b, bricks, False)
        for i in col_brick:
            if i.color == b.color:
                pass
            else:
                # Change color of collided brick
                # print(b.__dict__)
                i.color = b.color
                i.file = Constants.BRICK_TEAMS[i.color]
                i.image = pygame.image.load('assets/' + i.file).convert_alpha()
                i.image = pygame.transform.scale(i.image, (Constants.BLOCK_SIZE, Constants.BLOCK_SIZE))
                pygame.sprite.Sprite.kill(b)
    else:
        pass
