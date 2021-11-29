# 최소 스패닝 트리
import sys
input = sys.stdin.readline 
V, E = map(int, input().split())
# start, end, weight
E_arr = [[0,0,0] for _ in range(E)]
for e in range(E):
    E_arr[e] = list(map(int, input().split()))

# 가중치 기준으로 오름차순 정렬 - 낮은 가중치부터 선택하기 위함
E_arr.sort(key= lambda x:x[2])

# 각 노드의 부모 노드
parent_node = [0]*(V+1)
answer = 0
idx = 0

# 최상위 부모노드 찾는 함수
def findPnode(node):
    if parent_node[node] == 0:
        # 초기상태일 경우
        parent_node[node] = node
        return node
    if parent_node[node] == node:
        return node
    parent_node[node] = findPnode(parent_node[node])
    return parent_node[node]
while idx<E:
    p_node_start = findPnode(E_arr[idx][0])
    p_node_end = findPnode(E_arr[idx][1])

    # 사이클
    if p_node_start == p_node_end:
        idx = idx + 1
        continue
    answer = answer + E_arr[idx][2]
    # end의 부모노드 갱신
    parent_node[p_node_end] = p_node_start

    idx = idx + 1

print(answer)
