

def check_bipartite_graph(i, p):
    visited[i] = p
    for e in G[i]:
        if visited[e]==-1:
            visited[e] = p^1
            if check_bipartite_graph(e, p)==False:
                return False
        else:
            if visited[e]==p:
                return False
    return True
