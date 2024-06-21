# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. 
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
f = open('24_demo.txt')
data = f.read()
schet = 1
maximal = 0
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        schet+=1
    else:
        maximal = max(maximal,schet)
        schet = 1
print(maximal)
        
