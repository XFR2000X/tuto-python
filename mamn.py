from random import shuffle
musique_list = input('insérez 4 musique pour la semaine sous la forme m1/m2/m3/m4 ')
musique=musique_list.split("/")
shuffle(musique)
print("lundi "+musique[0]+ ' Mardi '+ musique [1]+" Jeudi " + musique[2]+ " Vendredi "+musique[3])
