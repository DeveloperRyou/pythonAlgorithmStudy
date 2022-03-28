# 수강신청
# 해시테이블 활용해보자 (딕셔너리로도 구현 가능)

class HashTable:
	def __init__(self):
		self.hashsize = 100007
		self.hashtable = [[] for _ in range(self.hashsize)]
	def key_to_idx(self, key):
		return int(key) % self.hashsize
	def iskey(self, key):
		idx = self.key_to_idx(key)
		res = False
		for data in self.hashtable[idx]:
			if data[0] == key:
				res = True
		return res
	def push(self, key, value):
		idx = self.key_to_idx(key)
		if self.iskey(key) is False:
			self.hashtable[idx].append([key, value])
		else:
			for data in self.hashtable[idx]:
				if data[0] == key:
					data[1] = value
	def getlist(self):
		lst = []
		for each_lst in self.hashtable:
			for data in each_lst:
				lst.append(data)
		return lst

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hashTable = HashTable()
for i in range(M):
	num = input().rstrip()
	hashTable.push(num, i)
lst = hashTable.getlist()
lst.sort(key = lambda x:x[1])
for i in range(min(N, len(lst))):
	print(lst[i][0])
"""
dic = {}
for i in range(M):
	num = input().rstrip()
	dic[num]=i
lst = []
for key in dic:
	lst.append([key, dic[key]])
lst.sort(key = lambda x:x[1])
for i in range(min(N, len(lst))):
	print(lst[i][0])
"""