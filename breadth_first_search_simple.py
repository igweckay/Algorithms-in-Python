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

# map is an adjacency dictionary that lists all of the cities as keys and their connection cities
map = {'Arad': ['Zerind','Timisoara'],
        'Zerind': ['Arad','Oradea'],
        'Oradea': ['Zerind','Sibiu'],
        'Timisoara': ['Arad','Lugoj'],
        'Lugoj': ['Timisoara','Mehadia'],
        'Mehadia': ['Lugoj','Drobeta'],
        'Drobeta': ['Mehadia','Craiova'],
        'Craiova': ['Drobeta','Rimnicu Vilcea','Pitesti'],
        'Rimnicu Vilcea': ['Craiova','Pitesti','Sibiu'],
        'Sibiu':['Zerind','Oradea','Rimnicu Vilcea','Fagaras'],
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

# level is a map/dictionary of the level on the tree each node is attached to, it is to be appended whenever
# a new node is introduced
level = {'Arad': '0'}

# parent is a map/ dictionary of the parent nodes, so that one can traverse through the tree to find a branch to the root node
# the parent dictionary is to be appended whenever a new node is introduced
parent = {'Arad': 'nil'}
level_number = 1

# frontier is the list of nodes to be visited. Sicne this code starts at Arad, Arad is on the frontier
frontier = ['Arad']

while frontier:
    # next is list of unexplored nodes in the frontier
    next = []
    node_count_frontier = len(frontier)
    u = 0 #vertex in frontier
    v = 0
    for u in range(0,node_count_frontier):
        for v in range(0,len(map[frontier[u]])):
            next_node_cities = map[frontier[u]]
            booli = (next_node_cities[v] in level.keys())
            if (next_node_cities[v] not in level.keys()):
                #append the level number to the level dictionary "memory part 1"
                level[next_node_cities[v]] = [level_number]
                #append to the parent dictionary "memory part 2". this will help with traversal
                parent[next_node_cities[v]] = frontier[u]
                #move the next list to the frontier, and the drama continues... don don don
                next.append(next_node_cities[v])
    frontier = next
    level_number += 1


print level; print parent
