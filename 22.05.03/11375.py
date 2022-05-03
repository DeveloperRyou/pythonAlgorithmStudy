# 열혈강호
# 직원 : N, 일 : M
# 직원이 할수있는 일의 목록이 있을 때, 몇개의 일을 할수 있는지?
# 이분매칭으로 해결 (dfs, V*E)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph_from = [[] for _ in range(N)]
graph_to = [[] for _ in range(M)]
for i in range(N):
	lst = list(map(int, input().split()))[1:]
	for work in lst:
		graph_from[i].append(work-1)
		graph_to[work-1].append(i)

match_from = [-1] * N
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
for i in range(N):
	visit = [False] * N
	if match_from[i] == -1 and dfs(visit, i):
		answer += 1
print(answer)