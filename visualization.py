### NEW TRIAL 

#il faut faire un : pip install networkx

# First networkx library is imported along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt
   
# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all the set of edges that constitutes a graph
        self.visual = []
          
    # addEdge function inputs the vertices of an edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)
          
    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()
  
# Driver code
# We're going to use the Dijstra_algo.py file to get the relations between two persons
import sys
import json
from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
from Dijkstra_algo import Graph, dijkstra_algorithm, print_result


def visualization (id1, id2):
    
    file_calculus = open('Database/database_calculus.json')
    init_graph = json.load(file_calculus)
    file_calculus.close()

    file_relations = open('Database/database_conversion.json')
    relations = json.load(file_relations)
    file_relations.close()

    name1, surname1 = relations[id1]["name"], relations[id1]["surname"]

    nodes = list(init_graph.keys())
    people_graph = Graph(nodes, init_graph)
    list_relations, list_people_related = dijkstra_algorithm(graph=people_graph, start_node=id1)

    # Contruction of the visualization 
    G = GraphVisualization()
    G.addEdge(f"{name1} {surname1}", f"{list_relations[0]}, ':', {list_people_related[0]}" )
    for i in range(1, len(list_relations)-1):
        G.addEdge(f"{list_relations[i]}, ':', {list_people_related[i]}", f"{list_relations[i+1]}, ':', {list_people_related[i+1]}")
    G.visualize()


print(visualization("@I398@", "@I406@"))
