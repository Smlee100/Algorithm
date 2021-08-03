# 입력: N의 진짜 약수(1과 N을 제외한 진짜 약수 모두 주어진 경우)
# N을 구하기 위해서는 입력의 최소값 X 최대값을 구하면 됨

N = int(input()) #진짜 약수 개수
a = list(map(int, input().split()))

print(max(a) * min(a))
