# 재귀로 완전탐색, 알파벳 최대 갯수 26 -> 2~3^26 = 1억 내외
# pypy로 해결
import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = []
for r in range(R):
    arr.append(input())
# 네 방향을 담는 벡터
vector = [(-1,0),(1,0),(0,1),(0,-1)]
def cordAcceptable(cordY, cordX):
    return cordX>=0 and cordX<C and cordY>=0 and cordY<R
check = [0]*26
check[ord(arr[0][0])-ord('A')]=1
def findPath(cordY = 0, cordX = 0, length = 1):
    current_length = length
    for i in range(4):
        next_cordY = cordY+vector[i][0]
        next_cordX = cordX+vector[i][1]
        if cordAcceptable(next_cordY,next_cordX):
            alphabet = arr[next_cordY][next_cordX]
            if check[ord(alphabet)-ord('A')] == 0:
                check[ord(alphabet)-ord('A')] = 1
                length = max(length, findPath(next_cordY, next_cordX, current_length+1))
                check[ord(alphabet)-ord('A')] = 0
    return length

print(findPath())