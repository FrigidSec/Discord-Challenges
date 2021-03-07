import os
import random

flag = "// NOT SO EASY, HOMIE //"
enc_char = ''
key = []
with open('out.enc', 'w') as wf:
    for i in range(13):
        key.append(random.randint(0,100))
    for char_ind in range(len(flag)):
        enc_char += str(ord(flag[char_ind]) ^ key[char_ind % 13]) + ' '
    print ("CIPHER : ", enc_char)
    wf.write(enc_char)

