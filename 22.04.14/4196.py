# 도미노
# SCC로 묶고 해당 SCC가 화살표를 안받으면 count
# 1 <-> 2
# 3 -> 4 -> 5 라면
# 1, 3 카운트
# pypy로 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

cnt = 0
stack = []
SCC = []

def DFS(node, graph, dfsn, finished):
	global cnt
	global stack
	global SCC
	dfsn[node] = cnt
	parent_node = cnt
	cnt += 1

	stack.append(node)
	for next in graph[node]:
		if dfsn[next] == -1:
			parent_node = min(parent_node, DFS(next, graph, dfsn, finished))
		elif finished[next] == False:
			parent_node = min(parent_node, dfsn[next])
	
	if dfsn[node] == parent_node:
		new = []
		while True:
			top = stack.pop()
			new.append(top)
			finished[top] = True
			if top == node:
				break
		SCC.append(new)

	return parent_node

T = int(input())
for t in range(T):
	cnt = 0
	stack = []
	SCC = []
	N, M = map(int, input().split())
	graph = [ [] for _ in range(N+1) ]	
	rev_graph = [ [] for _ in range(N+1) ]
	for m in range(M):
		a, b = map(int, input().split())
		graph[a].append(b)
		rev_graph[b].append(a)
	finished = [False] * (N+1)
	dfsn = [-1] * (N+1)
	for idx in range(1, N+1):
		if finished[idx] == False:
			DFS(idx, graph, dfsn, finished)
	answer = 0
	for lst in SCC:
		flag = True
		for node in lst:
			for next in rev_graph[node]:
				if next not in lst:
					flag = False
		if flag:
			answer += 1
	print(answer)
