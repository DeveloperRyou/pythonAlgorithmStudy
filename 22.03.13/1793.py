# 타일링 DP연습문제

DP = [0] * 251
DP[0] = 1
DP[1] = 1
DP[2] = 3
for i in range(3, 251):
    DP[i] = DP[i-1] + 2 * DP[i-2]

while True:
    try:
        N = int(input())
        print(DP[N])
    except:
        break