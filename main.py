import pygame
from game import Game
import math

### initialisation :
pygame.init()

### définir une clock
clock = pygame.time.Clock()
FPS = 100

### générer la fenêtre du jeu :
pygame.display.set_caption("TOOSSA Game") #titre du jeu
screen = pygame.display.set_mode((1080, 720)) # dimension de la fenêtre

### charger l'arrière plan du jeu
background = pygame.image.load("assets/bg.jpg")

### importer charger notre bannière :
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) # pour arrondir le résultat de la division

# importer charger notre bouton pour lancer la partie :
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33 + 10)
play_button_rect.y = math.ceil(screen.get_height() / 2 )

### charger le jeu :
game = Game()

### pour maintenir la fenêtre allumée
running = True
# boucle tant cette condition est vérifiée :
while running:
    # appliquer l'arrière plan :
    screen.blit(background, (0,-200)) # (0,-200) pour qu'elle soit au centre

    # vérifier si notre jeu a commencé
    if game.is_playing :
        # déclencher les instructions de la partie
        game.update(screen)
    # vérifier si le jeu n'a pas commencé :
    else :
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'arrière plan :
    pygame.display.flip()

    # controler l'appui sur les touches
    for event in pygame.event.get() :
        # vérifier que le bouton quitter est appuyé
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            print("fermeture de fenêtre")
        # détecter si un joueur appuye sur un bouton
        elif event.type == pygame.KEYDOWN :
            game.pressed[event.key] = True
            # Détecter si le joueur appui sur espace pour lancer un projectile
            if event.key == pygame.K_SPACE :
                if game.is_playing :
                    game.player.launch_projectile()
                else :
                    # lancer le jeu :
                    game.start()
                    # jouer le son :
                    game.sound_manager.play("click")

        elif event.type == pygame.KEYUP :
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification pour savoir si la souris est en collision avec le bouton 'play'
            if play_button_rect.collidepoint(event.pos) :
                # lancer le jeu :
                game.start()
                # jouer le son :
                game.sound_manager.play("click")
    # fixer le nombre de FPS sur ma Clock
    clock.tick(FPS)
