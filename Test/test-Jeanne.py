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
dict = {"individual" : 'Jeanne', "Sister" : 'Lilas', 'Husband' :'Ewald'} #à modifier = dictionnaire contenant les liens de la personne
G = GraphVisualization()
keys = [] 
for key in dict.keys():
    keys.append(key)
for i in range(len(keys)-1):
    G.addEdge(f"{keys[i]}, ':', {dict[keys[i]]}", f"{keys[i+1]}, ':', {dict[keys[i+1]]}")
G.visualize()

