def dfs(arr, row, col):
    '''
    각 요소마다 네 방향으로 최솟값이 되는 인덱스를 탐색하는 등의 동작이 반복되니
    그를 간편하기 위해 쓸 길찾기 함수를 dfs 방식으로 설계
    '''
    newR, newC = row, col
    curR, curC = row, col
    stack = [[row, col]] #현재 위치 push 하고 시작. pop 해서 관련된 노드?(네 방향 중 최솟값) 찾아가야 하니까..!
    cnt = 1

    while stack: # 스택 안에 요소가 존재할 때만 루프돌기
        curR, curC = stack.pop() # stack에 쌓았던 row, col을 pop 해서 curR, curC로 받고 시작작 
        minR, minC = curR, curC
        min_v = 501

        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            newR = curR + dr
            newC = curC + dc

            if 0<=newR<N and 0<=newC<N:# 배열 내에 있고
                if min_v > arr[newR][newC]: # 최솟값보다 작으면
                    min_v = arr[newR][newC] # 네 방향의 최솟값 갱신
                    minR, minC = newR, newC

        if arr[minR][minC] > arr[curR][curC]: # 그 최솟값이 현위치 값보다 크거나 같으면 while문 종료료
            break
        
        stack.append([minR, minC]) #그게 아니라면 최소가 되는 인덱스 stack에 쌓기
        cnt += 1 #이동거리 + 1. 이후에 while문 처음으로 돌아가서 윗줄에서 stack에서 쌓았던 minR, minC를 다시 pop해서 curR, curC로 받고 그 위치부터 반복 시작 
    
    return cnt

T = int(input())

for tc in range(1, T+1):
    N = int(input()) 
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for row in range(N):
        for col in range(N):
            cnt = dfs(arr, row, col)

            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{tc} {max_cnt}')

#input값
'''
3
5
19 57 74 73 94
26 27 32 98 61
40 88 49 38 25
21 66 53 95 46
80 23 58 39 89
7
40 49 56 83 84 31 11
42 95 12 16 21 19 26
98 93 29 68 10 92 82
23 13 24 58 35 25 47
17 66 39 67 70 14 87
22 34 46 94 69 96 89
62 88 50 51 61 71 86
9
90 57 65 18 25 93 64 11 54
95 19 80 37 63 44 15 14 10
89 59 46 70 38 36 21 51 97
53 47 60 88 40 48 79 56 55
83 13 27 86 45 71 75 28 84
30 20 29 35 99 98 61 94 23
85 42 43 22 16 77 31 78 34
74 26 73 92 50 72 87 49 32
68 24 91 12 17 82 69 67 81
'''
