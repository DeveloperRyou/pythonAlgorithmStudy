# 움직이는 방향 4, 횟수 5 -> 4^5의 연산
# 재귀 전체탐색으로 해결
# range 사용 주의!

from collections import deque
import sys
input = sys.stdin.readline

def table_max(table):
    res = 0
    for i in range(N):
        for j in range(N):
            res = max(res, table[i][j])
    return res 

def table_change(table, type):
    if type == 0: # left
        for i in range(N):
            que = deque()
            for j in range(N):
                if table[i][j] != 0:
                    que.append(table[i][j])
                table[i][j] = 0
            idx = 0
            while que:
                fo = que.popleft()
                if table[i][idx] == 0:
                    table[i][idx] = fo
                elif table[i][idx] == fo:
                    table[i][idx] = fo*2
                    idx += 1
                else:
                    table[i][idx+1] = fo
                    idx += 1
    if type == 1: # right
        for i in range(N):
            que = deque()
            for j in range(N-1, -1, -1):
                if table[i][j] != 0:
                    que.append(table[i][j])
                table[i][j] = 0
            idx = N-1
            while que:
                fo = que.popleft()
                if table[i][idx] == 0:
                    table[i][idx] = fo
                elif table[i][idx] == fo:
                    table[i][idx] = fo*2
                    idx -= 1
                else:
                    table[i][idx-1] = fo
                    idx -= 1
    if type == 2: # up
        for j in range(N):
            que = deque()
            for i in range(N):
                if table[i][j] != 0:
                    que.append(table[i][j])
                table[i][j] = 0
            idx = 0
            while que:
                fo = que.popleft()
                if table[idx][j] == 0:
                    table[idx][j] = fo
                elif table[idx][j] == fo:
                    table[idx][j] = fo*2
                    idx += 1
                else:
                    table[idx+1][j] = fo
                    idx += 1
    if type == 3: # down
        for j in range(N):
            que = deque()
            for i in range(N-1, -1, -1):
                if table[i][j] != 0:
                    que.append(table[i][j])
                table[i][j] = 0
            idx = N-1
            while que:
                fo = que.popleft()
                if table[idx][j] == 0:
                    table[idx][j] = fo
                elif table[idx][j] == fo:
                    table[idx][j] = fo*2
                    idx -= 1
                else:
                    table[idx-1][j] = fo
                    idx -= 1


def rec(table, current):
    if current == 5:
        return table_max(table)
    res = 0
    temp_table=[]
    for i in range(N):
        temp_table.append([])
        for j in range(N):
            temp_table[i].append(table[i][j])

    for type in range(4):
        table_change(table, type)
        res = max(res, rec(table, current+1))
        for i in range(N):
            for j in range(N):
                table[i][j] = temp_table[i][j]
    return res

N = int(input())
table = []
for _ in range(N):
    table.append([])
for i in range(N):
    table[i] = list(map(int, input().split()))

print(rec(table, 0))