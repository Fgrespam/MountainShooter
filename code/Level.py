#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 segundos
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []  # List to hold entities in the level
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Set a timer for the timeout
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP) #100ms para o evento de timeout
        #MENU_OPTION

    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3') # musica de fundo
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60) # Limit de fps
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()  # Verifica se o jogador ou inimigo atirou
                    if shoot is not None: # Se shoot não for None, significa que o jogador ou inimigo atirou
                        self.entity_list.append(shoot) # adiciona o tiro na lista de entidades
                if ent.name == 'Player1':
                    self.level_text(14, f'Payer1 - Health: {ent.health} | Score: {ent.score}', C_GREEN, (10, 25))  # Mostra a vida do player1 na tela
                if ent.name == 'Player2':
                    self.level_text(14, f'Payer1 - Health: {ent.health} | Score: {ent.score}', C_CYAN, (10, 45))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice('Enemy1 Enemy2'.split()) # Escolhe aleatoriamente um inimigo
                    self.entity_list.append(EntityFactory.get_entity(choice))  # adiciona inimigo1
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP # Diminui o tempo de timeout
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True  # Retorna para o menu se o tempo acabar

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True


                if not found_player:
                    return False


            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f} s', C_WHITE, (10, 5)) # Mostra o tempo em segundos na tela
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35)) # Mostra o fps na tela
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20)) # Mostra o numero de entidades na tela
            pygame.display.flip()
            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)# checa colisões entre entidades
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)  # Draw the text on
