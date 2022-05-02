# 학교가지마
# 정점에서 정점까지 이동을 막으려면 몇개의 벽을 세워야 하는가?
# 정점에서 정점까지의 최대유량으로 해결
# 간선을 막는게 아니라 정점을 막아야하기 때문에 in정점, out정점이 필요함

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = []
for _ in range(N):
	mp.append(input())

# 0~N*M : in / N*M~N*M*2 : out
graph = [[] for _ in range(N*M*2)]
flow = [{} for _ in range(N*M*2)]

st, ed = 0, 0
vec = [[1,0],[0,1],[-1,0],[0,-1]]
for i in range(N):
	for j in range(M):
		if mp[i][j] == '#':
			continue
		graph[i*M+j].append((i*M+j + N*M, 1))
		if mp[i][j] == 'K':
			st = i*M+j + N*M
		if mp[i][j] == 'H':
			ed = i*M+j
		for vy, vx in vec:
			y = i + vy
			x = j + vx
			if 0<=y<N and 0<=x<M and mp[y][x]!='#':
				graph[i*M+j + N*M].append((y*M+x , 1))
				graph[i*M+j].append((y*M+x + N*M , 0))
				# 중요 포인트, 용량 0짜리 간선 추가해서 in -> out 으로 되돌아가는 길 탐색 필요

for i in range(N*M*2):
	for node, _ in graph[i]:
		flow[node][i] = 0
		flow[i][node] = 0

def bfs(visit):
	que = deque()
	que.append(st)
	visit[st] = st
	while len(que) > 0:
		node = que.popleft()
		if node == ed:
			return True
		for to, capacity in graph[node]:
			if visit[to] == -1 and (capacity-flow[node][to]) > 0:
				que.append(to)
				visit[to] = node
	return False

answer = 0
while True:
	visit = [-1]*N*M*2
	if bfs(visit) == False:
		break
	node = visit[ed]
	to = ed
	while node!=to:
		flow[node][to] += 1
		flow[to][node] -= 1
		to = node
		node = visit[node]
	answer+=1
st_y = (st-N*M)//M
st_x = (st-N*M)%M
ed_y = ed//M
ed_x = ed%M
if abs(st_y - ed_y) == 0 and abs(st_x - ed_x) == 1:
	print(-1)
elif abs(st_y - ed_y) == 1 and abs(st_x - ed_x) == 0:
	print(-1)
else:
	print(answer)