##########################################################################################
# breadth-first search implimentation
# by kay igwe
#
# using python 2.7.1
# helpful lecture from MIT OpenCourseware: https://www.youtube.com/watch?v=s-CYnVz-uh4
#
# This algorithm performs breadth first search. and prints the level of the node with respect
# to the tree levels, and it prints the parent of the node. The level can be used to figure out
# the level in the tree. The parent can be used to trace a node's path back to the root node
# In this code, the root node is Arad, but it can be changed to be any node or to be based on
# user input.
##########################################################################################
from operator import itemgetter, attrgetter
# map is an adjacency dictionary that lists all of the cities as keys and their connection cities
map = {'Arad': ['Zerind','Timisoara','Sibiu'],
        'Zerind': ['Arad','Oradea'],
        'Oradea': ['Zerind','Sibiu'],
        'Timisoara': ['Arad','Lugoj'],
        'Lugoj': ['Timisoara','Mehadia'],
        'Mehadia': ['Lugoj','Drobeta'],
        'Drobeta': ['Mehadia','Craiova'],
        'Craiova': ['Drobeta','Rimnicu Vilcea','Pitesti'],
        'Rimnicu Vilcea': ['Craiova','Pitesti','Sibiu'],
        'Sibiu':['Arad','Oradea','Rimnicu Vilcea','Fagaras'],
        'Fagaras': ['Sibiu','Bucharest'],
        'Pitesti': ['Rimnicu Vilcea','Craiova','Bucharest'],
        'Bucharest': ['Pitesti','Giurgiu','Urziceni'],
        'Giurgiu': ['Bucharest'],
        'Urziceni': ['Bucharest','Hirsova','Vaslui'],
        'Hirsova': ['Urziceni','Eforie'],
        'Eforie': ['Hirsova'],
        'Vaslui': ['Urziceni','Iasi'],
        'Iasi': ['Vaslui','Neamt'],
        'Neamt': ['Iasi']}

#added this adjacency dictionary that not only includes the connecting cities, but also includes distances
map_complex = {'Arad': [['Zerind', 75],['Sibiu', 140],['Timisoara', 118]],
        'Zerind': [['Arad', 75],['Oradea', 71]],
        'Oradea': [['Zerind', 71],['Sibiu', 151]],
        'Timisoara': [['Arad', 118],['Lugoj', 111]],
        'Lugoj': [['Timisoara', 111],['Mehadia', 70]],
        'Mehadia': [['Lugoj', 70],['Drobeta', 75]],
        'Drobeta': [['Mehadia', 75],['Craiova', 120]],
        'Craiova': [['Drobeta', 120],['Rimnicu Vilcea', 146],['Pitesti', 138]],
        'Rimnicu Vilcea': [['Craiova', 146],['Pitesti', 97],['Sibiu', 80]],
        'Sibiu':[['Arad', 140],['Oradea', 151],['Rimnicu Vilcea', 80],['Fagaras', 99]],
        'Fagaras': [['Sibiu', 99],['Bucharest', 211]],
        'Pitesti': [['Rimnicu Vilcea', 97],['Craiova', 138],['Bucharest', 101]],
        'Bucharest': [['Pitesti', 101],['Giurgiu', 90],['Urziceni', 85]],
        'Giurgiu': [['Bucharest', 90]],
        'Urziceni': [['Bucharest', 85],['Hirsova', 98],['Vaslui', 142]],
        'Hirsova': [['Urziceni', 98],['Eforie', 86]],
        'Eforie': [['Hirsova', 86]],
        'Vaslui': [['Urziceni', 142],['Iasi', 92]],
        'Iasi': [['Vaslui', 92],['Neamt', 87]],
        'Neamt': [['Iasi', 87]]}

#asking for user input
start_state = raw_input("Where would you like to start: ")
#end_state = raw_input("What is your destination? ")
# level is a map/dictionary of the level on the tree each node is attached to, it is to be appended whenever
# a new node is introduced
level = {start_state: '0'}

# parent is a map/ dictionary of the parent nodes, so that one can traverse through the tree to find a branch to the root node
# the parent dictionary is to be appended whenever a new node is introduced
parent = {start_state: 'nil'}
level_number = 1

# frontier is the list of nodes to be visited. Sicne this code starts at Arad, Arad is on the frontier
frontier = [start_state]

while frontier:
    # next is list of unexplored nodes in the frontier
    next = []
    node_count_frontier = len(frontier)
    for u in range(0,node_count_frontier):
        for v in range(0,len(map[frontier[u]])):
            next_node_cities = map[frontier[u]]
            if (next_node_cities[v] not in level.keys()):
                #append the level number to the level dictionary "memory part 1"
                level[next_node_cities[v]] = [level_number]
                #append to the parent dictionary "memory part 2". this will help with traversal
                parent[next_node_cities[v]] = frontier[u]
                #move the next list to the frontier, and the drama continues... don don don
                next.append(next_node_cities[v])
    frontier = next
    level_number += 1

#print level; print parent
#######################################################################
# This part of the code accounts for distance and chooses the node with
# the shortest distance from its parent
#
# contains and start and a goal state
# It uses the adjacency dictionary "complex_map"
#######################################################################
level_complex = {start_state: 0.0}
level_number_complex = 0
level_second_number_complex = 0
parent_complex = {start_state: 'nil'}
frontier_complex = [start_state]

goal_state = raw_input("What is the destination: ")

while frontier_complex:
    level_number_complex += 1
    next_complex_future_frontier = []
    next_complex = []
    node_count_frontier_complex = len(frontier_complex)
    for x in range(0, node_count_frontier_complex):
            for y in range(0, len(map_complex[frontier_complex[x]])):
                    next_complex.append(map_complex[frontier_complex[x]][y])
    next_complex = sorted(next_complex, key=itemgetter(1), reverse = False)
    for q in range(0, node_count_frontier_complex):
        for z in range(0, len(next_complex)):
            if (next_complex[z][0] not in level_complex.keys()) and (goal_state not in parent_complex.keys()):
                level_complex[next_complex[z][0]] = str(level_number_complex) + "." + str(level_second_number_complex)
                parent_complex[next_complex[z][0]] = frontier_complex[q]
                level_second_number_complex += 1
                next_complex_future_frontier.append(next_complex[z][0])
    frontier_complex = next_complex_future_frontier
    print frontier_complex
    print level_complex

    #frontier_complex = []
            #next_complex.append(next_node_cities_complex)

            #z = 0
            #for z in range(0, len(next_node_cities_complex)):
                #if next_node_cities_complex[z][1]





#print level; print parent
