MAX = 1000000
check = [True for i in range(MAX + 1)] #처음엔 모든 수가 소수(True)인 것으로 초기화
prime = []

#에라토스테네스의 체
for i in range(2,MAX+1):
    if check[i] == True: #i가 소수인 경우 (남은 수인 경우)
        prime.append(i)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= MAX:
            check[i * j] = False
            j = j + 1

# 다시!!!!
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3,MAX+1):
        if check[n-i] == False:
            print("{} = {} + {}".format(n, i, n-i))

        else:
            print("Goldbach's conjecture is wrong.")

