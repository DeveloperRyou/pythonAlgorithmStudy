# 물통

from collections import deque

A, B, ans_A, ans_B = map(int, input().split())

def strs(a, b):
	return (str(a)+','+str(b))

def BFS():
	que = deque()
	que.append((0, 0, 0))
	dp = {}
	while len(que)>0:
		cur_A, cur_B, weight = que.popleft()
		if cur_A == ans_A and cur_B == ans_B:
			return weight
		if strs(cur_A, cur_B) in dp:
			continue
		dp[strs(cur_A, cur_B)] = weight
		# A
		if cur_B != 0:
			que.append((0, cur_B, weight+1))
		if cur_A != 0 and cur_B != B:
			que.append((max(0, cur_A+cur_B-B), min(cur_B+cur_A, B), weight+1))
		if cur_A != A:
			que.append((A, cur_B, weight+1))
		# B
		if cur_A != 0:
			que.append((cur_A, 0, weight+1))
		if cur_B != 0 and cur_A != A:
			que.append((min(cur_A+cur_B, A), max(0, cur_B+cur_A-A), weight+1))
		if cur_B != B:
			que.append((cur_A, B, weight+1))
	return -1

print(BFS())