import sys

def decrypt(text,step):

    result = ""

    for i in range(len(text)):
        char = text[i]
        if not char.isalpha(): #verif lettre
            result += char
        elif char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65) #majuscules
        else:
            result += chr((ord(char) + s - 97) % 26 + 97) #minuscules
        return result

message_chiffre1 = open("message-chiffre.txt","r")
message_chiffre2 = open("message-chiffre","w")