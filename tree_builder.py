import json
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

gedcom_parser = Parser()

file_path = '../Database/Queen_Eliz_II.ged'
gedcom_parser.parse_file(file_path, False)

# Essai de la construction de la BDD

bdd = {}
root_child_elements = gedcom_parser.get_root_child_elements()
count_people = 0

# Iterate through all root child elements
for element in root_child_elements:

    if isinstance(element, IndividualElement):

        count_people += 1

        # creation of a dictionnary for the Individual

        id_person = str(element).split()[1]
        bdd[f"{id_person}"] = {}

        # Filling the dictionnary of the individual

        bdd_i = bdd[f"{id_person}"]
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

                        child = str(family_members).split()[2]

                        if child not in links.values():

                            links[f'child_{count + 1}'] = child
                            count += 1

                        if str(family_members).split()[2] not in bdd.keys():

                            bdd[str(family_members).split()[2]] = {'name': None, 'links': {}}

import tree_analyser

tree_analyser.tree_linker(bdd)
graph_calculus = tree_analyser.graph_calulator(bdd)



def saver_base(data, name):

    path_dbb_content = f"../Database/{name}.json"
    python_file = open(path_dbb_content, "w+")
    json.dump(data, python_file)
    python_file.close()

saver_base(bdd, 'database_conversion')
saver_base(graph_calculus, 'database_calculus')
