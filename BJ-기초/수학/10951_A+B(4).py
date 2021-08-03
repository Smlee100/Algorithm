# 0.기초
# 테스트케이스 주어지는 유형 but 입력이 몇 개인지 주어지지 않는 경우 -> EOF(End Of File)까지 받으면 됨
# Java: while(sc.hasNextInt()) 이용
# Python: try, except 이용

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break