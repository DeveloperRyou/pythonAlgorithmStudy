# 내리막길 찾기
# 우측 하단 모서리 부분은 접근가능한 경로가 2곳 (위, 왼쪽) 밖에 없음
# 다른곳에서는 상하좌우 다 접근 가능
# 우하단서부터 재귀로 경우의수 더하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(300000) # 맵 크기 250000

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
DP = [[None]*M for _ in range(N)]
DP[0][0] = 1

def rec(y, x):
    if DP[y][x] != None:
        return DP[y][x]
    if y == N-1 or x == M-1:
        left, up = 0, 0
        if x-1 >= 0 and mp[y][x-1] > mp[y][x]:
            left = rec(y, x-1)
        if y-1 >= 0 and mp[y-1][x] > mp[y][x]:
            up = rec(y-1, x)
        DP[y][x] = left+up
        return left+up
    left, up, right, down = 0, 0, 0, 0
    if x-1 >= 0 and mp[y][x-1] > mp[y][x]:
        left = rec(y, x-1)
    if y-1 >= 0 and mp[y-1][x] > mp[y][x]:
        up = rec(y-1, x)
    if x+1 >= 0 and mp[y][x+1] > mp[y][x]:
        right = rec(y, x+1)
    if y+1 >= 0 and mp[y+1][x] > mp[y][x]:
        down = rec(y+1, x)
    DP[y][x] = left+up+right+down
    return left+up+right+down

print(rec(N-1, M-1))