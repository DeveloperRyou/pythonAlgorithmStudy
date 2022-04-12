# 음악 프로그램
# 위상 정렬
# 순서대로 포인팅을 해주고 포인팅 받지 않는 노드 큐에 넣고 돌리기

from collections import deque


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
pointed = [0]*(N+1)

for _ in range(M):
	lst = list(map(int, input().split()))
	for i in range(1, len(lst)-1):
		graph[lst[i]].append(lst[i+1])
		pointed[lst[i+1]] += 1

que = deque()
for idx in range(1, N+1):
	if pointed[idx] == 0:
		que.append(idx)

answer = []
while len(que)>0:
	idx = que.popleft()
	answer.append(idx)
	for node in graph[idx]:
		pointed[node] -= 1
		if pointed[node] == 0:
			que.append(node)

if len(answer) != N:
	print(0)
else:
	for item in answer:
		print(item)