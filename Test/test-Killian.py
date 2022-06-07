import json
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement

gedcom_parser = Parser()
file_path = '../Database/Queen_Eliz_II.ged'
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

        # Add links between people
        # Start by creating the links dictionnary that will contain all links for one person

        bdd_i['links'] = {}
        links = bdd_i['links']

        # Adding ascending parental links

        parents = gedcom_parser.get_parents(element)
        count = 0

        if len(parents) != 0:

            while len(parents) > 0:
                 parent = parents[0]
                 parent = str(parent).split()[1]
                 links[f'parent_{count + 1}'] = parent
                 count += 1
                 parents.pop(0)

        # Adding descending parental links

        families = gedcom_parser.get_families(element)
        count = 0

        if len(families) > 0:

            for family in families:
                elements = family.get_child_elements()
                for family_members in family.get_child_elements():
                    if family_members.get_tag() == 'CHIL':
                        links[f'child_{count + 1}'] = str(family_members).split()[2]

# ---------- #
# parameters for the calculus graph

alpha = 1.

# bdd_calculus

bdd_calculus = {}

for key, value in bdd.items():

    bdd_calculus[key] = {}
    links = bdd_calculus[key]

    for relation_type, linked_person in value['links'].items():

        if 'parent' in relation_type:
            links[linked_person] = {'type' : 'parent', 'length' : alpha}

        if 'child' in relation_type:
            links[linked_person] = {'type' : 'child', 'length' : alpha}


path_dbb_content = "../Database/database_conversion.json"
python_file = open(path_dbb_content, "w+")
json.dump(bdd, python_file)
python_file.close()

path_dbb_calculus = "../Database/database_calculus.json"
bdd_calculus_file = open(path_dbb_calculus, "w+")
json.dump(bdd_calculus, bdd_calculus_file)
python_file.close()

