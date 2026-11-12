# Créé par Veronique, le 29/11/2024 en Python 3.7
import pygame
from random import randint
from pygame.locals import *
from Cellule import Cellule
from tkinter import Tk, messagebox

class Grille:
    def __init__(self,size,cellules_size, nbcell, nbmines,screen):
        self.size=size
        self.cells_size=cellules_size
        self.nbcell=nbcell
        self.nbmines=nbmines
        self.cells=[[Cellule(x, y, cellules_size) for x in range(size)] for y in range(size)]
        self.mines_placees=False
        self.premier_clic=True
        self.surface=screen

    def afficherGrille(self):
        for row in self.cells:
            for cell in row:
                cell.draw(self.surface)

        for x in range(self.size+1):
            pygame.draw.line(self.surface, (0,0,0), (0,x*self.cells_size), (self.size * self.cells_size, x * self.cells_size))

        for y in range(self.size+1):
            pygame.draw.line(self.surface, (0,0,0), (y*self.cells_size,0), (y * self.cells_size, self.size * self.cells_size))

    def get_cell(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.cells[x][y]
        else:
            print("Indices hors de la grille!")
            return None  # Retourner None si les indices sont invalides

    def placer_mines(self,posx,posy):
        mines=self.nbmines
        while mines>0: # tant que toutes les mines ne sont pas placées
            x=randint(0, self.size-1)#-1 car tab donc indice débutant à 0
            y=randint(0, self.size-1)
            if (x,y)!=(posx, posy) and not self.cells[x][y].mined: # si jamais les cos des mines ne sont pas les mm que des endroits safes, alors on va placer la mine
                self.cells[x][y].mined=True #la cellule comporte donc une mine
                mines-=1 #on décrémente le nb de mines à placer

        #update des compteurs de mines proches
        for x in range(self.size):
            for y in range(self.size):
                self.cells[x][y].voisinnage=self.compte_mines_proches(x,y)
        if mines==0:
            print("mines placées !")

    def compte_mines_proches(self,x,y):
        return self.compte_mines_lignes(x,y)+self.compte_mines_col(x,y)+self.compte_mines_diag(x,y)

    def compte_mines_lignes(self,x,y):
        comptemines=0
        if x>0 and self.cells[x-1][y].mined: #gauche
            comptemines+=1
        if x<self.size-1 and self.cells[x+1][y].mined: #droite
            comptemines+=1
        return comptemines

    def compte_mines_col(self,x,y):
        comptemines=0
        if y>0 and self.cells[x][y-1].mined: #dessus
            comptemines+=1
        if y<self.size-1 and self.cells[x][y+1].mined: #dessous
            comptemines+=1
        return comptemines

    def compte_mines_diag(self,x,y):
        comptemines=0
        if x>0 and y>0 and self.cells[x-1][y-1].mined: #diagonale haut gauche
            comptemines+=1
        if x>0 and y<self.size-1 and self.cells[x-1][y+1].mined: #haut droite
            comptemines+=1
        if x<self.size-1 and y>0 and self.cells[x+1][y-1].mined: #bas gauche
            comptemines+=1
        if x<self.size-1 and y<self.size-1 and self.cells[x+1][y+1].mined: #bas droite
            comptemines+=1
        return comptemines

    def reveler_cell(self, x, y):
        """
        Révèle une cellule donnée. Sur le premier clic, si c'est une mine, les mines sont replacées.
        """
        # Si c'est la première révélation, vérifiez les mines
        if self.premier_clic and self.cells[x][y].mined:
            self.premier_clic = False
            print("Premier clic sur une mine, on replace les mines")
            # S'assure qu'aucune mine n'est dans la zone 3x3 autour du premier clic
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < self.size and 0 <= j < self.size:
                        self.cells[i][j].mined = False  # Retirer toutes les mines de la zone

            self.placer_mines(x, y)  # Reset du placement des mines hors de la zone

            # Révéler toutes les cellules de la zone 3x3
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < self.size and 0 <= j < self.size:
                        self.reveler_cell(i, j)  # Révéler les cellules de la zone
            return

        # Révéler la cellule
        self.cells[x][y].revealed = True

        if self.cells[x][y].mined:
            # Si une mine est révélée après le premier clic, terminer la partie
            self.cells[x][y].charger_bombe(self.surface)
            self.fin_partie()
        else:
            # Sinon, afficher le nombre de mines proches
            self.cells[x][y].set_nb_mines(self.compte_mines_proches(x, y))
            self.cells[x][y].draw_mines_around(self.surface)  # Afficher le nombre de mines proches


    def reveler_adjacent(self, x, y):
        """
        Révèle toutes les cases adjacentes non minées et leurs voisines si elles n'ont pas de mines autour.
        Lors du premier clic, cette méthode est utilisée pour tout révéler autour de la case, si possible.
        """
        a_traiter = [(x, y)]  # Commencer par la cellule actuelle
        cases_revelees = set()  # Pour éviter de traiter plusieurs fois la même cellule

        while a_traiter:
            cx, cy = a_traiter.pop()

            # Vérifiez que les coordonnées sont valides et que la case n'est pas déjà révélée
            if 0 <= cx < self.size and 0 <= cy < self.size and not self.cells[cx][cy].revealed:
                self.reveler_cell(cx, cy)  # Révéler la cellule actuelle
                cases_revelees.add((cx, cy))  # Marquer la cellule comme révélée

                # Si la cellule a un voisinage nul, révéler toutes ses voisines (sauf les mines)
                if self.cells[cx][cy].voisinnage == 0:
                    for i in range(cx - 1, cx + 2):  # -1, 0, +1 pour les voisins horizontaux
                        for j in range(cy - 1, cy + 2):  # -1, 0, +1 pour les voisins verticaux
                            if 0 <= i < self.size and 0 <= j < self.size:
                                if (i, j) not in cases_revelees and not self.cells[i][j].mined:
                                    a_traiter.append((i, j))  # Ajouter à la pile si ce n'est pas une mine

                # Si la cellule a un voisinage non nul, on ne révèle pas ses voisins
                if self.cells[cx][cy].voisinnage > 0:
                    continue  # Passer à la cellule suivante sans explorer ses voisins



    def marquer(self, x, y):
        # On va marquer ou retirer le drapeau sur la cellule
        if not self.cells[x][y].revealed:  # Si la cellule n'est pas révélée
            if self.cells[x][y].flagged:
                # Si elle est déjà marquée, on la retire
                self.cells[x][y].unmark(self.surface)
                print("Drapeau retiré !")
            else:
                # Sinon, on la marque avec un drapeau
                self.cells[x][y].mark(self.surface)
                print("Drapeau placé !")


    def verif_victoire(self):
        pass

    def fin_partie(self):
        tk = Tk()
        tk.withdraw()
        messagebox.showinfo("Game over", "you discovered a bomb !")
        tk.destroy()
