# detect cycle in undrected graph
def detect_cycle(i, p):
    visited[i] = 1
    for e in G[i]:
        if e!=p:
            if visited[e]==0:
                if dfs(e, i):
                    return True
            else:
                return True
    return False
