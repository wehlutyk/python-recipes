# Walk all the neighboring nodes of a node up to a certain
# depth, using networkx

def _walk_neighbors(G, node, depth, l):
    l.append(node)
    if depth > 0:
        for n in G.neighbors_iter(node):
            _walk_neighbors(G, n, depth - 1, l)

def walk_neighbors(G, node, depth):
    out = []
    _walk_neighbors(G, node, depth, out)
    return out

