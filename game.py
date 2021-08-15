import pygame.sprite
from comet_event import CometFallEvent
from player import Player
from monster import Mummy, Alien
from sounds import SoundManager

### créer le jeu :
class Game :
    def __init__(self):
        # définir si notre joueur à commencer à jouer ou non :
        self.is_playing = False
        # génerer noter joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # génerer l'évenement
        self.comet_event = CometFallEvent(self)
        # groupe de monstres
        self.all_monsters = pygame.sprite.Group()
        # mettre le score à 0
        self.score = 0
        self.font = pygame.font.Font("assets/my_font.ttf", 25)
        #gérer le son
        self.sound_manager = SoundManager()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        # remetter le jeu à neuf : retirer les monstres + remettre le joueur à 100 de vie + lancement du jeu + retirer les comettes
        ### retirer les monstres :
        self.all_monsters = pygame.sprite.Group()
        ### remettre le joueur à 100 de vie :
        self.player.health = self.player.max_health
        ### lancement du jeu
        self.is_playing = False
        ### retirer les comettes
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        ### mise à zero du nbre de score
        self.score = 0
        # jouer le son :
        self.sound_manager.play("game_over")

    def add_score(self, points=10):
        self.score += points

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image de mon joueur :
        screen.blit(self.player.image, (self.player.rect))

        # appliquer l'image des projectiles :
        self.player.all_projectiles.draw(screen)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser l'animation
        self.player.update_animation()

        # actualiser la barre d'évenement :
        self.comet_event.update_bar(screen)

        # déplacer les projectiles du joueur :
        for projectile in self.player.all_projectiles:
            projectile.move()

        # déplacer les monstres dans le jeu :
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # récuperer les comets de notre jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'image des monstres :
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de comettes :
        self.comet_event.all_comets.draw(screen)

        # vérifier si le joueur souhaite aller vers la droite ou à gauche
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    # pour vérifier les collisions entre les monstres et notre joueur :
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))