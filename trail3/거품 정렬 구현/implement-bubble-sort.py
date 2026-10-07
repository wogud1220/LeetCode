n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for j in range(len(arr)):
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]

print(*arr)

