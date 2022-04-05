# 구간합 구하기
# 세그먼트 트리
"""
      15
   10      5
 3   7   5   x
1 2 3 4 5 x x x
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
# 높이 설정
n = N
height=1
while n!=1:
	height+=1
	if n%2 != 0:
		n += 1
	n//=2
seg_tree = [0]*(2**height)
for i in range(N):
	seg_tree[2**(height-1)-1 + i] = int(input())
def init(left, right, node):
	if left == right:
		return seg_tree[node]
	mid = (left+right)//2
	seg_tree[node] = init(left, mid, node*2+1) + init(mid+1, right, node*2+2)
	return seg_tree[node]
init(0, 2**(height-1)-1,0)
#print(seg_tree)

def update(left, right, node, index, value):
	if left == right and left == index:
		seg_tree[node] = value
		return value
	mid = (left+right)//2
	if left<=index<=mid:
		seg_tree[node] = update(left, mid, node*2+1, index, value) + seg_tree[node*2+2]
	else:
		seg_tree[node] = seg_tree[node*2+1] + update(mid+1, right, node*2+2, index, value)
	return seg_tree[node]

def sum(left, right, node, index_left, index_right):
	if index_right < left or right < index_left:
		return 0
	if index_left <= left and right <= index_right:
		return seg_tree[node]
	mid = (left+right)//2
	return sum(left, mid, node*2+1, index_left, index_right) \
		+ sum(mid+1, right, node*2+2, index_left, index_right)
	
for _ in range(M+K):
	a, b, c = map(int, input().split())
	if a == 1:
		update(0, 2**(height-1)-1, 0, b-1, c)
	else:
		print(sum(0, 2**(height-1)-1, 0, b-1, c-1))