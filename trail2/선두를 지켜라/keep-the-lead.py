n, m = map(int, input().split())

# Process A's movements
v = []
t = []
for _ in range(n):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

# Process B's movements
v2 = []
t2 = []
for _ in range(m):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

# Please write your code here.

arr1 = [0] * (sum(t) + 1)
arr2 = [0] * (sum(t2) + 1)
time = 0

for i in range(n): # 총 4번 0 1 2 3
    for j in range(t[i]): # 총 2번 , 0,1
        time+=1
        arr1[time] = arr1[time-1] +  v[i] 

time = 0
for i in range(m): # 총 4번 0 1 2 3
    for j in range(t2[i]): # 총 2번 , 0,1
        time+=1
        arr2[time] = arr2[time-1] +  v2[i] 


cnt = 0
leader = 0

for i in range(1, len(arr1)):
    if arr1[i] > arr2[i]:
        if leader == 0 :
            leader = 1
        elif leader == 2:
            cnt += 1
            leader = 1

    elif arr1[i] < arr2[i]:
        if leader == 0:
            leader = 2
        elif leader == 1:
            cnt += 1
            leader = 2

        else:
            leader = 2
# print(arr1)
# print(arr2)
print(cnt)
