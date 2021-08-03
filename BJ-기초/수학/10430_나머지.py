# (A+B)%C = (A%C + B%C)%C 와 항상 같음
# (A*B)%C = (A%C * B%C)%C 와 항상 같음

a,b,c = map(int, input().split())

print((a+b)%c)
print((a%c + b%c)%c)
print((a*b)%c)
print((a%c * b%c)%c)