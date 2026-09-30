n, m = map(int, input().split())

d = [] # L R
t = [] # int
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

arr1 = [0] * (sum(t) + 1)
arr2 = [0] * (sum(t2) + 1)
time = 0
# Please write your code here.

for i in range(1,n+1):
    if d[i-1] == "R":
        for j in range(t[i-1]):
            time += 1
            arr1[time] = arr1[time-1] + 1 # 1초에 1, 2초에 2...
        
    else: # L
        for j in range(t[i-1]):
            time += 1
            arr1[time] = arr1[time-1] - 1 # 1초에 1, 2초에 2...
    
time = 0
for i in range(1,m+1):
    if d2[i-1] == "R":
        for j in range(t2[i-1]):
            time += 1
            arr2[time] = arr2[time-1] + 1 # 1초에 1, 2초에 2...
        
    else: # L
        for j in range(t2[i-1]):
            time += 1
            arr2[time] = arr2[time-1] - 1 # 1초에 1, 2초에 2...



for i in range(1, len(arr1)):
    if arr1[i] == arr2[i]:
        print(i)
        break
else:
    print(-1)
