# 본대탈출 3
# 움직이지 않았을때 1 0 0 0 0 ... 0
# 인접행렬을 곱해준다(행렬곱)
# 1 0 0 0 ... -> 0 1 1 1 ... -> ??? -> ??? 에서 첫번째 인덱스가 가능한 경로수
# log D로 동작 가능

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0]*N for _ in range(N)]

for _ in range(M):
	a, b = map(int, input().split())
	graph[a-1][b-1] = 1
	graph[b-1][a-1] = 1

D = int(input())

dic = {1:graph}

def multi(g1, g2):
	res = [[0]*N for _ in range(N)]
	for i in range(N):
		for j in range(N):
			for k in range(N):
				res[i][j] = (res[i][j] + g1[i][k]*g2[k][j])%1000000007
	return res

def find(n):
	if n in dic:
		return dic[n]
	if n%2 == 0:
		dic[n] = multi(find(n//2), find(n//2))
		return dic[n]
	else:
		dic[n] = multi(find(n-1), dic[1])
		return dic[n]

print(find(D)[0][0])
