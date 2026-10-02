n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

arr = [0]*n

for i in range(0,n):
    for j in range(0,n):
        arr[i] = arr[i]+ A[j] * abs(i-j)

print(min(arr))