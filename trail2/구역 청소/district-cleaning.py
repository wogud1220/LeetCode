a, b = map(int, input().split())
c, d = map(int, input().split())

# Please write your code here.

arr1 = [0] * 101


for i in range(a, b):
    arr1[i] = 1
for i in range(c, d):
    arr1[i] = 1

print(sum(arr1))

