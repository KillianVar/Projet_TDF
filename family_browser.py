# The goal of this file is to try to browse the Queen's family tree.

# imports

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement

import random as rd

# code :

# Path to your `.ged` file
file_path = 'Database/database_queen/Queen_Eliz_II.ged'

# Initialize the parser
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)

root_child_elements = gedcom_parser.get_root_child_elements()

# Iterate through all root child elements
for element in root_child_elements:
    
    # Is the `element` an actual `IndividualElement`?
    # (Allows usage of extra functions such as `surname_match` and `get_name`.)
    if isinstance(element, IndividualElement):

        # Lets inspect this element :

        # his gender, birth, death and age :

        gender = element.get_gender()
        if gender == "M":
            pronoun = ["He", "His"]
        else:
            pronoun = ["She", "Her"]

        name, surname = element.get_name()

        print(50 * '-')
        print(f'{name} {surname}')

        if element.is_deceased():
            print(f'{pronoun[0]} was born on {element.get_birth_data()[0]} and died on {element.get_death_data()}.')
        else:
            print(f'{pronoun[0]} was born on {element.get_birth_data()[0]} and is still alive !')

        try:
            parents = gedcom_parser.get_parents(element)
            parent_name = []
            for parent in parents:
                parent_name.append(parent.get_name())
            if len(parents) == 2:
                print(f'{pronoun[1]} '
                f'parents are {parent_name[0][0]} {parent_name[0][1]} and {parent_name[1][0]} {parent_name[1][1]}.')
        except ValueError:
            pass

        try:
            families = gedcom_parser.get_families(element)
            if len(families) > 0 :
                for family in families:
                    print('--*--' * 30)
                    for family_members in gedcom_parser.get_family_members(family):
                        print(str(family_members).split()[1], family_members.get_name())

        except Exception:
            pass
