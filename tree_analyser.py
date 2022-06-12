# Adding secondary links

# Adding siblings :
def tree_linker(bdd):

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




def graph_calulator(bdd):

    # ---------- #
    # parameters for the calculus graph

    alpha = 1.
    beta = 1.5

    # bdd_calculus_intermediate

    bdd_calculus_intermediate = {}

    for key, value in bdd.items():

        bdd_calculus_intermediate[key] = {}
        links = bdd_calculus_intermediate[key]

        for relation_type, linked_person in value['links'].items():

            checker_1 = 'parent' in relation_type or 'child' in relation_type
            checker_1 = checker_1 and not 'grand' in relation_type
            checker_2 = 'grandparent' in relation_type or 'grandchild' in relation_type

            if checker_1:

                links[linked_person] = alpha

            elif checker_2:

                links[linked_person] = beta

    return bdd_calculus_intermediate