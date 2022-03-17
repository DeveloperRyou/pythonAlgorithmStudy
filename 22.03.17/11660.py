# 2차원 구간합 구하기
# DP로 쭉 긁고 빼주면 끝

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
DP = []
DP.append([0]*(N+1))
for _ in range(N):
    DP.append([0]*(N+1))

for i in range(1, N+1):
    for j in range(1, N+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] + mp[i-1][j-1] - DP[i-1][j-1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(DP[y2][x2] - DP[y1-1][x2] - DP[y2][x1-1] + DP[y1-1][x1-1])