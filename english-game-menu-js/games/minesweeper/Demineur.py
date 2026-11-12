# Créé par Veronique, le 29/11/2024 en Python 3.7
import pygame
from pygame.locals import *
from Grille import Grille
from Cellule import Cellule
from random import randint
pygame.init()
grid_size=12 #size of the grid
cell_size=50 # size of the cells
mainscreen = pygame.display.set_mode((grid_size*cell_size,grid_size*cell_size))
background = pygame.Surface(mainscreen.get_size())
background.convert()
#initialisation de la grille
nbmines=randint(12, 24)
grille=Grille(grid_size, cell_size,grid_size*grid_size,nbmines, mainscreen)
grille.placer_mines(grille.size,grille.cells_size)
tries=0
running=True
while running:
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                coords=pygame.mouse.get_pos()
                print(coords)
                print(int(coords[0]/cell_size),int(coords[1]/cell_size))
                x,y = int(coords[1] / cell_size), int(coords[0] / cell_size)
                if 0<=x<=grille.size and 0<=y<=grille.size:
                    case_cliquee = grille.get_cell(x,y)
                    if not case_cliquee.revealed:
                        if tries==0:
                            grille.reveler_adjacent(x,y)
                            print("premier_clic !")
                        else:
                            grille.reveler_cell(x,y)
                    tries+=1
                else:
                    print("clic hors grille !")


            if event.button == 3:  # Clic droit pour poser ou retirer un drapeau
                coords = pygame.mouse.get_pos()
                x, y = int(coords[1] / cell_size), int(coords[0] / cell_size)
                if 0 <= x < grille.size and 0 <= y < grille.size:
                    case_cliquee = grille.get_cell(x, y)
                    if case_cliquee.flagged:
                        case_cliquee.unmark(mainscreen)  # Retirer le drapeau
                    else:
                        case_cliquee.mark(mainscreen)  # Poser le drapeau


    mainscreen.blit(background, (200,200))
    grille.afficherGrille()

    pygame.display.flip()
pygame.quit()
