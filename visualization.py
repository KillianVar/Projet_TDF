### NEW TRIAL

# il faut faire un : pip install networkx

# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
from tree_inspector import file_reading, tree_analysis


def path_visualization(database, id_1, id_2):

    family_graph = nx.Graph()
    init_graph, relations = file_reading(database)
    list_relations, list_people_related = tree_analysis(id_1, id_2, init_graph, relations)


    # Contruction of the visualization

    peoples_name = {}

    for person_id in list_people_related:

        related_persons = relations[person_id]['links']
        peoples_name[person_id] = relations[person_id]['surname']

        for relation_type, related_person in related_persons.items():

            checker = 'sibling' not in relation_type
            checker = checker and 'cousin' not in relation_type

            if checker:

                peoples_name[related_person] = relations[related_person]['surname']
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
    nx.draw_networkx_labels(family_graph, pos=positions, labels=peoples_name, font_size=9)
    nx.draw_networkx_edges(family_graph, pos=positions, width=0.5,  edge_color='black')
    nx.draw_networkx_edges(family_graph, pos=positions, width=2., edgelist=chosen_path,
            edge_color='red')
    nx.draw_networkx_edge_labels(family_graph, pos=positions, font_size=3,
                                 edge_labels=relations_labels, label_pos=0.5, alpha=0.8)
    nx.draw_networkx_labels(family_graph, pos=positions, font_size=5)
    plt.savefig('test.png', dpi=500)
    plt.show()

def whole_visualisation(database):

    family_graph = nx.Graph()



path_visualization('database_family1', "@I27@", "@I36@")