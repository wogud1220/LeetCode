commands = input()

# Please write your code here.
commands = list(commands)

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
dir_num = 3
now_r, now_c, cnt, flag = 0, 0, 0, 0

for command in commands:
    if command == 'F':
        now_r += dy[dir_num]
        now_c += dx[dir_num]
    elif command == 'R':
        dir_num = (dir_num + 1) % 4
    elif command == 'L':
        dir_num = (dir_num - 1) % 4

    cnt +=1
    # print(now_r, now_c)

    if now_r == 0 and now_c == 0:
        print(cnt)
        flag = 1
        break
    

if flag == 0:
    print(-1)


