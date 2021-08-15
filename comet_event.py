import pygame
from comet import Comet

# créer une classe pour gérer cet évenement :
class CometFallEvent:
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 3
        # définir un groupe de comete:
        self.all_comets = pygame.sprite.Group()
        self.game = game
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # apparaitre 10 boules de feu :
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # fonctionne que si la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de comet")
            self.meteor_fall()
            self.fall_mode = True # activer l'évenement

    def update_bar(self, surface):
        # ajouter du pourcentage à la bar
        self.add_percent()

        # barre noir (en arrière plan)
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            surface.get_width(), # longueur de la fenêtre
            10 # l'épaisseur
        ])
        #barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # l'axe des x
            surface.get_height() - 20, # l'axe des y
            (surface.get_width()/100) * self.percent, # longueur de la fenêtre
            10 # l'épaisseur
        ])
