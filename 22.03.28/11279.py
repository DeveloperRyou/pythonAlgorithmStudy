# 우선순위큐, 최댓값 기준

import sys
input = sys.stdin.readline

from queue import PriorityQueue

que = PriorityQueue()
N = int(input())
for _ in range(N):
	a = int(input())
	if a == 0:
		if que.empty():
			print(0)
		else:
			print(que.get()[1])
	else:
		que.put((-a,a))
