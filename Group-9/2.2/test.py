from allinmatr import *
a = generate()
out(a)
t = {}
for i in a:
    for j in i:
        t[j] = 0
for i in a:
    for j in i:
        t[j] += 1
print(t)
