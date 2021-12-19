import pygame
import pygame.gfxdraw
import time
from constants import Constants



class Balls(object):
    def __init__(self, all_sprites, all_balls):
        self.all_sprites = all_sprites
        self.all_balls = all_balls

    def spawn_ball(self, pos, vel, team):
        ## Todo: Figure out how to spawn multiple balls with some sort of delay
        ball = Ball(pos, vel, team)
        self.all_sprites.add(ball)
        self.all_balls.add(ball)

    def ball_test(self):
        print("This is a Ball Test!")
        print(self)

    def update(self):
        print(self.__dict__)
        print(type(self))


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, vel, team):
        super().__init__()

        self.color = team
        self.file = Constants.BALL_TEAMS[self.color]
        self.rad = int(Constants.BALL_SIZE/2)
        self.image = pygame.Surface([Constants.BALL_SIZE, Constants.BALL_SIZE], pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.file, (self.rad, self.rad), self.rad)

        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.dx = vel[0]
        self.dy = vel[1]

    def update(self):
        self.check_boundary()
        self.x_pos += self.dx
        self.y_pos += self.dy
        self.rect.center = [self.x_pos, self.y_pos]
        # self.rect.center = pygame.mouse.get_pos() # has sprite follow the mouse

    def check_boundary(self):
        if not Constants.PLAYER_WIDTH <= self.x_pos <= (Constants.PLAYER_WIDTH+Constants.BOARD_WIDTH):
            self.dx = -1*self.dx

        if not 0 <= self.y_pos <= Constants.SCREEN_HEIGHT:
            self.dy = -1*self.dy
