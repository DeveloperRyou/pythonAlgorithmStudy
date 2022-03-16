# 피보나치 확장
# 음수일반항을 구해보자
# f(n-2) = f(n) - f(n-1) -> f(n) = f(n+2) - f(n+1)

N = int(input())
DP = [0]*2000001
mid = 1000000
MAX = 2000001
DP[mid+1] = 1
DP[mid-1] = 1

for i in range(mid+2, MAX):
    DP[i] = (DP[i-1] + DP[i-2])%1000000000
for i in range(mid-2, -1, -1):
    DP[i] = (DP[i+2] - DP[i+1])%1000000000 if (DP[i+2] - DP[i+1]) > 0 else (DP[i+2] - DP[i+1])%-1000000000

if DP[mid + N] > 0:
    print(1)
elif DP[mid + N] < 0:
    print(-1)
else:
    print(0)
print(abs(DP[mid + N]))
