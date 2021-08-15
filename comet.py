import pygame
import random
from monster import Mummy, Alien

# créer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # définir l'image associée à cette comette :
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3) # vitesse du comette
        self.rect.x = random.randint(20, 800)
        self.rect.y = -  random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son :
        self.comet_event.game.sound_manager.play("meteorite")

        # vérifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets) == 0:
            print("evenement fini")
            # remettre la barre à 0
            self.comet_event.reset_percent()
            # apparaitre les 3 premiers monstres:
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)

    def fall(self):
        self.rect.y += self.velocity
        # détruire la comette après le sol :
        if self.rect.y >= 500 :
            print('sol')
            # retirer la boule de feu
            self.remove()
            # s'il n'y a plus de boule de feu
            if len(self.comet_event.all_comets) == 0 :
                # remettre la jauge au départ
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False


        # vérifier si la boule de feu touche la joueur :
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print('joueur touché')
            # retirer la boule de feu
            self.remove()
            # subir des dégats :
            self.comet_event.game.player.damage(5)
