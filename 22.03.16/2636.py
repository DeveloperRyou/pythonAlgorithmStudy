# 치즈
# 공기를 9로 색칠하고, 공기와 닿아있는 치즈를 지우면서 개수를 세리기
# 치즈가 언제 다 없어지는지 확인하고 출력

N, M = map(int, input().split())
mp = []
mp.append([0] * (M+2))
for _ in range(N):
    t = list(map(int, input().split()))
    t.insert(0, 0)
    t.append(0)
    mp.append(t)
mp.append([0] * (M+2))
N += 2
M += 2

import sys
sys.setrecursionlimit(20000)

def find_air(y, x):
    if (0<=y<N and 0<=x<M) and mp[y][x] == 0:
        mp[y][x] = 9
        find_air(y+1,x)
        find_air(y,x+1)
        find_air(y-1,x)
        find_air(y,x-1)

def find_cheese():
    answer = 0
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                if (mp[i+1][j] == 9 or
                    mp[i][j+1] == 9 or
                    mp[i-1][j] == 9 or
                    mp[i][j-1] == 9): # 주변에 공기 있을때

                    mp[i][j] = 0
                    answer += 1
    return answer

def is_break():
    flag = 1
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 1:
                flag = 0
            if mp[i][j] == 9:
                mp[i][j] = 0
    return flag


def solution():
    time = 0
    answer = 0
    while True:
        if is_break():
            print(time)
            print(answer)
            return 

        find_air(0, 0)
        answer = find_cheese()
        time += 1

solution()