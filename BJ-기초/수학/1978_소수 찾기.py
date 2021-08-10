def is_prime(x):
    if x < 2:
        return False
    i = 2 #2부터 시작하여
    while i * i <= x:
        if x % i == 0:
            return False
        i = i+1 #1씩 증가시키면서
    return True

N = int(input())
a = list(map(int,input().split()))
ans = 0
for x in a:
    if is_prime(x):
        ans = ans + 1
print(ans)


