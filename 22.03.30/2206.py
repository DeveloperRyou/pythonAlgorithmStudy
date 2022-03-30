# 벽 부수고 이동하기
# 벽은 한개만 부술 수 있음
# 출발, 도착점에서 각각 bfs 하고 벽 기준으로 확인
# pypy로 통과

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [input() for _ in range(N)]

INF = 99999999
bfs_s = [[INF]*M for _ in range(N)]
bfs_e = [[INF]*M for _ in range(N)]

def BFS(mp_bfs, s_y, s_x):
	que = deque()
	que.append((s_y, s_x, 1))
	vec = [[1, 0],[-1, 0],[0, 1],[0, -1]]
	while len(que)>0:
		y, x, weight= que.popleft()
		if mp_bfs[y][x] == INF and mp[y][x] == '0':
			mp_bfs[y][x] = weight
			for vy, vx in vec:
				if 0<=y+vy<N and 0<=x+vx<M:
					que.append((y+vy, x+vx, weight+1))

BFS(bfs_s, 0, 0)
BFS(bfs_e, N-1, M-1)

answer = bfs_e[0][0]

vec = [[1, 0],[-1,0],[0,1],[0,-1]]
for i in range(N):
	for j in range(M):
		if mp[i][j] == '1':
			for y1, x1 in vec:
				for y2, x2 in vec:
					if 0<=i+y1<N and 0<=j+x1<M and 0<=i+y2<N and 0<=j+x2<M:
						temp = bfs_s[i+y1][j+x1] + bfs_e[i+y2][j+x2] + 1
						answer = min(temp, answer)
if answer == INF:
	answer = -1
print(answer)
