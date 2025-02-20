def bfs(s):
    tracking = []
    visited = [0 for _ in range(V+1)]
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)
        tracking.append(t)

        for w in sorted(G[t]):
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1

    return tracking
def dfs(s):
    tracking = []
    visited = [0 for _ in range(V+1)]
    stack = []
    stack.append(s)
    visited[s] = 1

    while stack:
        t = stack.pop()
        tracking.append(t)

        for w in sorted(G[t], reverse = True):
            if visited[w] == 0:
                stack.append(w)
                visited[w] = 1

    return tracking
        
        
V, E, start = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    v1, v2 = map(int, input().split())
    G[v1].append(v2)
    G[v2].append(v1)
print(*dfs(start))
print(*bfs(start))