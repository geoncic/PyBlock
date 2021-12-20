class Constants(object):
    BLOCK_SIZE = 10
    BALL_SIZE = BLOCK_SIZE
    BOARD_HEIGHT = 800
    BOARD_WIDTH = 800
    PLAYER_WIDTH = 200
    SCREEN_HEIGHT = BOARD_HEIGHT
    SCREEN_WIDTH = BOARD_WIDTH + 2*PLAYER_WIDTH
    BRICK_TEAMS = {'RED': 'red_block_20x20.png',
                   'GREEN': 'green_block_20x20.png',
                   'BLUE': 'blue_block_20x20.png',
                   'YELLOW': 'yellow_block_20x20.png'}
    BALL_TEAMS = {'RED': (150, 0, 0),
                  'GREEN': (0, 150, 0),
                  'BLUE': (0, 0, 150),
                  'YELLOW': (150, 150, 0)}
    TEAMS = {'YELLOW': ((PLAYER_WIDTH+BOARD_WIDTH-0.05*BOARD_WIDTH), (BOARD_WIDTH-0.05*BOARD_WIDTH)),
             'RED': ((PLAYER_WIDTH+0.05*BOARD_WIDTH), (0.05*BOARD_WIDTH)),
             'GREEN': ((PLAYER_WIDTH+0.05*BOARD_WIDTH), (BOARD_WIDTH-0.05*BOARD_WIDTH)),
             'BLUE': ((PLAYER_WIDTH+BOARD_WIDTH-0.05*BOARD_WIDTH), (0.05*BOARD_WIDTH))}
    FILL = 1
    COLS = int(BOARD_WIDTH // BLOCK_SIZE)
    ROWS = int(COLS * FILL)
    ANG_COEF = 1
    DELAY = 5
    AMMO = 0
