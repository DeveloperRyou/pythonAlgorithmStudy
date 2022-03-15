# 주어진 모양대로 한번 긁고
# 최대를 저장하면서 모든 맵 탐색
# 맵 사이즈가 250000이니 시간적인 고려 필요 X
# pypy로 해결

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*M for _ in range(N)]
vecY = [-1,0,0,1]
vecX = [0,1,-1,0]

def rec(y, x, dep):
    if not (0<=y and y<N and 0<=x and x<M) or check[y][x] == 1:
        return 0
    if dep == 4:
        return mp[y][x]
    
    check[y][x] = 1
    res = 0
    for i in range(4):
        res = max(res, rec(y+vecY[i], x+vecX[i], dep+1))
        if dep == 2:
            for j in range(i+1, 4):
               res = max(res, rec(y+vecY[i], x+vecX[i], 4) + rec(y+vecY[j], x+vecX[j], 4))
        
    check[y][x] = 0
    return res + mp[y][x]

answer = -1
for i in range(N):
    for j in range(M):
        answer = max(answer, rec(i, j, 1))
        
print(answer)