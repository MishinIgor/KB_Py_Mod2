import random
a = [[str(random.randint(0,9)) for i in range(4)] for j in range(4)]
f = open('input.txt','w')
for i in a:
    for j in i:
        f.write(j)
        f.write(' ')
    f.write('\n')
f.close()