from random import choice
from string import ascii_letters , digits
import os
import sys

cuantas = 1
caracteres = ascii_letters + digits
def generatePassword(ab):
    for i in range(ab):
        final = ''.join([choice (caracteres) for i in range(4,16)])
        print (final)
generador(cuantas)
