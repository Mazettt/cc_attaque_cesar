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

try:
    f = open(sys.argv[1], 'r') #open message
    f1 = open("message-dechiffre.txt", 'w') #open message

    step = int(input("Entrez le nombre de décalage des lettres : "))
    text = f. ()
    f1. (encrypt(text, 26-step))
    f.close()
    f1.close()
    print("Le message chiffré est disponible sous le nom message-dechiffre.txt")

except Exception:
    print("Le fichier n'est pas existant.")

# PAS FINI