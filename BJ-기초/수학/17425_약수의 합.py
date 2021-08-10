# 테스트케이스 주어진 경우 ->시간복잡도 문제 생김
# 약수의 개수는 약수가 아닌 수의 개수보다 매우 작다
# part1: f[i]를 구한다 / part2: 입출력 구현

MAX = 1000000
f = [1]*(MAX+1)
g = [0]*(MAX+1)
for i in range(2,MAX+1):
    j = 1
    while i*j <= MAX:
        f[i*j] = f[i*j] + i
        j = j + 1
for j in range(1,MAX+1):
    g[i] = g[i-1] + f[i]

T = int(input())
ans = []
for i in range(1,T+1):
    N = int(input())
    ans.append(g[N])
print('\n'.join(map(str,ans))+'\n')

