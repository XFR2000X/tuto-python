# Trois animaux font la course lequel des trois va gagner ?
# Le chat, le chien ou la tortue ?
# Réponse: chien
# Perdu ou Gagné
from random import shuffle
oui_non =input("tu veux jouer à un jeux oui ou non ? ")
if oui_non == 'oui':
    print("cool")
else:
    print("domage")
    quit()
mise = input("miser sur un animeaux chat,chien,tortue")
animaux=['chat','chien','tortue']
shuffle(animaux)
print('vous avez miser '+ mise + ' et '+ animaux[0]+ " a gagne")