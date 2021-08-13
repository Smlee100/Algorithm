# E(15개)/S(28개)/M(19개) -> 조합의 수(=가능한 연도의 개수): 15*28*19=7980
# 모든 연도를 다 만들어도 갯수가 많지 않기때문에 가능하다

E,S,M = map(int, input().split())
e,s,m = 1,1,1 #year년은 e,s,m의 조합으로 되어있음 TODO: 설정해주는거 생각
year = 1
while True:
    if e == E and s == S and m == M:
        break
    e = e + 1
    s = s + 1
    m = m + 1
    if e >= 16:
        e = e - 15
    if s >= 29:
        s = s - 28
    if m >= 20:
        m = m - 19
    year = year + 1

print(year)