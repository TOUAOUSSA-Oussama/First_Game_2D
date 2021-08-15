import pygame
import random

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load('assets/'+sprite_name+'.png')
        self.image = pygame.transform.scale(self.image, self.size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    # definir une méthode pour démarrer l'animation :
    def start_animation(self):
        self.animation = True

    # définir une méthode pour animer le sprite
    def animate(self, loop=False):
        # vérifier si l'animation est active
        if self.animation:
            # passer à l'image suivante
            self.current_image += random.randint(0, 1)
            # vérifier si on attient la fin de l'animation:
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0
                # vérifier si l'animation n'est pas en mode boucle
                if not loop:
                    # désactiver l'animation
                    self.animation = False
            # modifier l'image précedante par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # charger les images du sprite_name dans le dossier correspond
    images = []
    # récupérer le chemin du dossier :
    path  = 'assets/'+sprite_name+'/'+sprite_name
    # boucler sur chaque image du dossier :
    for num in range(1, 25):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images

# définir un dictionnaire qui va contenir les images chargées, exple : mummy -> (mummy1.png, ...mummy23.png)...
animations = {
    'mummy' : load_animation_images("mummy"),
    'player' : load_animation_images("player"),
    'alien' : load_animation_images("alien")
}
