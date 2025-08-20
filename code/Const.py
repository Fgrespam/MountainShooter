import pygame


# C
C_ORANGE =(255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1 # Evento personalizado para spawn de inimigos
EVENT_TIMEOUT = pygame.USEREVENT + 2 # Evento personalizado para timeout do level
ENTITY_SPEED = { # Velocidade de cada entidade
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level2Bg4': 4,
    'Player1'  : 3,
    'Player1Shot': 3, # Tiro do jogador 1
    'Player2'  : 3,
    'Player2Shot': 3, # Tiro do jogador 2
    'Enemy1'   : 1,
    'Enemy1Shot': 5, # Tiro do inimigo 1
    'Enemy2'   : 1,
    'Enemy2Shot': 2, # Tiro do inimigo 2
}

ENTITY_DAMAGE = { # Dano de cada entidade
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1'  : 1, # se a nave do jogador colidir com algo, ela causa 1 de dano
    'Player1Shot': 25, # Tiro do jogador 1
    'Player2'  : 1,
    'Player2Shot': 20, # Tiro do jogador 2
    'Enemy1'   : 1, # se a nave do inimigo colidir com algo, ela causa 1 de dano
    'Enemy1Shot': 20, # Tiro do inimigo 1
    'Enemy2'   : 1,
    'Enemy2Shot': 15, # Tiro do inimigo 2
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
}

ENTITY_HEALTH = { # Vida de cada entidade
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
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
PLAYER_KEY_SHOOT = {'Player1': pygame.K_LCTRL, # Jogador 1 usa CTRL esquerdo para atirar
                    'Player2': pygame.K_RALT} # Jogador 2 usa ALT direito para atirar

# S
SPAWN_TIME = 4000 # Tempo em milissegundos para spawn de inimigos

 # T
TIMEOUT_STEP = 100 # Tempo em milissegundos para o evento de timeout do level
TIMEOUT_LEVEL = 20000  # Tempo em milissegundos para o timeout do level (20 segundos)

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }