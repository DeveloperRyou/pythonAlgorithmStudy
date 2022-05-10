# 최소공통조상
# 조상 찾는걸 logn으로 해서 빠르게 해결
# pypy로 해결

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())
lst = [[] for _ in range(N)]
for i in range(N-1):
	a, b = map(int, input().split())
	lst[a-1].append(b-1)
	lst[b-1].append(a-1)
parent = [[-1]*20 for _ in range(N)]
depth = [-1] * N
depth[0] = 0

def makeTree(node):
	for to in lst[node]:
		if depth[to] == -1:
			parent[to][0] = node
			depth[to] = depth[node] + 1
			makeTree(to)
makeTree(0)
# dp로 parent 채우기
for j in range(20):
	for i in range(N):
		if parent[i][j] != -1:
			parent[i][j+1] = parent[parent[i][j]][j]


M = int(input())
for _ in range(M):
	a, b = map(int, input().split())
	a-=1
	b-=1
	if depth[a] < depth[b]:
		a, b = b, a
	# a가 더 깊음
	size = depth[a] - depth[b]
	idx = 0
	while size!=0:
		if size % 2 == 1:
			a = parent[a][idx]
		size//=2
		idx+=1
	# 높이 같아짐

	if a!=b:
		for idx in range(19,-1,-1):
			if parent[a][idx] != -1 and parent[b][idx] != -1 \
				and parent[a][idx]!=parent[b][idx]:
				a = parent[a][idx]
				b = parent[b][idx]
		a = parent[a][0]
	print(a+1)

