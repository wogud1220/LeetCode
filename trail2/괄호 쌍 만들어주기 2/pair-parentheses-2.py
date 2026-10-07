A = input()

# Please write your code here.

A = list(A)
cnt = 0

for i in range(1, len(A)):
    if A[i-1] == '(' and A[i] == '(':
        for j in range(i+1, len(A)-1):
            if A[j] == ')' and A[j+1] == ')':
                cnt += 1
print(cnt)