# !5 = 5*4*3*2*1
def fact(n):
    if n>1:
        return n*fact(n-1)
    elif n<=1:
        return 1
print(fact(5))
# n=5 => 5* fact(5-1) => fact(5-1) = 4*fact(3) => fact(3) = 3*fact(2)...5*4*3*2*1