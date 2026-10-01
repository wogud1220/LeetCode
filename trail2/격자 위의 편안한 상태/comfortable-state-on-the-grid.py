n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
dir_num, cnt  = 0, 0

arr = [[0 for _ in range(n)] for _ in range(n)]


for k in range(m):
    i, j = points[k][0]-1, points[k][1]-1
    arr[i][j] = 1
    cnt = 0
    for v in range(4):
        if 0<= (i+dy[v]) < n and 0 <= (j+dx[v]) < n and arr[i + dy[v]][j + dx[v]] == 1 :
            cnt += 1
    
    if cnt == 3:
        print(1)
    else:
        print(0)


