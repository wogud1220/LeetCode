n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]
x1, x2 = zip(*segments)
x1, x2 = list(x1), list(x2)

# Please write your code here.


arr = [0] * 101

# print(x1[0], x2[0])

for i in range(n):
    for j in range(x1[i], x2[i]+1): # 1, 2, 3, 4 
        arr[j] += 1

if n in arr: print("Yes")
else: print("No")

