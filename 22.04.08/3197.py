# 백조문제
# 치즈랑 비슷한듯?
# 모든 맵을 노드라고 가정
# 2250000개 노드를 bfs적으로 연결
# 연결 끝나고 백조끼리 연결 되었는지 확인
# 연결 과정은 union. 확인은 find로
# pypy로 통과

from collections import deque

R, C = map(int, input().split())
mp = [list(input()) for _ in range(R)]
tree = []
for i in range(R*C):
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

swans = []
que = deque()
vec = [[1,0],[-1,0],[0,1],[0,-1]]
for i in range(R):
	for j in range(C):
		newQue = True
		if mp[i][j] == '.' or mp[i][j] == 'L':
			if mp[i][j] == 'L':
				swans.append(i*C+j)
			for vy, vx in vec:
				if 0<=i+vy<R and 0<=j+vx<C:
					if mp[i+vy][j+vx] == 'X' and newQue:
						que.append((i, j, 0))
						newQue = False
					if mp[i+vy][j+vx] == '.' or mp[i+vy][j+vx] == 'L':
						union(i*C+j, (i+vy)*C+(j+vx))

date = -1
while len(que)>0:
	y, x, date_before = que.popleft()
	if date<date_before:
		date = date_before
		connect = True 
		for idx in range(len(swans)-1):
			if find(swans[idx], swans[idx+1]) == False:
				connect = False
				break
		if connect:
			break
	for vy, vx in vec:
		if 0<=y+vy<R and 0<=x+vx<C:
			if mp[y+vy][x+vx] == 'X':
				que.append((y+vy, x+vx, date_before+1))
				mp[y+vy][x+vx] = '.'
				for uy, ux in vec:
					if 0<=y+vy+uy<R and 0<=x+vx+ux<C:
						if mp[y+vy+uy][x+vx+ux] !='X':
							union((y+vy)*C+(x+vx), (y+vy+uy)*C+(x+vx+ux))
if date == -1:
	date = 0
print(date)