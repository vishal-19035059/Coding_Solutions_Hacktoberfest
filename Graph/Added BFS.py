# graph
L = [[0,1], [1,2], [2,3]]

# number of nodes
n = 4
G = {i:set() for i in range(n)}

# build graph
for i, j in L:
    G[i].add(j)
    G[j].add(i)

    
visited = [0]*n

# bfs 
def bfs(i):
    q = [i]
    visited = [0]*n
    while q:
        ele = q.pop()
        visited[ele] = 1
        for e in G[ele]:   
            if visited[e]==0:
                q.append(e)
