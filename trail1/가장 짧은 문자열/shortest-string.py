s1 = input()
s2 = input()
s3 = input()

a = len(s1)
b = len(s2)
c = len(s3)

d = max(a,b)
d = max(d,c)

e = min(a,b)
e = min(e,c)

print(d-e)