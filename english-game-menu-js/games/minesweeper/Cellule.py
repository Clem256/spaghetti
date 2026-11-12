# Créé par Veronique, le 29/11/2024 en Python 3.7
import pygame
from pygame.locals import *

class Cellule:
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.revealed=False
        self.flagged=False
        self.mined=False
        self.voisinnage=0
        self.font=pygame.font.Font(None, 40)
        self.rect=pygame.Rect(x*size,y*size,size,size) #it's a square so same dimension for height and width
        self.color=(128,128,128)
        self.colors=[(0,255,0),(0,0,255),(255,0,0),(163,74,232),(78,183,141),(194,200,3),(222,116,3),(237,93,242)]

    def draw(self, surface):
        if self.revealed:
            if self.mined:
                pygame.draw.rect(surface, (255, 0, 0), self.rect)  # Couleur de fond de la case rouge si c'est une mine -> fin de game
            if not self.mined or self.flagged:
                pygame.draw.rect(surface, (200, 255, 200), self.rect)  # Même chose mais en vert clair si c'est une case safe
                if self.voisinnage > 0:
                    text = self.font.render(str(self.voisinnage), True, self.colors[self.voisinnage - 1])  # Police + couleur du texte
                    surface.blit(text, (self.rect.x + 10, self.rect.y + 10))
        else:
            # Si la cellule n'est pas révélée et qu'elle est marquée, afficher le drapeau
            if self.flagged:
                try:
                    flag = pygame.image.load("minesweeper/red-flag.png")
                    flag = pygame.transform.scale(flag, (self.size, self.size)).convert_alpha()
                    surface.blit(flag, (self.rect.x, self.rect.y))
                except pygame.error:
                    print("Erreur de chargement de l'image 'red-flag.png'")
            else:
                pygame.draw.rect(surface, self.color, self.rect)  # Dessine la cellule sans drapeau si elle n'est pas marquée


    def click(self):
        if not self.flagged and not self.mined:
            self.revealed=True

    def mark(self, screen):
    # Si jamais la case n'a pas été révélée
        if not self.revealed:
            self.flagged = True  # Mettre un drapeau
            try:
                flag = pygame.image.load("minesweeper/red-flag.png")
                flag = pygame.transform.scale(flag, (self.size, self.size)).convert_alpha()
                screen.blit(flag, (self.x * self.size, self.y * self.size))
                pygame.display.update()
                print("drapeau placé !")
            except pygame.error:
                print("Erreur de chargement de l'image 'flag.png'")


    def unmark(self,surface):
        #si jamais la case n'a pas été révélée
        if not self.revealed:
            self.flagged=False
            self.draw(surface)
            pygame.display.update()
            print("drapeau retiré !")

    def charger_bombe(self, screen):
        bomb=pygame.image.load("minesweeper/bombe.png")
        bomb=pygame.transform.scale(bomb, (self.size, self.size)).convert_alpha()
        screen.blit(bomb,(self.x*self.size,self.y*self.size))
        pygame.display.update()

    def draw_mines_around(self, screen):
        if self.voisinnage>0 and self.voisinnage<=len(self.colors):
            color=self.colors[self.voisinnage-1]
        else:
            color=self.color
        text=self.font.render(str(self.voisinnage), True, color)
        screen.blit(text, text.get_rect(center=self.rect.center))

    def set_nb_mines(self, nbmines):
        self.voisinnage=nbmines

    def reveal(self):
        if not self.flagged:
            self.revealed=True
            return self.mined
        return False


