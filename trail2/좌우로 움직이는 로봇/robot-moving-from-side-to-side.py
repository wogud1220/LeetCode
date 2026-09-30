n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

arr1 = [0] * (sum(t) + 1)
arr2 = [0] * (sum(t_b) + 1)
time =0

for i in range(n):
    for j in range(t[i]):
        time += 1

        if d[i] == "R":
            arr1[time] = arr1[time-1] + 1

        else:
            arr1[time] = arr1[time-1] - 1

time = 0
    
for i in range(m):
    for j in range(t_b[i]):
        time += 1

        if d_b[i] == "R":
            arr2[time] = arr2[time-1] + 1

        else:
            arr2[time] = arr2[time-1] - 1

cnt = 0
long_a = 0
long_b = 0


long_a = sum(t)
long_b = sum(t_b)

i = 1
j = 1

k = 1

while k <= max(long_a, long_b):

    if i == long_a and k > long_a:
        prev_a = arr1[i]
    else:
        prev_a = arr1[i-1]

    if j == long_b and k > long_b:
        prev_b = arr2[j]
    else:
        prev_b = arr2[j-1]

    if arr1[i] == arr2[j] and prev_a != prev_b:
        cnt += 1

    if i < long_a:
        i += 1
    
    if j < long_b:
        j += 1

    k += 1

print(cnt)