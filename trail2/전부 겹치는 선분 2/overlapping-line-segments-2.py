n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1 = [seg[0] for seg in segments]
x2 = [seg[1] for seg in segments]

# Please write your code here.
answer = "No"
# print(x1) 1, 4, 7, 2
for i in range(n):
    max_start = -float('inf')
    min_end = float('inf')

    for j in range(n): # i는 제거, j는 검사
        if i == j:
            continue

        max_start = max(max_start, x1[j])
        min_end = min(min_end, x2[j])

    if max_start <= min_end:
        answer = "Yes"
        break

print(answer)