arr = [list(map(int, input().split())) for _ in range(9)]
max_v = 0
p, q = 0, 0
for i in range(9):
    for j in range(9):
        if max_v <= arr[i][j]:
            max_v = arr[i][j]
            p, q = i+1, j+1
print(max_v)
print(p, q)
