from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from gedcom.element.element import Element
from gedcom.element.family import FamilyElement


gedcom_parser = Parser()
file_path = 'Queen_Eliz_II.ged'
gedcom_parser.parse_file(file_path, False)

X = gedcom_parser.get_families()
