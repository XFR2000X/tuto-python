from random import shuffle
oui_non =input("tu veux jouer à un jeux oui ou non ? ")
if oui_non == 'oui':
    print("cool")
else:
    print("domage")
    quit()
mise = input("miser sur un animeaux chat,chien,tortue: ")
animaux=['chat','chien','tortue']
shuffle(animaux)
if mise==animaux [0]:
    print("vous avez gagnez")
else:
    print("vouz avez perdu car c'est "+animaux[0]+ ' qui a gagné')