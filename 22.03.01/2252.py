# 학생들의 키 순서가 주어질 때, 가능한 순서 출력
# 위상정렬 문제, 큐로 구현
# 정점+간선 만큼 연산 (N+M)

from collections import deque

N, M = map(int, input().split())
line_num = [0] * (N+1)
line_vertex = []
for _ in range(N+1):
    line_vertex.append([])

for _ in range(M):
    fr, to = map(int, input().split())
    line_vertex[fr].append(to)
    line_num[to] += 1

queue = deque()
for i in range(1, N+1):
    if line_num[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    for vertex in line_vertex[now]:
        line_num[vertex] -= 1
        if line_num[vertex] == 0:
            queue.append(vertex)
    print(now, end = ' ')