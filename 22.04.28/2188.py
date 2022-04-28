# 축사배정
# 소가 축사에 최대 몇마리 들어갈 수 있는가?
# 최대유량으로 해결
# st에서 소들로 용량 1인 간선, 소들에서 축사로 용량 1인 간선, 축사에서 ed로 용량1인 간선 (단방향)
# st에서 ed로 최대 유량 = 최대 소
# 행렬 : 시간초과
# 리스트로 바꿔보기? 그래도 시간초과
# dfs에서 깊이가 너무 깊어지는게 문젠가?
# bfs로 바꿔서 해결

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
st = 0
ed = 401

capacity = [[] for _ in range(402)]
flow = [[0]*402 for _ in range(402)]

for cow in range(1, N+1):
	capacity[st].append(cow)
for room in range(N+1, N+M+1):
	capacity[room].append(ed)

for cow in range(1, N+1):
	lst = list(map(int, input().split()))
	for room in range(1, lst[0]+1):
		capacity[cow].append(N+lst[room])
		capacity[N+lst[room]].append(cow)

def bfs():
	visit = [False]*402
	que = deque()
	que.append(st)
	while len(que)>0:
		node = que.popleft()
		for to in capacity[node]:
			if visit[to] == False:
				if to > node: # 소에서 축사 넣을때 (정방향)
					w = 1 - flow[node][to]
				else : # 축사에서 소 뺄때 (역방향)
					w = 0 - flow[node][to]
				if w > 0:
					visit[to] = node
					if to == ed:
						break
					que.append(to)
		if visit[ed] != False:
			res = deque()
			res.appendleft(ed)
			before = visit[ed]
			while before != st:
				res.appendleft(before)
				before = visit[before]
			res.appendleft(st)
			return res
	return None

answer = 0
while True:
	res = bfs()
	if res is None:
		break
#	print(res)
	path_st = res.popleft()
	while len(res) > 0:
		path_ed = res.popleft()
		flow[path_st][path_ed] += 1
		flow[path_ed][path_st] -= 1
		path_st = path_ed
	answer += 1
print(answer)