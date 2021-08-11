#TODO: for문이 많다 용도와 이렇게 생각하는 방법 질문

# 9명중7명찾기 = 9명중2명찾기(대표2명뽑기->36가지)
# 1. 9명중 2명 찾기 2. 키를 계산하기

import sys
n = 9
heights = [int(sys.stdin.readline()) for _ in range(n)] #난쟁이 키 입력 받을 리스트 생성
heights.sort()

total = sum(heights) #난쟁이 9명 키의 합
#7난쟁이에 포함되지 않은 2명 난쟁이를 i, j라고 하면
for i in range(0,n):
    for j in range(i+1,n):
        if total - (heights[i] + heights[j]) == 100: #9명 키의합-가짜2명(j,j) 키의합 = 100
            for k in range(0,n): 
                if i == k or j == k:
                    continue
                print(heights[k])

            sys.exit(0)
