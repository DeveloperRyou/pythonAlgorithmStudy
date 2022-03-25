# 벽장문
# 벽장문을 사용하기 위해서 움직여야 하는 벽장문의 최소를 출력
# XXOXXXOXX 에서 1번 벽장문 사용시
# OXXXXXOXX 가 됨 (열려있는 벽장문 - 열어야 하는 벽장문 = 움직인 벽장문)
# 1, 4, 5 일 경우 예로 (XXOXXXOXX -> OXXXXXOXX -> OXXOXXXXX -> OXXXOXXXX) 이런 식으로 움직임
# 가장 가까운 문을 움직이는게 정답이 아님
# 벽장문은 최대 20개, 20개중 2개 열려있으니 20C2개 경우의수
# DP[벽장문 여는 순서][20**2]
# 두번째 인덱스 % N, // N 으로 열려있는 벽장문 확인
# 현재 벽장문을 만들기 위해서 움직여야하는 벽장문 계산하고 DP에 적용

N = int(input())
a, b = map(int, input().split())
if a > b: # b가 항상 크게
	a, b = b, a
M = int(input())
arr = [int(input()) for _ in range(M)]

DP = [[999999]*(N*N+N) for _ in range(M+1)]
DP[0][b*N+a] = 0

def checkmin(i, idx):
	a = idx%N
	b = idx//N
	res = 999999
	for idx_a in range(1, N+1):
		for idx_b in range(idx_a+1, N+1):
			res = min(res, abs(idx_a-a)+abs(idx_b-b)+DP[i][idx_b*N+idx_a])
	return res

for i in range(M):
	# N=5 ,val=3이면 XOXOO, OXXOO, OOXXO, OOXOX 가능 (16, 17, 23, 28)
	val = arr[i]
	for j in range(1, N+1):
		if j == val:
			continue
		if j < val:
			idx = val*N+j
			DP[i+1][idx] = checkmin(i, idx)
		else:
			idx = j*N+val
			DP[i+1][idx] = checkmin(i, idx)

print(min(DP[M]))