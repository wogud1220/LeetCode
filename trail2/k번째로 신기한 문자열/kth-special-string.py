n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

arr = []
for s in str:
    if s[:len(t)] == t:
        arr.append(s)

arr.sort()

print(arr[k-1])