n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
# n*n , t초, r행, c열, d = u d r l
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

# if d == 'U':
#     dir_num = (dir_num) % 4

# elif d == "D":
#     dir_num = (dir_num - 2) % 4

# elif d == "R":
#     dir_num = (dir_num + 1) % 4

# elif d == "L":
#     dir_num = (dir_num - 1) % 4


if d == "R":
    dir_num = 0
elif d == "U":
    dir_num = 1
elif d == "L":
    dir_num = 2
else:
    dir_num = 3



# arr = [[0 for _ in range(2)] for _ in range(n+1)]
# arr[0] = r,c
for i in range(1,t+1):
    nr = r + dy[dir_num]
    nc = c + dx[dir_num]
    
    if 0 < nr <= n and 0 < nc <= n:
        r = nr
        c = nc
    else:
        if dir_num == 0:
            dir_num = 2
        elif dir_num == 1:
            dir_num = 3
        elif dir_num == 2:
            dir_num = 0
        elif dir_num == 3:
            dir_num = 1

print(r,c)
