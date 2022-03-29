# 최단경로
# 다익스트라

from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(20001)]
for _ in range(E):
	u, v, w = map(int, input().split())
	edges[u].append((w, v))

answer = [None]*20001
que = PriorityQueue()
answer[K] = 0
for edge in edges[K]:
	que.put(edge)

while not que.empty():
	weight, node = que.get()
	if answer[node] == None or answer[node] > weight:
		answer[node] = weight
		for next_weight, next_node in edges[node]:
			que.put((weight+next_weight, next_node))

for i in range(1, V+1):
	if answer[i]==None:
		print("INF")
	else:
		print(answer[i])
