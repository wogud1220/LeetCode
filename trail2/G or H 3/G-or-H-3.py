n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.

a = max(x)
arr = [0] * (a + 1)

for i, j in zip(x,c):
    arr[i] = j

for i in range(len(arr)):
    if arr[i] == 'G':
        arr[i] = 1
    elif arr[i] == 'H':
        arr[i] = 2


i = 0
j = k

max_cnt = 0
for i in range(len(arr)):
    result = 0
    for j in range(i, min(i + k + 1, len(arr))):
        result += arr[j]
    max_cnt = max(max_cnt,result)
    
print(max_cnt)

