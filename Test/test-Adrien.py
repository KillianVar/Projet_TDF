from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement

import json
import tree_manager


gedcom_parser = Parser()
file_path = 'Queen_Eliz_II.ged'
gedcom_parser.parse_file(file_path, False)


# Essai de la construction de la BDD

bdd = {}
root_child_elements = gedcom_parser.get_root_child_elements()

# Iterate through all root child elements
for element in root_child_elements:
    
    if isinstance(element, IndividualElement):

        # creation of a dictionnary for the Individual

        id = str(element).split()[1]
        bdd[f"{id}"] = {}

        # Filling the dictionnary of the individual

        bdd_i = bdd[f"{id}"]
        name, surname = element.get_name()
        bdd_i["name"] = name
        bdd_i["surname"] = surname
        bdd_i["gender"] = element.get_gender()
        parents = gedcom_parser.get_parents(element)
        if len(parents) != 0:
            bdd_i["father"] = str(parents[0]).split()[1]
            if len(parents) !=1:
                bdd_i["mother"] = str(parents[1]).split()[1]

        print(bdd)

        # Lets inspect this element :

        # his gender, birth, death and age :

        gender = element.get_gender()
        if gender == "M":
            pronoun = ["He", "His"]
        else:
            pronoun = ["She", "Her"]

        name, surname = element.get_name()

        #print(50 * '-')
        #print(f'{name} {surname}')

        #if element.is_deceased():
            #print(f'{pronoun[0]} was born on {element.get_birth_data()[0]} and died on {element.get_death_data()}.')
        #else:
            #print(f'{pronoun[0]} was born on {element.get_birth_data()[0]} and is still alive !')

        try:
            parents = gedcom_parser.get_parents(element)
            parent_name = []
            for parent in parents:
                parent_name.append(parent.get_name())
            if len(parents) == 2:
                #print(f'{pronoun[1]} '
                f'parents are {parent_name[0][0]} {parent_name[0][1]} and {parent_name[1][0]} {parent_name[1][1]}.'
        except ValueError:
            pass


# Ajout des photos comme nouvelles relations

# Description du problème : un individu étant très proche socialement d'un autre individu sans que leur
# position dans l'arbre soit proche doivent être reconnus par l'algorithme

# Solution proposée : se fonder sur les photos de famille sur lesquelles sont identifiés les individus
# Plus deux individus ont d'occurences - photo, plus leur distance va diminuer

# Exemple précis : individu qui n'a pas été élevé par ses parents mais par sa tante


# entrée : dictionnaire relatif à l'individu {'@I...@' : 'nbre occurences'}

# fonctionnement général : notre petit algorithme prend en entrée le dictionnaire d'occurences, puis vient
# modifier la distance entre les individus en fonction de cette occurence.

dict_occur_I521 = {"@I521@" : {"@I431@": 5, "@I432@": 3, "@I392@": 1, "@I6456@": 2}}

def photo_occur_detector(dict_occur):

# ouverture de l'ancienne base de données

    file_calculus = open('./Database/database_calculus.json')
    calculus = json.load(file_calculus)
    file_relations = open('./Database/database_conversion.json')
    relations = json.load(file_relations)
    individual = list(dict_occur.keys())[0]
    dict_occur_inside = dict_occur.values()

    dict_indi = relations[f'@{individual}@']
    dict_calculus = calculus[f'@{individual}@']

    for people in dict_occur_inside.keys():

        if people in dict_calculus.keys():

            new_dist = (1/dict_occur_inside[f"{people}"]) * dict_calculus[f"{people}"]
            dict_calculus[f"{people}"] = new_dist

        else:

            dict_link = dict_indi["links"]
            dict_link["photo_relation"] = people    # ajout de la nouvelle relation

            dict_calculus[f"{people}"] = 5 * (1/dict_occur_inside[f"{people}"])

    tree_manager.saver_base(relations, 'database_conversion')  # enregistrement en écrasant l'ancienne base
    tree_manager.saver_base(calculus, 'database_calculus')

photo_occur_detector(dict_occur_I521)