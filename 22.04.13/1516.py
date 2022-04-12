# 게임 개발
# 위상 정렬
# 필요한 건물이 없는 건물을 큐에 넣고 큐를 계속 돌린다

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
pointed = [0]*(N+1)
weight = [0]*(N+1)

for idx in range(1, N+1):
	lst = list(map(int, input().split()))
	weight[idx] = lst[0]
	for i in range(1, len(lst)):
		if lst[i] == -1:
			break
		graph[lst[i]].append(idx)
		pointed[idx] += 1

que = deque()
for idx in range(1, N+1):
	if pointed[idx] == 0:
		que.append(idx)

answer = [0]*(N+1)
while len(que)>0:
	idx = que.popleft()
	answer[idx] += weight[idx]
	for node in graph[idx]:
		pointed[node] -= 1
		if pointed[node] == 0:
			que.append(node)
		answer[node] = max(answer[node], answer[idx])

for idx in range(1, N+1):
	print(answer[idx])