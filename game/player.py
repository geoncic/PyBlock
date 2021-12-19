import pygame
import pygame.gfxdraw
import math
from game.constants import Constants
from game.ball import Balls


class Players(object):
    def __init__(self, all_sprites, all_players):
        self.all_sprites = all_sprites
        self.all_players = all_players
        self.create_player()

    def update(self):
        pass

    def create_player(self):
            for p_team in Constants.TEAMS:
                # print(p_team)
                # self.pos = Constants.TEAMS[p_team]
                self.team = p_team
                player = Player(self.team)
                self.all_sprites.add(player)
                self.all_players.add(player)


class Player(pygame.sprite.Sprite):
    def __init__(self, team, ammo=0, fire=False):
        super().__init__()
        # set color as image file name
        self.pos = Constants.TEAMS[team]
        self.team = team
        self.ammo = ammo # Amount of bullets to fire when trigger
        self.fire = fire # Trigger state to fire bullets

        self.file = 'cannon_100px.png'
        self.image = pygame.image.load('assets/'+self.file).convert_alpha()
        # Scale the image based on BLOCK_SIZE
        self.image = pygame.transform.scale(self.image, (Constants.BLOCK_SIZE*5,Constants.BLOCK_SIZE*5))
        self.orig_image = self.image
        self.x_pos = self.pos[0]
        self.y_pos = self.pos[1]
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.angle = 0

    def fire_ammo(self, all):
        pos = [self.x_pos, self.y_pos]
        angle = self.angle
        dy = -math.cos(math.radians(angle)) * 10
        dx = -math.sin(math.radians(angle)) * 10
        vel = [dx, dy]

        Balls.spawn_ball(all, pos, vel, self.team)

    def update(self, all):
        # Have player cannons follow the mouse cursor position
        # mx, my = pygame.mouse.get_pos()
        # self.dx = mx - self.x_pos
        # self.dy = my - self.y_pos
        # self.angle = (180 / math.pi) * math.atan2(self.dx, self.dy) - 180
        # self.image = pygame.transform.rotate(self.orig_image, self.angle)
        # self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

        if self.angle > 360:
            self.angle = 0
        else:
            self.angle += 1

        if self.fire:
            if self.ammo:
                print("Fire!")
                self.ammo -= 1
                print(self.ammo)
                self.fire_ammo(all)
            else:
                print("Out of ammo!")
                print(self.ammo)
                self.fire = False


        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
