import random
f = open('input.txt','w')
matr = [[str(random.randint(0,9)) for i in range(5)] for j in range(5)]
for i in matr:
    for j in i:
        f.write(j)
        f.write(' ')
    f.write('\n')
f.close()