# 친구비
# 마찬가지로 union find
# union 메소드를 구현해 트리로 접근
# 트리에서 최소 친구비에 관한 내용도 가지고 가기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, K = map(int, input().split())
cost = list(map(int, input().split()))

tree = []
tree.append(0)
for i in range(1, N+1):
	tree.append([i, cost[i-1]])

def findHead(node):
	if node == tree[node][0]:
		return node
	head = findHead(tree[node][0])
	tree[node][0] = head
	return head

def union(node1, node2):
	head_node1 = findHead(node1)
	head_node2 = findHead(node2)
	tree[head_node1][0] = head_node2
	tree[head_node2][1] = min(tree[head_node1][1], tree[head_node2][1])

for m in range(M):
	a, b = map(int, input().split())
	union(a, b)

minimum_cost = 0
for i in range(1, N+1):
	if tree[i][0] == i:
		minimum_cost+=tree[i][1]
if minimum_cost<=K:
	print(minimum_cost)
else:
	print("Oh no")