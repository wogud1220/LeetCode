a = input()

# Please write your code here.
a = list(a)
changed= False

for i in range(0, len(a)):
    if a[i] == '0':
        a[i] = '1'
        changed = True
        break

if changed == False:
    a[-1] = 0

for i in range(0, len(a)):
    a[i] = int(a[i])

result = 0
j = 0
for i in range(len(a)-1, -1, -1):
    result += 2**j * a[i]
    j+= 1
print(result)

    