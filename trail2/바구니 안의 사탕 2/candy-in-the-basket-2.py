N, K = map(int, input().split())
candy = []
pos = []

for _ in range(N):
    c, p = map(int, input().split())
    candy.append(c)
    pos.append(p)

# Please write your code here.
arr = [0] * (max(pos) + 1)
for c,p in zip(candy,pos):
    arr[p] += c 


max_cnt = 0
for i in range(len(arr)):
    result = sum(arr[i:i + 2*K + 1])
    max_cnt = max(max_cnt, result)


print(max_cnt)