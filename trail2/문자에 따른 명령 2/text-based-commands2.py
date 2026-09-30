dirs = input()

# Please write your code here.

dirs = list(dirs) # ['L', 'F']
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

dir_num = 3 # 처음엔 북쪽 보기
x,y = 0, 0

for ch in dirs:
    if ch == 'L':
        dir_num = (dir_num -1) % 4
    elif ch == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
