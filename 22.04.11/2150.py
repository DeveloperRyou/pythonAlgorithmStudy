# SCC 강한연결요소
# DFS로 돌면서 SCC확인
# DFS 도중 자신의 부모노드로 갈 수 있을 때 사이클 형성
# 스택에 담고 있다가 사이클 형성 안되는 순간 해당 노드까지 pop
# 부모노드는 dfsnum으로 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

V, E = map(int, input().split())
gragh = [[] for _ in range(V+1)]
for _ in range(E):
	a, b = map(int, input().split())
	gragh[a].append(b)

dfsnum = [-1]*(V+1)
finished = [False]*(V+1)
stack = []
SCC = []
cnt = 0

def DFS(node):
	global cnt
	stack.append(node)
	dfsnum[node] = cnt
	parent_node = cnt
	cnt += 1

	for next in gragh[node]:
		if dfsnum[next] == -1: # 자손노드로 DFS
			parent_node = min(parent_node, DFS(next))
		elif finished[next] == False: # 부모노드 또는 사이클 안의 노드 확인
			parent_node = min(parent_node, dfsnum[next])
	
	if parent_node == dfsnum[node]: # 자손노드 없을 떄 SSC 형성
		SCC.append([])
		while True:
			child_node = stack.pop()
			SCC[-1].append(child_node)
			finished[child_node] = True
			if child_node == node:
				break
	
	return parent_node

for i in range(1, V+1):
	if finished[i] == False:
		DFS(i)

for i in range(len(SCC)):
	SCC[i].sort()
SCC.sort(key=lambda x : x[0])

print(len(SCC))
for i in range(len(SCC)):
	for j in range(len(SCC[i])):
		print(SCC[i][j], end=' ')
	print(-1)