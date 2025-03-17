import random
from random import shuffle

word = input("ajouter des mots de la forme mot1/mot2/mot3...").split("/")
print(word)
shuffle(word)
print(word)
word_len = len(word)
if word_len<10 :
    print(word[0],word[1])
else:
    print(word[word_len-1],word[word_len-2],word[word_len-3])



# animaux = [ 'chat', 'chien', 'veau', 'aigle', 'pigeon' ]
# shuffle(animaux)
# print(animaux[0])
# nbre_animaux = len(animaux)
# print(nbre_animaux)
# print(animaux[1])
# print(animaux[-1])
# animaux += ['vautour', 'ver']
# print(animaux)