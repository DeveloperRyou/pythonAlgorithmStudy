# 우선순위큐
# 내부적으로는 heapq 로 구현되어있음
# 직접구현도 시도

import sys

input = sys.stdin.readline
"""
from queue import PriorityQueue
"""
class PriorityQueue:
	def __init__(self):
		self.size = 0
		self.que = [0]*100001
	def empty(self):
		if self.size == 0:
			return True
		return False
	def topdown_priority(self):
		idx = 0
		while idx*2+1 < self.size:
			if idx*2+2 < self.size and self.que[idx*2+1] > self.que[idx*2+2]:
				if self.que[idx] > self.que[idx*2+2]:
					self.que[idx], self.que[idx*2+2] = self.que[idx*2+2], self.que[idx]
				else:
					break
				idx = idx*2+2
			else:
				if self.que[idx] > self.que[idx*2+1]:
					self.que[idx], self.que[idx*2+1] = self.que[idx*2+1], self.que[idx]
				else:
					break
				idx = idx*2+1
	def bottomup_priority(self):
		idx = self.size-1
		while idx>0:
			if self.que[(idx-1)//2] > self.que[idx]:
				self.que[(idx-1)//2], self.que[idx] = self.que[idx], self.que[(idx-1)//2]
			else:
				break
			idx = (idx-1)//2
	def get(self):
		res = self.que[0]
		self.que[0] = self.que[self.size-1]
		self.size -= 1
		self.topdown_priority()
		return res
	def put(self, data):
		self.que[self.size] = data
		self.size += 1
		self.bottomup_priority()

que = PriorityQueue()
N = int(input())
for _ in range(N):
	a = int(input())
	if a == 0:
		if que.empty():
			print(0)
		else:
			print(que.get())
	else:
		que.put(a)
