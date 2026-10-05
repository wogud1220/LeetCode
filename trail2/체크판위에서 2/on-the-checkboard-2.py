R, C = map(int, input().split()) # r세로, c가로
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.

answer = 0

# 첫 번째 중간 지점
for r1 in range(1, R - 1):
    for c1 in range(1, C - 1):

        # 두 번째 중간 지점
        for r2 in range(r1 + 1, R - 1):
            for c2 in range(c1 + 1, C - 1):

                # 이동할 때마다 색이 달라야 함
                if (grid[0][0] != grid[r1][c1]
                    and grid[r1][c1] != grid[r2][c2]
                    and grid[r2][c2] != grid[R-1][C-1]):

                    answer += 1

print(answer)