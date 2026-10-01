n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dir_num = 0
now_r_position = 0
now_c_position = 0
# dir_num = (dir_num + 1) % 4
for num in range(1, n * m + 1):
    arr[now_r_position][now_c_position] = num

    next_r = now_r_position + dy[dir_num]
    next_c = now_c_position + dx[dir_num]

    if 0 <= next_r < n and 0 <= next_c < m and arr[next_r][next_c] == 0:
        now_r_position = next_r
        now_c_position = next_c
    else: # 격자 끝이라면
        dir_num = (dir_num + 1) % 4
        now_r_position = now_r_position + dy[dir_num]
        now_c_position += dx[dir_num]

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()