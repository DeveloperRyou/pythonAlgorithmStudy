# 타일채우기 3*N
# N = 30

DP = [0] * 31
DP[2] = 3
DP[4] = DP[2] * DP[2] + 2
for i in range(6, 31, 2):
    s = 0
    for j in range(i-4, 0, -2):
        s += DP[j] * 2
    DP[i] = DP[i-2] * 3 + s + 2
N = int(input())
print(DP[N])