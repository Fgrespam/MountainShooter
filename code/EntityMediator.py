from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):  # verifica se o entity esta dentro da janela
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):  # se o enemy sair da tela, sua vida vai para 0
            if ent.rect.left >= WIN_WIDTH:  # se o entity sair da tela, sua vida vai para 0
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False  # verifica se houve colisao entreos entities
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot):
            valid_interaction = True
        elif isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy):
            valid_interaction = True
        elif isinstance(ent1, Player) and isinstance(ent2, EnemyShot):
            valid_interaction = True
        elif isinstance(ent1, EnemyShot) and isinstance(ent2, Player):
            valid_interaction = True

        if valid_interaction:  # if valid_interaction: == True: mesma coisa
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and  # as quatro condiçoes verificam se houve colisao entre os entities
                    ent1.rect.bottom >= ent2.rect.top and  # as quatro perguntas que o professor fez
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage # se houve colisao, diminui a vida dos entities
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]): # metodo para dar score ao player quando um inimigo morre
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity]):  # verifica se houve colisao entre os entities
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):  #
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1,
                                                         entity2)  # verifica se houve colisao entre os entities

    @staticmethod
    def verify_health(entity_list: list[Entity]):  # verifica se o entity esta vivo
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list) # metodo para dar score ao player quando um inimigo morre
                entity_list.remove(ent)
