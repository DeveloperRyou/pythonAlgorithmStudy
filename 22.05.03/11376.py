# 열혈강호 2
# 직원 : N, 일 : M
# 직원이 최대 2개 일을 할수 있음, 일은 한사람이 해야함
# 직원 노드를 2개 만듬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph_from = [[] for _ in range(N*2)]
graph_to = [[] for _ in range(M)]
for i in range(N):
	lst = list(map(int, input().split()))[1:]
	for work in lst:
		graph_from[i].append(work-1)
		graph_to[work-1].append(i)
		graph_from[i+N].append(work-1)
		graph_to[work-1].append(i+N)

match_from = [-1] * (N*2)
match_to = [-1] * M

def dfs(visit, node):
	visit[node] = True
	for to in graph_from[node]:
		# 노드가 이어져있지 않음 or 이어져있는 전 노드에서 dfs
		if match_to[to] == -1 or \
			(visit[match_to[to]] == False and dfs(visit, match_to[to])):
			match_from[node] = to
			match_to[to] = node
			return True
	return False

answer = 0
for i in range(N*2):
	visit = [False] * (N*2)
	if match_from[i] == -1 and dfs(visit, i):
		answer += 1
print(answer)