import pygame

# créer la classe qui va gérer les projectiles de mon joueur :
class Projectile(pygame.sprite.Sprite):
    # définir le constructeur de cette classe:
    def __init__(self, player):
        super().__init__()
        self.velocity = 1 #vitesse de déplacement = 1 pixel
        self.image = pygame.image.load("assets/projectile.png")
        self.image = pygame.transform.scale(self.image, (50, 50)) #pour réduire la taille du projectile
        self.rect = self.image.get_rect() # les coordonnées de l'image
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.player = player
        self.origin_image = self.image
        self.angle = 0
        self.attack = 25 # points de dégats du monster

    def rotate(self):
        # tourner le projectile
        self.angle += 4
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)  # self et pas projectile prq on est déjà dans la classe projectile

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # vérifier si le projectile entre en colision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters) :
            # supprimer le projectile :
            self.remove()
            # infliger les dégats :
            monster.damage(self.attack)

        # vérifier si le projectile n'est plus présent dans l'écran
        if self.rect.x > 1080 :
            # supprimer le projectile en dehors de l'écran
            self.remove()
