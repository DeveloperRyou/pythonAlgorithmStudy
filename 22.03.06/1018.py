# N*M*128 1억보다 작음
# 브루트포스
# 미리 가능한 배열 만든 후 검사

import sys
input = sys.stdin.readline

def check_mp(idx_y, idx_x, mp, is_white):
    temp_white = "WBWBWBWB"
    temp_black = "BWBWBWBW"
    temp_mp = []
    if is_white:
        for _ in range(4):
            temp_mp.append(temp_white)
            temp_mp.append(temp_black)
    else:
        for _ in range(4):
            temp_mp.append(temp_black)
            temp_mp.append(temp_white)
    cnt = 0
    for i in range(8):
        for j in range(8):
            if mp[idx_y + i][idx_x + j] != temp_mp[i][j]:
                cnt += 1
    return cnt

N, M = map(int, input().split())
mp = []
for _ in range(N):
    mp.append(input())
mn = 128
for idx_y in range(N - 7):
    for idx_x in range(M - 7):
        mn = min(check_mp(idx_y, idx_x, mp, 1), mn)
        mn = min(check_mp(idx_y, idx_x, mp, 0), mn)
print(mn)