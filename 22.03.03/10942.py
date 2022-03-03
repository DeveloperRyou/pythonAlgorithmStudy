# N = 2000 수열, M = 1000000개 질문
# 미리 질문에 대한 답 N^2개를 구한 뒤 접근
# 답은 DP로 채워 넣어 O(N^2) 달성
# 답찾기 200만, 질문 100만으로 해결

import sys
input = sys.stdin.readline
N = int(input())
N_arr = list(map(int, input().split()))
N_arr.insert(0,0)

table = [[]]
for i in range(1,N+1):
    table.append([])
    for _ in range(N+1):
        table[i].append(0)

def pal(st, ed):
    if st == ed:
        return 1
    if st+1 == ed:
        if N_arr[st] == N_arr[ed]:
            return 1
        else:
            return 0
    if N_arr[st] == N_arr[ed] and table[st+1][ed-1] == 1:
        return 1
    return 0
    

for sep in range(N):
    for idx in range(1, N+1-sep):
        table[idx][idx+sep] = pal(idx, idx+sep)

M = int(input())
for _ in range(M):
    st, ed = map(int, input().split())
    print(table[st][ed])