# 문제에 할 수 있는 방법이 나와있음: 인접한 두 칸을 고르고, 사탕을 교환한다.
# 1.인접한 두 칸을 고른다: 한칸을 고르고(전체 칸의 개수:N^2) 인접한 4중에 한칸을 고른다(N^2*4) ->O(N^2)
# 2.같은 색으로 이루어져 있는 가장 긴 연속 부분 행 또는 열을 고른다: 어디에 있을지 알 수 없음 (전체를 검사해야함) ->O(N^2)
# 1&2방법을 하면 총 시간복잡도는 O(N^4)
# 2번에서 시간을 O(N)을 줄일 수 있음: 변화가 있을 수 있는 곳만 2번을 구하는 것 총 시간복잡도 O(N^3)으로 가능

# 가장 긴 연속 부분 행, 열 찾는 함수
# 테이블a에서 행 따로, 열 따로 봐주면 됨
def check(a, start_row, end_row, start_col, end_col):
    n = len(a)
    ans = 1
    #행 순회하면서 연속되는 숫자 세기
    for i in range(start_row, end_row+1): #몇번행부터 몇번행까지 검사해라
        cnt = 1 #현재 연속을 모두 저장(이전 수가 다르면 1이므로 초기화 1로 함)
        for j in range(1, n):
            if a[i][j] == a[i][j-1]: #이전 것과 같다면=연속 부분 찾는 것 TODO: 이전과 같은걸 찾을 때 왜 j-1?
                cnt = cnt + 1 #cnt 증가
            else: #이전 것과 다르면
                cnt = 1 #다시 1로 초기화
            if cnt > ans:
                ans = cnt #ans 갱신하기(최대값을 찾는 것)
    #열 순회하면서 연속되는 숫자 세기
    for i in range(start_col, end_col+1): #몇번열부터 몇번열까지 검사해라
        cnt = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt = cnt + 1
            else:
                cnt = 1
            if cnt > ans:
                ans = cnt
    return ans

N = int(input())
a = [list(input()) for _ in range(N)]
ans = 0
# 한칸[i,j]고르기 -> 오른쪽,아래만 검사하면 됨
for i in range(N):
    for j in range(N):
        if j+1 < N: #TODO: 이 조건이 뭔지 생각하기
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j] #두칸 서로 바꿔주고(swap)
            temp = check(a,i,i,j,j+1) #i행의 j열,j+1열을 check으로 계산을 해보고 최대값이면
            if ans < temp:
                ans = temp #ans에 바꿔 넣어줌
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j] #★★마지막에 이줄 쓰는 이유: 원래 상태로 배열을 바꾸는 부분!!
        if i+1 < N: #TODO: 이 조건이 뭔지 생각하기
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
            temp = check(a,i,i+1,j,j) #j열의 i행,i+1행을 check으로 계산을 해보고 최대값이면
            if ans < temp:
                ans = temp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j] #★★마지막에 이줄 쓰는 이유: 원래 상태로 배열을 바꾸는 부분!!
print(ans)