def connected_r(node, graph, connections):
    for neighbor in graph[node]:
        if neighbor not in connections:
            connections.add(neighbor)
            connections |= connected_r(neighbor, graph, connections)

    return connections

def connected(node, graph):
    return connected_r(node, graph, set())

def cc(graph):
    '''
    graph is in the form:
    key: { node_key, ... }

    Directed graph implied

    return set { key: {reachable}, ... }
    '''

    #print(connected('a', graph))
    reachable = { key: {} for key in graph }
    for key in graph:
        reachable[key] = connected(key, graph)

    return reachable

# Bag problem easy. Parse bags into map. Count all bags that can reach shinybag
#g = cc({ 'a': { 'b', 'c' }, 'b': {'c', 'a'}, 'c': {'d'}, 'd': {} })
#print(g)
