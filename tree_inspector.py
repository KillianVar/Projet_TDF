import tree_manager
import json
from Dijkstra_algo import Graph, dijkstra_algorithm, print_result

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser

def reloader():
    file_path = '../Database/Queen_Eliz_II.ged'

    bdd = tree_manager.gedcom_converter(file_path)

    tree_manager.tree_linker(bdd)
    graph_calculus = tree_manager.graph_calulator(bdd)

    tree_manager.saver_base(bdd, 'database_conversion')
    tree_manager.saver_base(graph_calculus, 'database_calculus')

reloader()

file_calculus = open('../Database/database_calculus.json')
init_graph = json.load(file_calculus)
file_calculus.close()

file_relations = open('../Database/database_conversion.json')
relations = json.load(file_relations)
file_relations.close()

nodes = list(init_graph.keys())

people_graph = Graph(nodes, init_graph)

previous_nodes, shortest_path = dijkstra_algorithm(graph=people_graph, start_node="@I398@")

print_result(previous_nodes, shortest_path, "@I398@", "@I406@", relations=relations)