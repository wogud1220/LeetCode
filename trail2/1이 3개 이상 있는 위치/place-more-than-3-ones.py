n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.



dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
result = 0
for i in range(n):
    for j in range(n):
        cnt = 0

        for k in range(4): # 동서남북
            nj = j + dx[k]
            ni = i + dy[k]
            if (nj >=0 and nj < n) and (ni >= 0 and ni < n):
                if grid[ni][nj] == 1:
                    cnt += 1

        if cnt >=3:
            result += 1

print(result)
            