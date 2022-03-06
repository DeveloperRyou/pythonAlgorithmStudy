# 로프를 적게쓰는게 최대일 수도 있음
# 정렬 이후 계산이 필요
# 최솟값 * 로프 갯수 = 들어올릴 수 있는 중량
# 반복하면서 최대 중량 찾기

import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
mx = 0
for i in range(N):
    mx = max(arr[i] * (N - i), mx)
print(mx)