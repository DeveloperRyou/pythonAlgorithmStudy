# 정사각형의 크기 최대에서 줄여가면서 만족하는지 확인

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = []
for _ in range(N):
    mp.append(input())

len_sq = min(N, M)
while len_sq > 1:
    flag = 0
    for idx_y in range(N-len_sq+1):
        for idx_x in range(M-len_sq+1):
            if mp[idx_y][idx_x] == mp[idx_y][idx_x+len_sq-1] and \
                mp[idx_y][idx_x] == mp[idx_y+len_sq-1][idx_x] and \
                mp[idx_y][idx_x] == mp[idx_y+len_sq-1][idx_x+len_sq-1]:
                flag = 1
    if flag:
        break
    len_sq -= 1

print(len_sq*len_sq)