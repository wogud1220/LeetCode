N = int(input())
command = []
value = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push":
        value.append(int(line[1]))

    elif line[0] == "size":
        print(len(value))

    elif line[0] == "empty":
        if value:
            print(0)
        else:
            print(1)

    elif line[0] == "pop":
        print(value.pop())

    elif line[0] == "top":
        print(value[-1])
    else:
        value.append(0)
    
# Please write your code here.



