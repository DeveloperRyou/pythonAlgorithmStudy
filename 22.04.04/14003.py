# 가장 긴 증가하는 부분수열

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

"""
DP를 이용한 O(N^2)
10	20	30	15	50	40
1	2	3	2	4	4
그 전 인덱스를 탐색하고 증가상태를 만족할 때, 인덱스 값 + 1 저장
"""
"""
DP = [[] for _ in range(N)]
for i in range(N):
	temp = []
	for j in range(i):
		if arr[i]>arr[j] and len(temp)<len(DP[j]):
			temp = DP[j]
	for j in range(len(temp)):
		DP[i].append(temp[j])
	DP[i].append(arr[i])
answer = 0
answer_idx = -1
for i in range(N):
	if answer < len(DP[i]):
		answer = len(DP[i])
		answer_idx = i
print(answer)
for i in range(answer):
	print(DP[answer_idx][i], end = ' ')
"""
"""
이분탐색을 이용한 O(nlogn)
10	20	30	15	50	40
1	2	3	2	4	4
10	10	10	10	10	10
	20	20	152015201520
		30	30	30	30
				50	40
10	30	5	15	20	40
1	2	1	2	3	4
10	10	510 510	510	510
	30	30	153015301530
				20	20
					40
마지막에서 거꾸로 올라가면서 가능한것 중 큰거 선택
"""
DP = []
DP.append([-1000000001]) # 이분탐색에서 기준 필요
for idx in range(N):
	if DP[-1][-1] < arr[idx]:
		DP.append([arr[idx]])
	else:
		lo, hi = 0, len(DP)-1
		while lo + 1 != hi:
			mid = (lo+hi)//2
			if DP[mid][-1] < arr[idx]:
				lo = mid
			else:
				hi = mid
		DP[hi].append(arr[idx])
print(len(DP)-1)
#print(DP)
mx = 1000000001
answer=[]
for i in range(len(DP)-1,0,-1):
	DP[i].sort(reverse=True)
	for j in range(len(DP[i])):
		if mx > DP[i][j]:
			mx = DP[i][j]
			answer.append(mx)
			break
answer.reverse()
for i in range(len(answer)):
	print(answer[i], end=' ')