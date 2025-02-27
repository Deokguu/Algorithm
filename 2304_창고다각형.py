N = int(input())

columns = [] #기둥 위치, 높이
max_l = 0 # 위치 최댓값
max_h = 1 #높이 최댓값

for i in range(N):
    L, H = map(int, input().split())
    columns.append([L, H])
    if max_l < L:
        max_l = L
    if max_h < H:
        max_h = H
        max_idx = L

column_heights = [0] * (max_l+1) # 각 인덱스의 기둥 높이

for l, h in columns:
    column_heights[l] = h

total = 0 # 너비 1인 직사각형 넓이 합
temp = 0 # 현재까지의 가장 큰 높이 추적적

for i in range(max_idx+1):
    if column_heights[i] > temp:
        temp = column_heights[i] # 더 높은 높이 갱신
    total += temp

temp = 0
for i in range(max_l, max_idx, -1):
    if column_heights[i] > temp:
        temp = column_heights[i]
    total += temp
print(total)


