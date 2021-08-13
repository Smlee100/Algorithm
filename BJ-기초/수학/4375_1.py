# TODO: EOF(try, except를 어떤 조건보고 걸어준건가)

while True:
    try:
        N = int(input())
    except:
        break
    num = 0
    i = 1 #수의 길이 1부터 시작
    while True:
        num = num * 10 + 1 #이전 수를 이용해서 다음 수를 만들어줌(1,11,111,1111,...)
        if num % N == 0: #N의 배수이면
            print(i) #수의 길이를 출력
            break
        i = i + 1

