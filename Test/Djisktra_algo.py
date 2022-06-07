# imports :
import json

# base parameters :

alpha = 1.

# open txt database :

path_calculus_dbb = '../Database/database_calculus.json'
dbb_calculus_file = open(path_calculus_dbb, "r")
dbb_calculus = json.loads(dbb_calculus_file.read())

# Setupping the node list :

node_list = []

# Searching the nearest node :

def min_finder(starting_node):
    minimum = 1000000
    end_node = ''
    for near_node, node_infos in starting_node.items():
        if node_infos['length'] < minimum:
            minimum = node_infos['length']
            end_node = near_node
    return dbb_calculus[end_node]

# Updating distances :

def distance_updater(starting_node, intermediate_node_1, intermediate_node_2):
    dist_2 = intermediate_node_2[starting_node.key()]
    dist_2 = dist_2['length']
    dist_1 = intermediate_node_1[starting_node.key()]
    dist_1 = dist_1['length']
    dist_3 = intermediate_node_2[intermediate_node_1.key()]
    dist_3 = dist_3['length']
    if dist_1 > dist_2 + dist_3:
        dist_2 = dist_2 + dist_3
        index = node_list.index(intermediate_node_2.key())
        node_list[index - 1] = intermediate_node_1.key()

def djikstra(graph, weight, starting_node):
    calculus_graph = dbb_calculus
    s1 = starting_node
    while calculus_graph != {}:
        intermediate_node_1 = min_finder(s1)
