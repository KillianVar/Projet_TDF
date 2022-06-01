from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement


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