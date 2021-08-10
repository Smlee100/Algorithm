MAX = 1000000
check = [0] * (MAX+1)
check[0] = check[1] = True #true:지워진 수-> 우선 처리(2는 소수)

#에라토스테네스의 체: 특정 범위안에 소수인지 아닌지 판별하기 위해 사용
for i in range(2,MAX+1):
    if not check[i]: #false:i가 지워지지 않음
        j = i+i #i의 배수
        while j <= MAX:
            check[j] = True #i의 배수를 모두다 지워버림
            j = j+i #i씩 증가해가면서

m,n = map(int, input().split())
for i in range(m,n+1):
    if check[i] == False: #지워지지 않은 수가 소수
        print(i)
