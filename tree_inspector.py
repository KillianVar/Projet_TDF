import tree_manager
import json
from Dijkstra_algo import Graph, dijkstra_algorithm, print_result
import os.path
from os import path


def reloader(database, file):
    file_path = f'../Database/{database}/{file}'

    bdd = tree_manager.gedcom_converter(file_path)

    tree_manager.tree_linker(bdd)
    graph_calculus = tree_manager.graph_calulator(bdd)

    tree_manager.saver_base(bdd, f'{database}/database_conversion')
    tree_manager.saver_base(graph_calculus, f'{database}/database_calculus')


def file_reading(database):

    t = True

    while t:
        try:
            file_calculus = open(f'./Database/{database}/database_calculus.json', 'r')
            init_graph = json.load(file_calculus)
            file_calculus.close()

            file_relations = open(f'./Database/{database}/database_conversion.json', 'r')
            relations = json.load(file_relations)
            file_relations.close()

            t = False

        except IOError:

            print('- ' * 50)
            print("""
            We weren't able to locate your files.
            Please enter the name of the database folder, we will try to read again the
            database in order to study your family tree.
            """)
            print('- ' * 50)
            database = input()

    return init_graph, relations


def tree_analysis(id_1, id_2, init_graph, relations):

    nodes = list(init_graph.keys())
    people_graph = Graph(nodes, init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=people_graph, start_node=id_1)
    links, path = print_result(previous_nodes, shortest_path, id_1, id_2, relations=relations)
    return links, path

reloader('database_family1', 'familiy1.ged')