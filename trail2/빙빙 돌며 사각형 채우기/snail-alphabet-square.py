n, m = map(int, input().split())

# Please write your code here.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dir_num = 0

arr = [[0 for _ in range(m)] for _ in range(n)]
now_r, now_c = 0, 0


for i in range(1, n*m + 1):
    arr[now_r][now_c] = chr(65 + (i - 1) % 26)
    
    next_r = now_r + dy[dir_num]
    next_c = now_c + dx[dir_num]

    if 0 <= next_r < n and 0<= next_c < m and arr[next_r][next_c] == 0:
        now_r = next_r
        now_c = next_c
    else:
        dir_num = (dir_num + 1) % 4
        now_r += dy[dir_num]
        now_c += dx[dir_num]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()