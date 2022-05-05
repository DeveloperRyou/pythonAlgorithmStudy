# 열혈강호 3
# 직원 : N, 일 : M, 2개일 : K
# 2개 일 할수 있는 직원 K명

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
graph = [[] for _ in range(N*2)]
for i in range(N):
	lst = list(map(int, input().split()))
	for job in lst[1:]:
		graph[i].append(job-1)
		graph[i+N].append(job-1)
	
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
	visit = [False] * 2*N
	if dfs(i, visit):
		answer += 1
for i in range(N, 2*N):
	visit = [False] * 2*N
	if dfs(i, visit):
		answer += 1
		K -= 1
	if K == 0:
		break
print(answer)