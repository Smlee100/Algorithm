# 0.기초
# 테스트케이스의 개수가 주어진 유형(*테스트케이스 번)
# 각각을 독립적인 문제로 생각하고 푼다(입력받으면서 출력해주면됨)

T = int(input()) #테스트케이스 개수
for i in range(1,T+1):
    a,b = map(int, input().split())
    print(a+b)


