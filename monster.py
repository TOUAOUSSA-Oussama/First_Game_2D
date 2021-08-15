import pygame
import random
import animation
###créer le monstre dans mon jeu
class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size) # important lorsqu'il y a héritage
        self.game = game
        self.health = 80 # les points de vie du monstre
        self.max_health = 80
        self.attack_player = 0.05 # points de dégats du joueur
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.velocity = random.randint(1, 3) # vitesse de déplacement d'un pixel
        self.start_animation()
        self.loot_amount  = 10

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def damage(self, amount):
        # Infliger les dégâts :
        self.health -= amount
        # vérifier si le monstre a encore de points de vie :
        if self.health <= 0:
            # reapparaître comme étant un nouveau monstre :
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = self.default_speed
            self.health = self.max_health
            # ajouter des points au score
            self.game.add_score(self.loot_amount)

            # si la barre d'évenement est chargé à son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)
                # déclencher la pluie des cometes :
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # dessiner l'arrière plan de la bar de vie :
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        # dessiner la bar de vie :
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x+10, self.rect.y-20, self.health, 5])

    def forward(self):
        # déplacement que s'il y' a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le joueur est en contact avec le monstre
        else :
            # infliger des dégats
            self.game.player.damage(self.attack_player)

# définir une classe de la momie :
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)

# définir une classe pour l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.attack = 0.8
        self.max_health = 250
        self.set_speed(1)
        self.loot_amount = 20