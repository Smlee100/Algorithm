# 1. 정답의 형태: 모든 정답은 숫자버튼을 누르고 그 다음에 +/-버튼을 누른다 -> 숫자가 나오면 앞에 동작이 의미없어지기 때문
# 2. +/-버튼 둘중에 하나만 누르면 됨 -> +- 같이 있으면 결국 같은 채널임(중복되는 채널에 여러번 연산하지 않기 위함)
# 숫자버튼을 몇번, 어떤 채널로 이동해야하는지 알 수 없음: 방법을 의미(어떤것이 최소가 되는지 알 수 없으니까 다해보는 것->브루트포스 문제)

# 숫자버튼을 이용해서 어디로 이동할 것인가?
# +/-를 몇 번 누르면 되는지 계산

import sys
input = sys.stdin.readline

N = int(input()) #이동하려는 채널
M = int(input()) #고장난 버튼 개수
button = [False] * 10 #숫자버튼(초기값:고장없음)
if M > 0:
    a = list(map(int,input().split())) #고장난 버튼이 있다면 고장난 숫자버튼 입력받음
else:
    a = [] #고장난 버튼 없다면 empty
for x in a:
    button[x] = True

# TODO: 함수 이해 필요(if조건) 다시!
# 이동할 채널C 정한다
# C에 포함되어있는 숫자 중에 고장난 버튼이 있는지 확인한다
# 고장난 버튼이 포함되어 있지 않다면 |C-N|을 계산해 +/- 버튼을 몇 번 눌러야 하는지 계산한다
def possible(C): #C(이동가능한 채널)로 이동가능하면 그때 C의 숫자의 개수를 리턴하는 함수
    if C == 0:
        if button[0]: #고장났으면 불가능
            return 0
        else: #아니면 0 한번 누르면 되니까 리턴 1
            return 1
    length = 0
    while C > 0:
        if button[C%10]: #한자리씩 보기위함
            return 0
        length = length + 1
        C = C // 10
    return length

# 100번에서 +/-로만 움직이는 경우
ans = abs(N-100)

for i in range(0,1000000+1): #이동할 수 있는 채널의 수 1000000
    C = i
    length = possible(C)
    if i > 0 : #숫자를 눌러서 갈 수 있는 경우
        press = abs(C-N) #+/- 버튼을 몇 번 눌러야 하는지
        if ans > length + press:
             ans = length + press
print(ans)
