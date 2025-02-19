def dfs(arr, row, col, visited): #return 단지 내 가구 수
    stack = [[row, col]] # push

    cnt = 0
    
    while stack:
        curR, curC = stack.pop() # pop
        if not visited[curR][curC]:
            visited[curR][curC] = True # 간 곳 표시
            cnt += 1

            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                newR = curR + dr
                newC = curC + dc
                
                if 0<=newR<N and 0<=newC<N and arr[newR][newC] == 1 and visited[newR][newC] == False:
                    stack.append([newR, newC]) #push

    return cnt
            

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[False] *len(arr) for _ in range(len(arr))]
village = []
# print(arr)
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1 and not visited[row][col]:
            village.append(dfs(arr, row, col, visited))

village.sort()

print(len(village))
for i in range(len(village)):
    print(village[i])

