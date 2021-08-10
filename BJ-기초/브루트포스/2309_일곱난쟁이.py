import sys
n = 9
heights = [int(sys.stdin.readline()) for _ in range(n)] #난쟁이 키 입력 받을 리스트 생성
heights.sort()

total = sum(heights) #난쟁이 9명 키의 합
for i in range(0,n):
    for j in range(i+1,n):
        if total - heights[i] - heights[j] == 100: #9명 키의합-가짜2명 키의합 = 100
            for k in range(0,n):
                if i == k or j == k:
                    continue
                print(heights[k])

            sys.exit(0)
