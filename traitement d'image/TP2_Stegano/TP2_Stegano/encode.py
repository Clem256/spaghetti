# coding: utf8
from stegano import *



def encode_with_params(bit, message, mask, final_path):
    size, message = image_load(message)
    size2, mask = image_load(mask)
    result = image_new(size)
    for i in range(len(message)):
        mask_msb = high(mask[i], 8 - bit)
        message_msb = high(message[i], bit)
        message_lsb = message_msb // 2**(8 - bit)
        result[i] = mask_msb + message_lsb
    image_save(result, size, final_path)

encode_with_params(7, 'message.jpg','mask.jpg' ,'resultat.png')
# sauvegarde l'image
