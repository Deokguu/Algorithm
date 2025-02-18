def dfs(arr, row, col): #return 단지 내 가구 수수
    curR, curC = row, col
    newR, newC = row, col

    visited = [[False] *len(arr) for _ in range(len(arr))]
    
    stack = [[row, col]] # push

    cnt = 0
    
    while stack:
        curR, curC = stack.pop() # pop
        visited[curR][curC] = True # 표시
        cnt += 1

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            newR = curR + dr
            newC = curC + dc
            
            if 0<=newR<N and 0<=newC<N and arr[newR][newC] == 1 and visited[newR][newC] == False:
                stack.append([newR, newC]) #push

        # cnt += 1
    
    return cnt
            

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
village = []
# print(arr)
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1:
            village.append(dfs(arr, row, col))
answer = list(set(village))
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])

