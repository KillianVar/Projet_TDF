#husband 
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement

import random as rd

file_path = 'Queen_Eliz_II.ged'
gedcom_parser = Parser()
gedcom_parser.parse_file(file_path, False)

root_child_elements = gedcom_parser.get_root_child_elements()

print(gedcom.parser.get_element_list())
