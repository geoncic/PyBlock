import pygame

from ball import Balls
from brick import Bricks
from player import Players
from constants import Constants
from collision import check_collision


class Game(object):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(size=(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color('grey')
        self.game_over = False

        self.all_sprites = pygame.sprite.Group()
        self.all_balls = pygame.sprite.Group()
        self.all_bricks = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()


        self.balls = Balls(self.all_sprites, self.all_balls)
        self.bricks = Bricks(self.all_sprites, self.all_bricks)
        self.players = Players(self.all_sprites, self.all_players)


    def reset(self):
        pass

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()


        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_pos, y_pos = pygame.mouse.get_pos()
                # Test if mouseclick is in board area
                if (Constants.PLAYER_WIDTH <= x_pos <= (Constants.PLAYER_WIDTH+Constants.BOARD_WIDTH)):
                    # pos = [x_pos, y_pos]
                    # Create a random direction and speed for newly spawned balls

                    # angle = random.uniform(math.pi*-1, math.pi)
                    # dy = math.sin(angle * math.pi / 2)*10
                    # dx = math.cos(angle * math.pi / 2)*10
                    # vel = [dx, dy]
                    # self.balls.spawn_ball(pos, vel)

                    # Spawn ball in direction of player cannon
                    # Note: If I try to 'count' multiple balls in this loop, every ball will spawn with the same pos,vel
                    for player in self.all_players:
                        if player.team == "RED":
                            if event.button == 3:
                                player.ammo += 10
                            # else:
                            #     pass
                            #
                            if event.button == 1:
                                player.fire = True
                            else:
                                pass
                        else:
                            pass

                    # for player in self.all_players:
                    #     pos = [player.x_pos, player.y_pos]
                    #     angle = player.angle
                    #     dy = -math.cos(math.radians(angle)) * 10
                    #     dx = -math.sin(math.radians(angle)) * 10
                    #     vel = [dx, dy]
                    #     # print(player.team)
                    #
                    #     self.balls.spawn_ball(pos, vel, player.team)

                    # count = 10
                    # bullet_event = pygame.USEREVENT + 1
                    # delay = 500
                    # while count > 0:
                    #     count -= 1
                    #     print(count)
                    #     pygame.time.set_timer(bullet_event,delay)
                    #     for player in self.all_players:
                    #         pos = [player.x_pos, player.y_pos]
                    #         angle = player.angle
                    #         dy = -math.cos(math.radians(angle))*10
                    #         dx = -math.sin(math.radians(angle))*10
                    #         vel = [dx, dy]
                    #         # print(player.team)
                    #
                    #         self.balls.spawn_ball(pos, vel, player.team)
                else:
                    pass

    def update(self):
        # Check Ball to Boundary, and update velocity
        # Check Ball to Brick collision, Update brick state, kill ball
        # ...I JUST realized. I don't need to check where the ball collides
        # with a brick because it doesn't change direction. it DIES!
        # Update sprites..ie, move?
        # self.balls.update(self.all_balls)

        pygame.display.update()
        check_collision(self.all_balls, self.all_bricks)

        # self.all_bricks.update()
        self.all_balls.update()
        self.all_players.update(self)
        self.clock.tick(100)



    def draw(self):
        self.screen.fill(self.bg_color)
        if self.game_over:
            pass
        else:
            self.all_bricks.draw(self.screen)
            self.all_balls.draw(self.screen)
            self.all_players.draw(self.screen)
