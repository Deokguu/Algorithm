def bfs(sti, stj):
    queue = []
    queue.append([sti, stj])
    visited[sti][stj] = True

    while queue:
        ti, tj = queue.pop(0)
    
        for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
            newR = ti + di
            newC = tj + dj
            if 0<=newR<N and 0<=newC<N and arr[newR][newC] == 1 and not visited[newR][newC]:
                queue.append([newR, newC])
                visited[newR][newC] = True
            

T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split()) # M배열가로 N배열세로 K배추개수
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, input().split())
        arr[i][j] = 1
    
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1 and not visited[row][col]:
                bfs(row, col)
                cnt += 1
    # print(arr)
    # print(visited)
    print(f'#{tc} {cnt}')
    # print(arr)
