# coding: utf8
# chargement des fonctionnalité d'image ainsi que de low et high
from stegano import *



def decoder_with_params(bit, image, final_path):
    # charge le fichier
    size, image = image_load(image)

    # crée une nouvelle image de résultat
    result = image_new(size)

    for i in range(len(image)):
        lsb = low(image[i], bit)
        shifted = lsb * (2 ** (8 - bit))  # on décale les 4 bytes de point faible vers les forts
        result[i] = high(shifted, bit)
    image_save(result, size, final_path)


decoder_with_params(7,'exercices/message_x.png','resultat.png')


