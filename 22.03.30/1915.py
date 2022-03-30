# 가장큰 정사각형 찾기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mp = [input().rstrip() for _ in range(N)]

dp_left = [[0]*M for _ in range(N)]
dp_down = [[0]*M for _ in range(N)]
dp_square = [[0]*M for _ in range(N)]

for i in range(N):
	for j in range(M):
		temp = 0
		if j>0:
			temp = dp_left[i][j-1]
		if mp[i][j] == '1':
			dp_left[i][j] = temp + 1

for j in range(M):
	for i in range(N):
		temp = 0
		if i>0:
			temp = dp_down[i-1][j]
		if mp[i][j] == '1':
			dp_down[i][j] = temp + 1

answer = 0
for i in range(N):
	for j in range(M):
		length = min(dp_left[i][j], dp_down[i][j])
		if length>=1:
			temp = 0
			if i>0 and j>0:
				temp = dp_square[i-1][j-1]
			dp_square[i][j] = min(length, temp+1)
			answer = max(answer, dp_square[i][j])
print(answer**2)