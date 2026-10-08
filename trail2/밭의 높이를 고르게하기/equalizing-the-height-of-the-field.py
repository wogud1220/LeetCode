N, H, T = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_cost = float('inf')
for i in range(N - T + 1):
    cost = 0
    for j in range(i, i + T):
        cost += abs(arr[j] - H)

    min_cost = min(min_cost, cost)

print(min_cost)