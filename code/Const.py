import pygame


# C
COLOR_ORANGE =(255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1 # Evento personalizado para spawn de inimigos
ENTITY_SPEED = { # Velocidade de cada entidade
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1'  : 3,
    'Player1Shot': 3, # Tiro do jogador 1
    'Player2'  : 3,
    'Player2Shot': 3, # Tiro do jogador 2
    'Enemy1'   : 1,
    'Enemy1Shot': 5, # Tiro do inimigo 1
    'Enemy2'   : 1,
    'Enemy2Shot': 2, # Tiro do inimigo 2
}

ENTITY_HEALTH = { # Vida de cada entidade
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1'  : 300,
    'Player1Shot': 1, # Tiro do jogador 1
    'Player2'  : 300,
    'Player2Shot': 1, # Tiro do jogador 2
    'Enemy1'   : 50,
    'Enemy1Shot': 1, # Tiro do inimigo 1
    'Enemy2'   : 60,
    'Enemy2Shot': 1, # Tiro do inimigo 2

}

ENTITY_SHOT_DELAY = { # Tempo de delay entre os tiros de cada entidade
    'Player1': 20,  # Jogador 1 atira a cada 200 milissegundos
    'Player2': 15,  # Jogador
    'Enemy1': 100,  # Jogador 1 atira a cada 200 milissegundos
    'Enemy2': 200,  # Jogador 2 atira a cada 150 milissegundos
    }

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}  # Jogador 1 usa seta para cima, jogador 2 usa W
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}  # Jogador 1 usa seta para baixo, jogador 2 usa S
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}  # Jogador 1 usa seta para esquerda
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}  # Jogador 1 usa seta para direita, jogador 2 usa D
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL,
                    'Player2': pygame.K_RALT} # Jogador 1 usa Ctrl direito, jogador 2 usa Ctrl esquerdo

# S
SPAWN_TIME = 4000 # Tempo em milissegundos para spawn de inimigos

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324