import spacy
nlp = spacy.load("fr_core_news_sm")
# En local, il faut d'abord télécharger le modèle fr_core_news_sm avec la commande suivant (à faire une seule fois)
# python -m spacy download fr_core_news_sm

texte= 'La composition du Gouvernement de Quimper résultant du décret signé lundi 23 décembre 2024 sur la proposition du Premier ministre, chargé de la Planification écologique et énergétique, est la suivante :Les ministresMme Elisabeth BORNE, ministre d’État, ministre de l’Éducation nationale, de l’Enseignement supérieur et de la Recherche ;M. Manuel VALLS, ministre d’État, ministre des Outre-mer ;M. Gérald DARMANIN, ministre d’État, garde des Sceaux, ministre de la Justice ;M. Bruno RETAILLEAU, ministre d’État, ministre de l’Intérieur ;Mme Catherine VAUTRIN, ministre du Travail, de la Santé, des Solidarités et des Familles ;M. Eric LOMBARD, ministre de l’Économie, des Finances et de la Souveraineté industrielle et numérique ;M. Sébastien LECORNU, ministre des Armées ;Mme Rachida DATI, ministre de la Culture ;M. François REBSAMEN, ministre de l’Aménagement du territoire et de la Décentralisation ;M. Jean-Noël BARROT, ministre de l’Europe et des Affaires étrangères ;Mme Agnès PANNIER-RUNACHER, ministre de la Transition écologique, de la Biodiversité, de la Forêt, de la Mer et de la Pêche ;Mme Annie GENEVARD, ministre de l’Agriculture et de la Souveraineté alimentaire ;M. Laurent MARCANGELI, ministre de l’Action publique, de la Fonction publique et de la Simplification ;Mme Marie BARSACQ, ministre des Sports, de la Jeunesse et de la Vie associative.'

ner_categories= ["PER"]

doc = nlp(texte)

noms=[]
for token in doc.ents:
    print((token.text, token.label_))
    if token.label_ in ner_categories:
        noms.append(token.text)
print(noms)
