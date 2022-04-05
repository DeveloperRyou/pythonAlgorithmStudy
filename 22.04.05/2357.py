# 최대최소
# 세그먼트 트리
"""
         (1,5)
   (1,4)      (5,5)
(1,2) (3,4) (5,5)  x
1  2  3  4  5  x  x  x
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 높이 설정
n = N
height=1
while n!=1:
	height+=1
	if n%2 != 0:
		n += 1
	n//=2
seg_tree = [[1000000001, 0] for _ in range(2**height)]
for i in range(N):
	temp = int(input())
	seg_tree[2**(height-1)-1 + i] = [temp, temp]

def init(left, right, node):
	if left == right:
		return seg_tree[node]
	mid = (left+right)//2
	min_left, max_left = init(left, mid, node*2+1)
	min_right, max_right = init(mid+1, right, node*2+2)
	mn = min(min_left, min_right)
	mx = max(max_left, max_right)
	seg_tree[node] = [mn, mx]
	return seg_tree[node]
init(0, 2**(height-1)-1,0)
#print(seg_tree)

def query(left, right, node, index_left, index_right):
	if index_right < left or right < index_left:
		return [1000000001, 0]
	if index_left <= left and right <= index_right:
		return seg_tree[node]
	mid = (left+right)//2
	min_left, max_left = query(left, mid, node*2+1, index_left, index_right)
	min_right, max_right = query(mid+1, right, node*2+2, index_left, index_right)
	mn = min(min_left, min_right)
	mx = max(max_left, max_right)
	return [mn, mx]

for _ in range(M):
	a, b = map(int, input().split())
	mn, mx = query(0, 2**(height-1)-1,0,a-1, b-1)
	print(mn, end=' ')
	print(mx)