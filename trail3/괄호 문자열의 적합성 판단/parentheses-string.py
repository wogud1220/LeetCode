str = input()

# Please write your code here.

str = list(str)
stack = []
flag = 0
for ch in str:
    if ch == "(":
        stack.append(ch)

    else:
        if stack:
            stack.pop()
        else:
            flag = 1
            break

if flag == 1:
    print("No")

elif stack:
    print("No")
else:
    print("Yes")