n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_answer = 0

i = 0
j = k

while True:
    if j > len(arr):
        break

    max_answer = max(max_answer, sum(arr[i:j]))

    i += 1
    j += 1

print(max_answer)
