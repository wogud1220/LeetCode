N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
import math

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
dir_num = 3

now_r, now_c = N // 2, N // 2
str = list(str)
result = 0
result += board[now_r][now_c]

for i in range(0,T):

    if str[i] == "R":
        dir_num = (dir_num + 1) % 4

    elif str[i] == "L":
        dir_num = (dir_num - 1) % 4
    
    else: # f인데
        next_r = now_r + dy[dir_num]
        next_c = now_c + dx[dir_num]

        if 0 <= next_r < N and 0<= next_c < N: # 한칸넘어간게 격자 안이라면
            now_r += dy[dir_num]
            now_c += dx[dir_num]
            # 현재 위치 이동 간으
            result += board[now_r][now_c]
        else: #f인데 격자밖이라면
            pass


    
print(result)