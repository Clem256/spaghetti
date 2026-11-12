import math
import random
from PIL import Image, ImageEnhance
import numpy
import matplotlib
matplotlib.use('TkAgg')

path='C:\\Users\\User\\Downloads\\'
filename='Cellules_de_sang_humain_au_microscope_optique.jpg'



#Read image
image = Image.open( path+filename )
#Read pixels
pixels = image.load()

# image size
size = image.size
print("Taille de l'image (largeur,heuteur): "+str(size))

data=[]
for x in range(size[0]):
    for y in range(size[1]):
        data.append(pixels[x, y][1])  # pour Histogramme
        R = pixels[x, y][0] # Couleur Rouge
        V = pixels[x, y][1] # Couleur Verte
        B = pixels[x, y][2] # Couleur Bleu
        pixels[x, y] = (B,V,R)

# Affiche l'image
image.show()
# Enregictre l'image
image.save(path +'Save.png', "PNG")


def nuance_de_gris(img):
    for x in range(size[0]):
        for y in range(size[1]):
            data.append(pixels[x, y][1])  # pour Histogramme
            B = pixels[x, y][2]  # Couleur Bleu
            pixels[x, y] = (B, B, B)
    img.show()

def show_black_white(img, seuil):
    for x in range(size[0]):
        for y in range(size[1]):
            data.append(pixels[x, y][1])  # pour Histogramme
            B = pixels[x, y][2]  # Couleur Bleu

            if B > seuil:
                B = 255
            else:
                B = 0

            pixels[x, y] = (B, B, B)
    img.show()

def show_negative_value(img):
    for x in range(size[0]):
        for y in range(size[1]):
            data.append(pixels[x, y][1])  # pour Histogramme
            R = pixels[x, y][0]  # Couleur Rouge
            V = pixels[x, y][1]  # Couleur Verte
            B = pixels[x, y][2]  # Couleur Bleu
            B = 255 - B
            R = 255 - R
            V = 255 - V
            pixels[x, y] = (R, V, B)
    img.show()

def contraste_gris(img):
    for x in range(size[0]):
        for y in range(size[1]):
            data.append(pixels[x, y][1])  # pour Histogramme
            B = pixels[x, y][2]  # Couleur Bleu
            B = (B-30)*255
            B = B/(120-30)
            B= int(B)
            pixels[x, y] = (B, B, B)
    img.show()




def flou_uniforme(img, r=7):
    src = img.copy()

    for x in range(size[0]):
        for y in range(size[1]):
            sumR = sumV = sumB = 0
            nb = 0

            for i in range(-r, r + 1):
                for j in range(-r, r + 1):
                    nb += 1
                    sumR += pixels[x+i, y+1][0]
                    sumV += pixels[x + i, y + 1][1]
                    sumB += pixels[x+i, y+1][2]
            result[x,y]=(sumR/nb, sumV/nb, sumB/nb)
    img.show()

def flou_non_uniforme(img, r=7):
    src = img.copy()

    for x in range(size[0]):
        for y in range(size[1]):
            sumR = sumV = sumB = 0
            nb = 0

            for i in range(-r, r + 1):
                for j in range(-r, r + 1):
                    coef = math.exp(-2*(i**2+j**2))
                    nb += coef
                    sumR += pixels[x+i, y+1][0] * coef
                    sumV += pixels[x + i, y + 1][1] * coef
                    sumB += pixels[x+i, y+1][2] * coef
            result[x,y]=(sumR/nb, sumV/nb, sumB/nb)
    img.show()

def bruiter_image(amplitude=255, pourcentage=50):
    for x in range(size[0]):
        for y in range(size[1]):
            if random.random() < pourcentage / 100:
                R = random.randint(0, amplitude)
                V = random.randint(0, amplitude)
                B = random.randint(0, amplitude)
                pixels[x, y] = (R, V, B)
    image.show()



def debruiter_image(seuil=150):
    copie = image.copy().load()

    for x in range(size[0]):
        for y in range(size[1]):

            voisins = []

            for i in range(-1, 1):
                for j in range(-1, 1):
                    nx = x + i
                    ny = y + j

                    if 0 <= nx < size[0] and 0 <= ny < size[1]:
                        if not (i == 0 and j == 0):
                            voisins.append(copie[nx, ny])

            if voisins:
                moyR = sum(v[0] for v in voisins) / len(voisins)
                moyV = sum(v[1] for v in voisins) / len(voisins)
                moyB = sum(v[2] for v in voisins) / len(voisins)

                R, V, B = copie[x, y]
                diff = abs(R - moyR) + abs(V - moyV) + abs(B - moyB)
                if diff > seuil:
                    pixels[x, y] = (int(moyR), int(moyV), int(moyB))
    image.show()

def compter_cellule():
    nuance_de_gris(image)
    show_negative_value(image)
    image.show()

# nuance_de_gris(image)
# show_black_white(image, 128)
#show_negative_value(image)
#contraste_gris(image)
#flou_uniforme(image)
#bruiter_image(100, 50)
#debruiter_image()

compter_cellule()
# Ouvre dans un tableau 3D l'image [Ligne][Colonne][Couleur]
pix = numpy.array(image)

# Pixel Rouge(0) en position 0,0
print(pix[0][0][0])
print(pixels[0,0][0])

# Création d'une nouvelle image et l'affiche
newimage = Image.fromarray(pix)
newimage.show()





# Affiche un Histogramme
import matplotlib.pyplot as plt
plt.hist(data,range=(0,255),bins=256)
plt.show()