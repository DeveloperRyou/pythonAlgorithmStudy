# 집합의 표현
# union find
# union, find 메소드를 구현해 트리로 접근

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
tree = []
for i in range(N+1):
	tree.append(i)

def findHead(node):
	if node == tree[node]:
		return node
	head = findHead(tree[node])
	tree[node] = head
	return head

def union(node1, node2):
	head_node1 = findHead(node1)
	head_node2 = findHead(node2)
	tree[head_node1] = head_node2

def find(node1, node2):
	head_node1 = findHead(node1)
	head_node2 = findHead(node2)
	if head_node1 == head_node2:
		return True
	return False


for m in range(M):
	a, b, c = map(int, input().split())
	if a == 0:
		union(b, c)
	else:
		if find(b, c) == True:
			print("YES")
		else:
			print("NO")