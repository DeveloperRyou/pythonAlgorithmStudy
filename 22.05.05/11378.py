# 열혈강호 4
# 직원 : N, 일 : M, 벌점 : K
# 벌점 만큼 일 더할 수 있음

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
	lst = list(map(int, input().split()))
	for job in lst[1:]:
		graph[i].append(job-1)
	
def dfs(node, visit):
	visit[node]=True 
	for job in graph[node]:
		if match[job] == -1:
			match[job] = node
			return True
		elif visit[match[job]] == False and dfs(match[job], visit):
			match[job] = node
			return True
	return False

match = [-1] * M
answer = 0
for i in range(N):
	visit = [False] * N
	if dfs(i, visit):
		answer += 1
	
for i in range(N):
	visit = [False] * N
	if K == 0:
		break
	while dfs(i, visit):
		if K == 0:
			break
		answer += 1
		K -= 1
print(answer)