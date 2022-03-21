# 계단수 찾기
# 계단수는 DP로 찾기
# 1 로 시작하는 3칸 계단수 = 0으로 시작하는 2칸 계단수 + 2로 시작하는 2칸 계단수
# 마지막에서는 1부터 9까지만 더해서 출력

DP = [ [1] * 10 for _ in range(101) ]
N = int(input())

for n in range(2, N+1):
    DP[n][0] = DP[n-1][1]
    for i in range(1, 9):
        DP[n][i] = (DP[n-1][i-1] + DP[n-1][i+1])%1000000000
    DP[n][9] = DP[n-1][8]

answer = 0
for i in range(1, 10):
    answer += DP[N][i]
print(answer%1000000000)
