# 네트워크 연결
# 최소 스패닝 트리

N = int(input())
M = int(input())
# st, ed, weight
arr = [list(map(int, input().split())) for _ in range(M)]
node = []
for i in range(N+1):
	node.append(i)
# 가중치 기준 연결
arr.sort(key=lambda x:x[2])

def parent_node(current_node):
	if node[current_node] == current_node:
		return current_node
	node[current_node] = parent_node(node[current_node])
	return node[current_node]

idx = 0
answer = 0
while idx < M:
	p1 = parent_node(arr[idx][0])
	p2 = parent_node(arr[idx][1])

	if p1 != p2:
		answer += arr[idx][2]
		node[p1] = p2
	idx+=1

print(answer)