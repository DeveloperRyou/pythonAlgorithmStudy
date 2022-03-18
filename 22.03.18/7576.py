# 토마토
# BFS

from collections import deque

M, N = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
que = deque()

for i in range(N):
    for j in range(M):
        if mp[i][j] == 1:
            que.append((i, j, 0))

answer = 0
while len(que) != 0:
    y, x, level = que.popleft()
    answer = max(answer, level)
    if y-1 >= 0 and mp[y-1][x] == 0:
        mp[y-1][x] = 1
        que.append((y-1, x, level+1))
    if y+1 < N and mp[y+1][x] == 0:
        mp[y+1][x] = 1
        que.append((y+1, x, level+1))
    if x-1 >= 0 and mp[y][x-1] == 0:
        mp[y][x-1] = 1
        que.append((y, x-1, level+1))
    if x+1 < M and mp[y][x+1] == 0:
        mp[y][x+1] = 1
        que.append((y, x+1, level+1))

def print_answer():
    for i in range(N):
        for j in range(M):
            if mp[i][j] == 0:
                print(-1)
                return
    print(answer)

print_answer()