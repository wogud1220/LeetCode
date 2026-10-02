A = input()

# Please write your code here.



A = list(A)
cnt = 0

for i in range(len(A)):
    
    for j in range(i+1, len(A)): # 1 7 
        if A[i] == '(' and A[j] == ')':
            cnt += 1
            # print(i,j)
print(cnt)