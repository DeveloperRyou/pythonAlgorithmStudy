# 가장큰 부분합 구하기
# n = 100000
# 

N = int(input())
arr = list(map(int, input().split()))
prefix = [0] * N
prefix[0] = arr[0]

for i in range(1, N):
    prefix[i] = max(prefix[i-1] + arr[i], arr[i])

mx = -100000001
for item in prefix:
    if item > mx:
        mx = item
print(mx)