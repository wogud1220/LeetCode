n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
add = []

for i in range(0,n,2):
    mid_num = arr[0:i+1]
    mid_num.sort()
    a = mid_num[len(mid_num) // 2]
    add.append(a)

print(*add)

