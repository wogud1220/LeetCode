n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
max_answer = 0

for i in range(len(numbers)):
    for j in range(i+2, n): # 2 5 -> 2,3,4
        max_answer = max(max_answer, numbers[i]+numbers[j])

print(max_answer)