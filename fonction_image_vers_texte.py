import easyocr

# une fonction qui s'apelle image_vers_texte
# en paramètre de la fonction : le chemin vers l'image
# en sortie le texte
def image_vers_texte(chemin_fichier_image):
    print(chemin_fichier_image)
    lecteur = easyocr.Reader(['fr', 'en'])
    texte = lecteur.readtext(chemin_fichier_image, detail=0, paragraph=True)
    # recolle les paragraphes de la liste texte en un seul champ texte
    texte = "\r\n".join(texte)
    return texte

toto = image_vers_texte('poesie.jpg')
print(toto)