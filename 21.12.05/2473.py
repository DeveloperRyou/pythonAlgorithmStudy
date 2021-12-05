# N=5000, N^3은 불가능, N^2로 해결
# 정렬 이후 가운데 인덱스 순회하면서 양방향으로 투포인터 탐색
# pypy로 해결

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 정렬
arr.sort()

minimum = 9999999999
answer = [0,0,0]
# 가운데 인덱스 순회
for mid in range(1, N-1):
    left = mid-1
    right = mid+1
    while left>=0 and right<N:
        sum = arr[left]+arr[mid]+arr[right]
        if minimum>abs(sum):
            minimum = abs(sum)
            answer = [left,mid,right]
        if sum>0:
            left = left - 1
        else:
            right = right + 1
print(arr[answer[0]], arr[answer[1]], arr[answer[2]], sep=' ')