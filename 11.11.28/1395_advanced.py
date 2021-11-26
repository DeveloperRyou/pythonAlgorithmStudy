import math
import sys
input = sys.stdin.readline # 10만개 이상 인풋 받을 때 안하니 시간초과
# python 통과
# 딕셔너리 대신 2개 리스트 이용

N, M = map(int, input().split())
# 트리 깊이
depth = math.ceil(math.log2(N))
# 구간합 트리 ** 리스트 2개 이용 **
tree_value = [0 for _ in range(400000)]
tree_shouldUpdate = [False for _ in range(400000)]

# 일반 트리갱신은 log N, 전체값 갱신시 M * NlogN 이라서 해결 불가능
# 정보저장 후 필요할 때만 갱신 -> M * logN 
def updateTree(update_start, update_end, start = 1, end = 2 ** depth, node = 1):
    # 정보갱신이 필요할 때
    if tree_shouldUpdate[node]:
        updateNode(node, start, end)

    # 모든 자손 노드가 업데이트 구간에 포함되었을 때
    if update_start<=start and end<=update_end:
        # 반전
        tree_value[node] = (end - start + 1) - tree_value[node]

        # leaf가 아닐 경우 자손 노드 업데이트 반전
        if start<end:
            tree_shouldUpdate[node*2] = not tree_shouldUpdate[node*2]
            tree_shouldUpdate[node*2+1] = not tree_shouldUpdate[node*2+1]
        return
    # 업데이트 구간에 포함되지 않은 경우
    if end<update_start or start>update_end:
        return

    # 겹치는 경우
    mid = (start+end)//2
    updateTree(update_start, update_end, start, mid, node*2)
    updateTree(update_start, update_end, mid+1, end, node*2+1)
    tree_value[node] = tree_value[node*2] + tree_value[node*2+1]

# 정보갱신
def updateNode(node, start, end):
    #반전
    tree_value[node] = (end - start + 1) - tree_value[node]
    tree_shouldUpdate[node] = False
    # leaf가 아닐 경우 자손 노드 업데이트 반전
    if start<end:
        tree_shouldUpdate[node*2] = not tree_shouldUpdate[node*2]
        tree_shouldUpdate[node*2+1] = not tree_shouldUpdate[node*2+1]

# 구간합
def prefixSum(sum_start, sum_end, start = 1, end = 2 ** depth, node = 1):
    # 정보갱신이 필요할 때
    if tree_shouldUpdate[node]:
        updateNode(node, start, end)
    
    # 모든 자손 노드가 구간합 구간에 포함되었을 때
    if sum_start<=start and end<=sum_end:
        return tree_value[node]
        
    # 업데이트 구간에 포함되지 않은 경우
    if end<sum_start or start>sum_end:
        return 0
    
    # 겹쳤을 때 
    mid = (start+end)//2
    return prefixSum(sum_start, sum_end, start, mid, node*2) + \
        prefixSum(sum_start, sum_end, mid+1, end, node*2+1)

for work in range(M):   
    # 각 줄 입력
    isCount, S, T = map(int, input().split())
    
    if isCount:
        print(prefixSum(S,T))
    else:
        updateTree(S,T)