import sys

def decrypt(text,step):

    result = ""

    for i in range(len(text)):
        char = text[i]
        if not char.isalpha(): #verif lettre
            result += char
        elif char.isupper():
            result += chr