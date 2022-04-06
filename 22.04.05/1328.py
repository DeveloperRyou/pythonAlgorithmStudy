# 고층빌딩
# DP
# [건물개수][왼쪽][오른쪽]
# 건물을 추가할 때 가장 작은 높이의 건물을 추가한다고 가정
# 왼쪽, 오른쪽 추가할 때는 낮은 높이의 건물이 보임
# 중간 사이사이 추가할 때는 안보임

N, L, R = map(int, input().split())

DP = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
DP[1][1][1] = 1
for level in range(1, N):
	for i in range(1, N+1):
		for j in range(1, N+1):
			if DP[level][i][j] > 0:
				DP[level+1][i][j+1] = (DP[level+1][i][j+1] + DP[level][i][j])%1000000007
				DP[level+1][i+1][j] = (DP[level+1][i+1][j] + DP[level][i][j])%1000000007
				DP[level+1][i][j] = (DP[level+1][i][j] + DP[level][i][j]*(level-1))%1000000007
print(DP[N][L][R])