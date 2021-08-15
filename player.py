import pygame
from projectile import Projectile
import animation

### créer une classe pour présenter notre joueur :
class Player(animation.AnimateSprite):

     def __init__(self, game):
         super().__init__("player")
         self.game = game
         self.max_health = 100 # max des points de vie
         self.health = 100 # les points de vie
         self.attack = 0.5 # le dommage (damage)
         self.velocity = 4 # vitesse de déplacement = 1 pixels
         self.image = pygame.image.load("assets/player.png") # l'image du joueur
         self.rect = self.image.get_rect() # les coordonnées du joueur
         self.rect.x = 400
         self.rect.y = 500
         self.all_projectiles = pygame.sprite.Group()

     def damage(self, amount):
         if self.health - amount > amount :
            self.health -= amount
         else:
             # si le joueur n'a plus de points de vie :
             self.game.game_over()

     def update_animation(self):
         self.animate()

     def update_health_bar(self, surface):
         # dessiner l'arrière plan de la bar de vie :
         pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
         # dessiner la bar de vie :
         pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

     def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        # démarrer l'animation :
        self.start_animation()
        # jouer le son :
        self.game.sound_manager.play("tir")

     def move_right(self):
         # vérifier s'il n'est pas en collision avec un monstre
         if not self.game.check_collision(self, self.game.all_monsters) :
             self.rect.x += self.velocity

     def move_left(self):
         self.rect.x -= self.velocity