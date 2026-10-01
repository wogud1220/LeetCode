N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.

# print(dir) ['N', 'E', 'S', 'W', 'S', 'E']
# print(dist) [3, 2, 3, 4, 5, 8]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

dir_num = 0
now_r, now_c, flag, cnt = 0, 0, 0, 0
for i in range(N):
    if dir[i] == 'N':
        dir_num = 3
    elif dir[i] == 'E':
        dir_num = 0
    elif dir[i] == 'S':
        dir_num = 1
    elif dir[i] == 'W':
        dir_num = 2

    for j in range(dist[i]): # 3회
        now_r += dy[dir_num] 
        now_c += dx[dir_num]
        cnt += 1
        if now_r == 0 and now_c == 0:
            print(cnt)
            flag = 1
            break

    if flag == 1:
        break
        
if flag == 0:
    print(-1)

