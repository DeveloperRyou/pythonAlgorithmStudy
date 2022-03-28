# 트리
# 클래스로 구현

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

N = int(input())
dic = {}
for _ in range(N):
	node, left, right = input().split()
	dic[node] = (left, right)

Tree = Node('A')

def fill_tree(tree):
	data = tree.data
	left, right = dic[data]
	if left != '.':
		tree.left = Node(left)
		fill_tree(tree.left)
	if right != '.':
		tree.right = Node(right)
		fill_tree(tree.right)
fill_tree(Tree)

def order(tree, type):
	if type == "pre":
		print(tree.data,end='')
	if tree.left is not None:
		order(tree.left, type)
	if type == "in":
		print(tree.data,end='')
	if tree.right is not None:
		order(tree.right, type)
	if type == "post":
		print(tree.data,end='')
		
order(Tree, "pre")
print()
order(Tree, "in")
print()
order(Tree, "post")