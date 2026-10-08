n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

# Please write your code here.

arr = [0] * (max(pos) + 1) # 17개 있음. [0] ~ [16]

for p, a in zip(pos, alpha):
    arr[p] = a
# print(arr)


max_cnt, result = 0, 0

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    for j in range(i, len(arr)): 
        if arr[j] == 0:
            continue

        temp = arr[i:j+1]
        g_count, h_count = temp.count('G'), temp.count('H')


        if g_count == 0:
            max_cnt = max(max_cnt, j - i)
        elif h_count == 0:
            max_cnt = max(max_cnt, j - i)
        elif g_count == h_count:
            max_cnt = max(max_cnt, j - i)
        

print(max_cnt)
