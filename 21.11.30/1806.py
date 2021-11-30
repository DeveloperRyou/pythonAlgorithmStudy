# 투포인터 -> 시간복잡도 N
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

idx1 = 0
idx2 = 0
MAX = 9999999999
answer = MAX
prifixSum = 0
while idx2<=N and idx1<=idx2:
    if prifixSum < S:
        # 마지막 인덱스 확인을 위한 조건문
        if idx2 == N:
            break
        prifixSum = prifixSum + arr[idx2]
        idx2 = idx2 + 1
    else:
        answer = min(answer, idx2-idx1)
        prifixSum = prifixSum - arr[idx1]
        idx1 = idx1 + 1

if answer == MAX:
    print(0)
else:
    print(answer)
