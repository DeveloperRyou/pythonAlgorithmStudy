# 쉬운 최단거리
# bfs이용해서 찾기

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(N)]
ans = [[None]*M for _ in range(N)]

que = deque()
vec = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(N):
	for j in range(M):
		if mp[i][j] == 2:
			que.append((i, j, 0))
while len(que)>0:
	y, x, dist = que.popleft()
	if 0<=y<N and 0<=x<M and ans[y][x] == None:
		if mp[y][x] != 0:
			ans[y][x] = dist
			for vy, vx in vec:
				que.append((y+vy, x+vx, dist+1))
for i in range(N):
	for j in range(M):
		if ans[i][j] == None:
			if mp[i][j] == 0:
				print(0, end=' ')
			else:
				print(-1, end=' ')
		else:
			print(ans[i][j], end=' ')
	print()
