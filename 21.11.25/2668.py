# 방향그래프에서 사이클 찾기
# N=100, 2중포문으로 O(n^2) 

N = int(input())

arr = [[0]*100 for row in range(100)]
check = [0]*100
cycle = [0]*100

for i in range(N):
    point = int(input())-1
    arr[i] = point

for i in range(N):
    # 전처리 (사아클이 만들어지는 노드)
    if cycle[i] == 1:
        pass
    # 전처리 (사이클이 바로 만들어질 때)
    point = arr[i]
    if point == i:
        cycle[i] = 1
    
    # 사이클 찾기
    isCycle = True
    check[i] = 1
    while point != i:
        check[point] = 1
        point = arr[point]
        # 사이클 못찾고 탐색한 노드에 방문했을 때
        if check[point] == 1 and point != i:
            isCycle = False
            break
    
    # 사이클 저장
    if isCycle:
        for i in range(N):
            if check[i] == 1:
                cycle[i] = 1
    check = [0]*100

num_node = 0
for i in range(N):
    num_node = num_node + cycle[i]
print(num_node)
for i in range(N):
    if cycle[i] == 1:
        print(i+1)