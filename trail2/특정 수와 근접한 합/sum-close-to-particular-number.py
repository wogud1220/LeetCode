N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.


total = sum(arr)
ans = float('inf')

for i in range(N):
    for j in range(i + 1, N):
        remain = total - arr[i] - arr[j]

        diff = abs(S - remain)
        ans = min(ans, diff)

print(ans)