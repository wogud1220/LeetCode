n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

cnt = 0
max_cnt = 0


for i in range(1,len(arr)):
    if arr[i-1] == arr[i]:
        cnt += 1
    else:
        cnt = 0
    
    max_cnt = max(cnt,max_cnt)

print(max_cnt+1)