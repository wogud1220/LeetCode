N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
from collections import defaultdict

hash = defaultdict(int)

for i in range(M):
    hash[student[i]] += 1

    if hash[student[i]] == K:
        print(student[i])
        break
else:
    print(-1)