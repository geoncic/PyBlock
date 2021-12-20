import pygame


class Buttons(object):
    def __init__(self, all_sprites, all_buttons):
        self.all_sprites = all_sprites
        self.all_buttons = all_buttons

        red_pos = (50, 100)
        blue_pos = (1050, 100)
        green_pos = (50, 600)
        yellow_pos = (1050, 600)
        width = 100
        height = 50
        text = "Test"

        red_button1 = Button(text, width, height, red_pos, "RED")
        blue_button1 = Button(text, width, height, blue_pos, "BLUE")
        yellow_button1 = Button(text, width, height, yellow_pos, "YELLOW")
        green_button1 = Button(text, width, height, green_pos, "GREEN")

        self.all_sprites.add(red_button1)
        self.all_buttons.add(red_button1)

        self.all_sprites.add(blue_button1)
        self.all_buttons.add(blue_button1)

        self.all_sprites.add(yellow_button1)
        self.all_buttons.add(yellow_button1)

        self.all_sprites.add(green_button1)
        self.all_buttons.add(green_button1)


class Button(pygame.sprite.Sprite):
    def __init__(self, text, width, height, pos, team):
        super().__init__()
        self.text = text
        self.color = team
        self.rect = pygame.Rect(pos, (width, height))
        self.top_color = '#444444'
        self.file = 'button.png'
        self.image = pygame.image.load('assets/' + self.file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))

    def update(self, all_players):
        # Update player button with player ammo
        for p in all_players:
            if self.color == p.color:
                self.text = str(p.ammo)
            else:
                pass
