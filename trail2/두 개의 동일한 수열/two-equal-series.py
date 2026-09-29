n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.

A_set = set(A)
B_set = set(B)

if A_set == B_set:
    print("Yes")
else:
    print("No")