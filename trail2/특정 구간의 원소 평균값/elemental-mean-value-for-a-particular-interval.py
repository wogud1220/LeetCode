n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        if (sum(arr[i:j]) / len(arr[i:j])) in arr[i:j]:
            cnt += 1
            # print(f"합계:{sum(arr[i:j])} 평균: {(sum(arr[i:j]) // len(arr[i:j]))} in {arr[i:j]}")

print(cnt)