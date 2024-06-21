# !5 = 5*4*3*2*1
def f(n):
    if n>1:
        return f(n-1)*n
    if n<=1:
        return 1
print(f(5))