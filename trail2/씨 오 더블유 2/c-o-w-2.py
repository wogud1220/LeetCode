n = int(input())
S = input()

# Please write your code here.
S = list(S)
cnt = 0
for i in range(len(S)):
    if S[i] == 'C':
        for j in range(i+1, len(S)):
            if S[j] == 'O':
                for k in range(j+1, len(S)):
                    if S[k] == 'W':
                        cnt += 1
    

print(cnt)