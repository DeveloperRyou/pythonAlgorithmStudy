# N이 20이고 N개의 항을 가지는 수열의 부분수열(말만 부분수열이고 사실 부분집합)을 구해보자
# N이 작으니 무지성 반복문 
# 부분집합의 개수 : 2^N 
# 시간복잡도 2^N * N (정렬에서 log 2^n = n * log2)

N = int(input())
arr = list(map(int, input().split()))
subarr = []

for bit in range(pow(2, N)):
    res = 0
    binary = list(map(int, bin(bit)[2:]))
    while len(binary) != N:
        binary.insert(0,0)
    for idx in range(N):
        if binary[idx]:
            res += arr[idx]
    subarr.append(res)

subarr.sort()
idx = 1
for item in subarr:
    if idx < item:
        break
    if idx == item:
        idx += 1
print(idx)