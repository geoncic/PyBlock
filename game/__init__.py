import pygame

from cursor import Cursors
from ball import Balls
from brick import Bricks
from player import Players
from button import Buttons
from constants import Constants
from collision import check_collision, check_click

pygame.init()
gui_font = pygame.font.Font(None, 30)


class Game(object):
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(size=(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color('grey')
        self.game_over = False

        self.all_sprites = pygame.sprite.Group()
        self.cursor = pygame.sprite.Group()
        self.all_balls = pygame.sprite.Group()
        self.all_bricks = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.all_buttons = pygame.sprite.Group()

        self.cursors = Cursors(self.all_sprites, self.cursor)
        self.balls = Balls(self.all_sprites, self.all_balls)
        self.bricks = Bricks(self.all_sprites, self.all_bricks)
        self.players = Players(self.all_sprites, self.all_players)
        self.buttons = Buttons(self.all_sprites, self.all_buttons)

    def reset(self):
        pass

    def handle_events(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                button_click = check_click(self.cursor, self.all_buttons)

                if button_click:
                    for p in self.all_players:
                        if event.button == 3:
                            if p.color == button_click:
                                p.ammo += 10
                            else:
                                pass
                        if event.button == 1:
                            if p.color == button_click:
                                p.fire = True
                            else:
                                pass
                    print(button_click)
                else:
                    pass

    def update(self):
        pygame.display.update()
        check_collision(self.all_balls, self.all_bricks)

        # self.all_bricks.update()
        self.all_balls.update()
        self.all_players.update(self)
        self.all_buttons.update(self.all_players)
        self.cursor.update()
        self.clock.tick(100)

    def draw(self):
        self.screen.fill(self.bg_color)
        if self.game_over:
            pass
        else:
            self.all_bricks.draw(self.screen)
            self.all_balls.draw(self.screen)
            self.all_players.draw(self.screen)
            self.all_buttons.draw(self.screen)
            # Draw text on buttons
            for b in self.all_buttons:
                b.text_surf = gui_font.render(b.text, True, '#FFFFFF')
                b.text_rect = b.text_surf.get_rect(center=b.rect.center)
                self.screen.blit(b.text_surf, b.text_rect)
