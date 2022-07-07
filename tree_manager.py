import json
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

def gedcom_converter(file_path):

    gedcom_parser = Parser()
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

                    for family_members in elements:

                        if family_members.get_tag() == 'CHIL':

                            child = str(family_members).split()[2]

                            if child not in links.values():
                                links[f'child_{count + 1}'] = child
                                count += 1

                            if str(family_members).split()[2] not in bdd.keys():
                                bdd[str(family_members).split()[2]] = {'name': None, 'links': {}}

    return bdd


def tree_linker(bdd):

    # Adding siblings :

    for person, person_data in bdd.items():

        sibling_count = 1

        if 'parent_1' in list(person_data['links'].keys()):

            parent_1 = person_data['links']['parent_1']

            for relation_type, related_person in bdd[parent_1]['links'].items():

                checker = ('child' in relation_type) and not ('grandchild' in relation_type)
                checker = checker and related_person is not person

                if checker:

                    bdd[person]['links'][f'sibling_{sibling_count}'] = related_person
                    sibling_count += 1




    # Starting by grandparents

    for person, person_data in bdd.items():

        links = person_data['links']
        links_copy = person_data['links'].copy()
        count_grandparent = 0

        for link_type, linked_person in links_copy.items():

            if 'parent' in link_type:

                parents = bdd[linked_person]['links']

                for secondary_linked_type, secondary_linked_person in parents.items():

                    checker = 'parent' in secondary_linked_type and secondary_linked_person not in links.keys()
                    checker = checker and 'grand' not in secondary_linked_type

                    if checker:

                        links[f'grandparent_{count_grandparent + 1}'] = secondary_linked_person

                        count_grandparent += 1


    # adding grandchildren

    for grandchildren, grandchildren_data in bdd.items():

        links = grandchildren_data['links']
        links_copy = links.copy()

        for link_type, linked_person in links_copy.items():

            if 'grandparent' in link_type:

                grandparent_links = bdd[linked_person]['links']

                n_grand_children = 0

                for relation_grandchildren in grandparent_links.keys():

                    if 'grandchildren' in relation_grandchildren :

                        n_grand_children += 1

                grandparent_links[f'grandchildren_{n_grand_children + 1}'] = grandchildren


    # Adding aunts / uncles

    for grandparent, grandparent_data in bdd.items():

        grandparent_links = grandparent_data['links']
        links_copy = grandparent_links.copy()

        for link_type, linked_person in links_copy.items():

            if 'grandchildren' in link_type:

                grandchildren = linked_person

                aunt_counter = 1

                # let's count the uncles and aunts the grandchild already has :

                for relation_type, related_person in grandparent_links.items():

                    if 'aunt_uncle' in relation_type:

                        aunt_counter += 1

                # let's add to the grandchild new uncles and aunts :

                for relation_type, related_person in grandparent_links.items():

                    if 'sibling' in relation_type and related_person not in bdd[grandchildren]['links'].values():

                        bdd[grandchildren]['links'][f'aunt_uncle_{aunt_counter}'] = related_person

    # adding nephews

    for nephew, nephew_data in bdd.items():

        nephew_links = nephew_data['links']
        links_copy = nephew_links.copy()

        for link_type, linked_person in links_copy.items():

            if 'aunt_uncle' in link_type:

                aunt_uncle = linked_person
                aunt_uncle_links = bdd[aunt_uncle]['links']

                nephew_counter = 1

                # let's count the nephews and nieces the aunt_uncle already has :

                for relation_type, related_person in aunt_uncle_links.items():

                    if 'nephew' in relation_type:

                        nephew_counter += 1

                if not nephew in list(aunt_uncle_links.values()):

                    aunt_uncle_links[f'nephew_{nephew_counter}'] = nephew

    # Adding cousins :

    for person, person_data in bdd.items():

        person_links_copy = person_data['links'].copy()
        person_links = person_data['links']

        cousins_count = 1

        for link_type, person_linked in person_links_copy.items():

            grandparent = ''

            if 'grandparent' in link_type:

                grandparent = person_linked

                for link_grandchildren, grandchildren in bdd[grandparent]['links'].items():

                    check_bol = 'grandchildren' in link_grandchildren and grandchildren is not person

                    if check_bol:

                        person_links[f'cousin_{cousins_count}'] = grandchildren
                        cousins_count += 1



def graph_calulator(bdd):

    # ---------- #
    # parameters for the calculus graph

    alpha = 1.
    beta = 1.5
    gamma = 1.7
    delta = 2.

    # bdd_calculus_intermediate

    bdd_calculus_intermediate = {}

    for key, value in bdd.items():

        bdd_calculus_intermediate[key] = {}
        links = bdd_calculus_intermediate[key]

        for relation_type, linked_person in value['links'].items():

            checker_1 = 'parent' in relation_type or 'child' in relation_type
            checker_1 = checker_1 and not 'grand' in relation_type
            checker_2 = 'grandparent' in relation_type or 'grandchild' in relation_type
            checker_3 = 'sibling' in relation_type
            checker_4 = 'aunt_uncle' in relation_type or 'nephew' in relation_type
            checker_5 = 'cousin' in relation_type

            if checker_1 or checker_3:

                links[linked_person] = alpha

            elif checker_2:

                links[linked_person] = beta

            elif checker_4:

                links[linked_person] = gamma

            elif checker_5:

                links[linked_person] = delta

    return bdd_calculus_intermediate


def saver_base(data, name):

    path_dbb_content = f"./Database/{name}.json"
    python_file = open(path_dbb_content, "w+")
    json.dump(data, python_file)
    python_file.close()
