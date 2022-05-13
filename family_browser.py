# The goal of this file is to try to browse the Queen's family tree.

# imports

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import random as rd


# code :

# Path to your `.ged` file
file_path = 'Queen_Eliz_II.ged'

# Initialize the parser
gedcom_parser = Parser()

root_child_elements = gedcom_parser.get_root_child_elements()

# Iterate through all root child elements
for element in root_child_elements:

    # Is the `element` an actual `IndividualElement`?
    # (Allows usage of extra functions such as `surname_match` and `get_name`.)
    if isinstance(element, IndividualElement):

        # Lets inspect this element :

        # his gender, birth, death and age :

        gender = element.get_gender()
        if element.is_deceased():
            if gender == "male":
                print(f'He was born on {element.get_birth_data()} and died on {element.get_death_data()}.')
            else:
                print(f'She was born on {element.get_birth_data()} and died on {element.get_death_data()}.')
        else :
            if gender == "male":
                print(f'He was born on {element.get_birth_data()} and is still alive !')
            else:
                print(f'She was born on {element.get_birth_data()} and is still alive !')
