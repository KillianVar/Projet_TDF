import json
from math import exp
import tree_manager


# Ajout des photos comme nouvelles relations

# Description du problème : un individu étant très proche socialement d'un autre individu sans que leur
# position dans l'arbre soit proche doivent être reconnus par l'algorithme

# Solution proposée : se fonder sur les photos de famille sur lesquelles sont identifiés les individus
# Plus deux individus ont d'occurences - photo, plus leur distance va diminuer

# Exemple précis : individu qui n'a pas été élevé par ses parents mais par sa tante


# entrée : dictionnaire relatif à l'individu {'@I...@' : 'nbre occurences'}

# fonctionnement général : notre petit algorithme prend en entrée le dictionnaire d'occurences, puis vient
# modifier la distance entre les individus en fonction de cette occurence.

dict_occur_I101 = {"@I101@" : {"@I431@": 5, "@I432@": 3, "@I392@": 1, "@I6456@": 2}}

def photo_occur_detector(dict_occur):

# ouverture de l'ancienne base de données

    file_calculus = open('Database/database_queen/database_calculus.json')
    calculus = json.load(file_calculus)
    file_relations = open('Database/database_queen/database_conversion.json')
    relations = json.load(file_relations)
    individual = list(dict_occur.keys())[0]
    dict_occur_inside = list(dict_occur.values())[0]

    dict_indi = relations[f"{individual}"]
    dict_calculus = calculus[f"{individual}"]
    s = 0

    for value in dict_occur_inside.values():

        s += value

    for people in dict_occur_inside.keys():

        not_relation_count = 1

        # Il est nécessaire ici de différencier des liens déjà existants
        # ou bien des nouveaux liens que l'on va créer

        if people in dict_calculus.keys():

            new_dist = (exp(-2 * dict_occur_inside['people'] / s)) * dict_calculus[f"{people}"]
            dict_calculus[f"{people}"] = new_dist

        else:

            dict_link = dict_indi["links"]
            dict_link[f"photo_relation_{not_relation_count}"] = people    # ajout de la nouvelle relation

            dict_calculus[f"{people}"] = 5 * (exp(-2 * dict_occur_inside['people'] / s))

            not_relation_count += 1

    # enregistrement en écrasant l'ancienne base

    tree_manager.saver_base(relations, 'database_conversion')
    tree_manager.saver_base(calculus, 'database_calculus')

photo_occur_detector(dict_occur_I101)