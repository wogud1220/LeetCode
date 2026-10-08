N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
from itertools import permutations

#아름다운 수열 생성
# bs = list(permutations(B))
# arr = [0] * len(bs)
# for idx,i in enumerate(bs, start = 0):
#     arr[idx] = list(i)
# # print(arr)

B.sort()

cnt = 0

for i in range(N - M + 1):
    temp = A[i:i + M]

    if sorted(temp) == B:
        cnt += 1

print(cnt)