# 최소스패닝 트리를 구하고 최대가중치 한개를 삭제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀깊이 1000 제한을 해제해야 함
N, M = map(int, input().split())
# start, end, weight
road = [[0,0,0] for _ in range(M)]
node_parent = [0]*(N+1) # 각노드의 부모노드
# 입력처리
for m in range(M):
    road[m] = list(map(int, input().split()))

# 가중치기준 오름차순 정렬
road.sort(key= lambda x:x[2])

# 최상위 부모노드 찾는 함수
def find(node):
    if node_parent[node] == 0:
        node_parent[node] = node
        return node
    if node_parent[node] == node:
        return node
    # 함수돌릴때 마다 부모노드 최신화 해 탐색횟수를 줄이기 -> 시간초과 방지
    node_parent[node] = find(node_parent[node])
    return node_parent[node]


idx = 0
answer = 0
# 마지막 가중치가 최대 가중치 일 것
last_weight = 0
# 스패닝트리 생성
while idx<M:
    node_parent_start = find(road[idx][0])
    node_parent_end = find(road[idx][1])
    # 사이클
    if node_parent_start == node_parent_end:
        idx = idx+1
        continue
    # 부모노드 최신화
    node_parent[node_parent_end] = node_parent_start
    
    last_weight = road[idx][2]
    answer = answer + last_weight
    idx = idx + 1

print(answer - last_weight)