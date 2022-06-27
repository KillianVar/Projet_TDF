### NEW TRIAL

# il faut faire un : pip install networkx

# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
import json
from Dijkstra_algo import Graph, dijkstra_algorithm, print_result


def visualization(id1, id2):
    file_calculus = open('../Database/database_queen/database_calculus.json')
    init_graph = json.load(file_calculus)
    file_calculus.close()

    file_relations = open('../Database/database_queen/database_conversion.json')
    relations = json.load(file_relations)
    file_relations.close()

    family_graph = nx.Graph()

    nodes = list(init_graph.keys())
    people_graph = Graph(nodes, init_graph)

    previous_nodes, shortest_path = dijkstra_algorithm(graph=people_graph, start_node=id1)
    list_relations, list_people_related = print_result(previous_nodes, shortest_path, id1, id2, relations=relations)

    # Contruction of the visualization

    for person_id in list_people_related:

        related_persons = relations[person_id]['links']

        for relation_type, related_person in related_persons.items():

            if 'sibling' not in relation_type:

                family_graph.add_node(related_person)
                family_graph.add_edge(person_id, related_person, relation=relation_type)

    chosen_path = []
    relations_labels = {}

    for k in range(len(list_relations)):
        chosen_path.append((list_people_related[k], list_people_related[k + 1]))
        relations_labels[(list_people_related[k], list_people_related[k + 1])] = list_relations[k]

    fig, ax = plt.subplots()

    positions = nx.kamada_kawai_layout(family_graph)
    nx.draw_networkx_nodes(family_graph, pos=positions, node_size=30)
    nx.draw_networkx_edges(family_graph, pos=positions, width=0.5,  edge_color='black')
    nx.draw_networkx_edges(family_graph, pos=positions, width=2., edgelist=chosen_path,
            edge_color='red')
    nx.draw_networkx_edge_labels(family_graph, pos=positions, font_size=3,
                                 edge_labels=relations_labels, label_pos=0.5, alpha=0.8)
    nx.draw_networkx_labels(family_graph, pos=positions, font_size=5)
    plt.savefig('test.png', dpi=500)
    plt.show(dpi=500)

visualization("@I392@", "@I406@")