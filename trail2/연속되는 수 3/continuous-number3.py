N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
cnt = 0
max_cnt = 0
minus_cnt = 0

for i in range(1, N):
    if arr[i-1] > 0 and arr[i] > 0:
        cnt += 1
    else:
        cnt = 0
    if arr[i-1] < 0 and arr[i] < 0:
        minus_cnt += 1
    else:
        minus_cnt = 0

    max_cnt = max(max_cnt, cnt, minus_cnt)
print(max_cnt + 1)