def GCD(x,y):
    if y == 0:
        return x
    else:
        return GCD(y,x%y)

a,b = map(int, input().split())
g = GCD(a,b)
print(g)
print((a*b)//g)