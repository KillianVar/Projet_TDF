from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement


gedcom_parser = Parser()
file_path = '/Database/Queen_Eliz_II.ged'
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

print(bdd['@I920@']['father'])
print(bdd['@I919@']['father'])
print(bdd['@I920@']['mother'])
print(bdd['@I919@']['mother'])


def chemin(bdd, id1, id2):
    list1 = [[id1]]
    list2 = [[id2]]
    t = True
    while t:
        l1 = []
        for i in list1[-1]:
            l1.append(bdd[f"{i}"]['father'])
            l1.append(bdd[i]['mother'])
        list1.append(l1)
        l2 = []
        for i in list2[-1]:
            l2.append(bdd[i]['father'])
            l2.append(bdd[i]['mother'])
        list2.append(l2)
        for i in range(len(list1)):
            for m in list1[i]:
                for j in range(len(list2)):
                    if m in list2[j]:
                        common_ancestor = m
                        t = False
    print(list1, list2)
    return f"Le plus court chemin vaut {i+j} et leur ancêtre commun est {common_ancestor}"


print(chemin(bdd, '@I921@', '@I920@'))
