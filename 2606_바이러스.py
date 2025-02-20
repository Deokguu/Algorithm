def bfs(s, V):
    visited = [0 for _ in range(V+1)]
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)
        for w in G[t]:
            if visited[w] == 0:    
                queue.append(w)
                visited[w] = 1
    return sum(visited) -1

    

            

V = int(input())
E = int(input())

G = [[] for _ in range(V+1)]

for i in range(E):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)

print(bfs(1, V))