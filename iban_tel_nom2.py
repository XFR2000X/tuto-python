import easyocr
import re
import spacy
from sympy import false


# une fonction qui s'apelle image_vers_texte
# en paramètre de la fonction : le chemin vers l'image
# en sortie le texte
def image_vers_texte(chemin_fichier_image):
    print(chemin_fichier_image)
    lecteur = easyocr.Reader(['fr', 'en'])
    texte = lecteur.readtext(chemin_fichier_image, detail=0, paragraph=True)
    # recolle les paragraphes de la liste texte en un seul champ texte
    texte = " ".join(texte)
    return texte

# une fonction qui s'apelle cherche_iban
# en paramètre de la fonction : le texte dans lequel chercher
# en sortie True si il trouve sinon False
def cheche_iban(texte):
    paterne = r'AL\d{10}[0-9A-Z]{16}|AD\d{10}[0-9A-Z]{12}|AT\d{18}|BH\d{2}[A-Z]{4}[0-9A-Z]{14}|BE\d{14}|BA\d{18}|BG\d{2}[A-Z]{4}\d{6}[0-9A-Z]{8}|HR\d{19}|CY\d{10}[0-9A-Z]{16}|CZ\d{22}|DK\d{16}|FO\d{16}|GL\d{16}|DO\d{2}[0-9A-Z]{4}\d{20}|EE\d{18}|FI\d{16}|FR\d{12}[0-9A-Z]{11}\d{2}|GE\d{2}[A-Z]{2}\d{16}|DE\d{20}|GI\d{2}[A-Z]{4}[0-9A-Z]{15}|GR\d{9}[0-9A-Z]{16}|HU\d{26}|IS\d{24}|IE\d{2}[A-Z]{4}\d{14}|IL\d{21}|IT\d{2}[A-Z]\d{10}[0-9A-Z]{12}|[A-Z]{2}\d{5}[0-9A-Z]{13}|KW\d{2}[A-Z]{4}22!|LV\d{2}[A-Z]{4}[0-9A-Z]{13}|LB\d{6}[0-9A-Z]{20}|LI\d{7}[0-9A-Z]{12}|LT\d{18}|LU\d{5}[0-9A-Z]{13}|MK\d{5}[0-9A-Z]{10}\d{2}|MT\d{2}[A-Z]{4}\d{5}[0-9A-Z]{18}|MR13\d{23}|MU\d{2}[A-Z]{4}\d{19}[A-Z]{3}|MC\d{12}[0-9A-Z]{11}\d{2}|ME\d{20}|NL\d{2}[A-Z]{4}\d{10}|NO\d{13}|PL\d{10}[0-9A-Z]{,16}n|PT\d{23}|RO\d{2}[A-Z]{4}[0-9A-Z]{16}|SM\d{2}[A-Z]\d{10}[0-9A-Z]{12}|SA\d{4}[0-9A-Z]{18}|RS\d{20}|SK\d{22}|SI\d{17}|ES\d{22}|SE\d{22}|CH\d{7}[0-9A-Z]{12}|TN59\d{20}|TR\d{7}[0-9A-Z]{17}|AE\d{21}|GB\d{2}[A-Z]{4}\d{14}'
    texte_sans_espace = texte.replace(" ", "")
    resultat = re.findall(paterne, texte_sans_espace)
    # si resultat est vide alors retourner False
    if len(resultat) == 0:
        return False
    # sinon
    else:
        return True


def cherche_telephone(texte):
    paterne = r'[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}'
    texte_sans_espace = texte.replace(" ", "")
    resultat = re.findall(paterne, texte_sans_espace)
    if len(resultat) == 0:
        return False
    else:
        return True

def cherche_nom(texte):
    # python - m spacy download fr_core_news_lg
    nlp = spacy.load("fr_core_news_lg")
    doc = nlp(texte)
    noms = []
    ner_categories = ["PER"]
    for token in doc.ents:
        print((token.text, token.label_))
        if token.label_ in ner_categories:
            noms.append(token.text)
    if len(noms) == 0:
        return False
    else:
        return True
def numero_compte(texte):
    patern = r'[^\d]\d{11}[^\d]'
    texte_sans_espace = texte.replace(" ", "")
    resultat = re.findall(patern, texte_sans_espace)
    if len(resultat) == 0:
        return False
        # sinon
    else:
        return True



texte_de_l_image = image_vers_texte('numero_de_compte.png')
print(texte_de_l_image)
trouve_iban = cheche_iban(texte_de_l_image)
print(trouve_iban)
trouve_telephone= cherche_telephone(texte_de_l_image)
print(trouve_telephone)
trouve_nom=cherche_nom(texte_de_l_image)
print(trouve_nom)
trouver_compte=numero_compte(texte_de_l_image)
print(trouver_compte)