# 선분이 만나는지 판별하는 함수를 만들고 N^2으로 해결
# 파이썬 시간초과

import sys
input = sys.stdin.readline

N = int(input())
lines = []
for n in range(N):
    lines.append(list(map(int, input().split())))


def isClockWise(cord1, cord2, cord3):
    # 좌표 1, 2, 3이 시계방향이면 1, 반시계면 -1, 직선이면 0 리턴
    '''vector1 = (cord2[0]-cord1[0], cord2[1]-cord1[1])
    vector2 = (cord3[0]-cord2[0], cord3[1]-cord2[1])

    # 외적
    externalP = vector1[0]*vector2[1]-vector1[1]*vector2[0]'''
    externalP = (cord1[0]*cord2[1]+cord2[0]*cord3[1]+cord3[0]*cord1[1])\
        - (cord1[0]*cord3[1]+cord2[0]*cord1[1]+cord3[0]*cord2[1])
    if externalP>0:
        # 반시계
        return -1
    elif externalP<0:
        # 시계
        return 1
    else:
        return 0

def isCross(line1, line2):
    # 점 3개가 시계방향으로 이루어져 있는지 검사하는 CCW알고리즘 이용
    A = (line1[0],line1[1])
    B = (line1[2],line1[3])
    C = (line2[0],line2[1])
    D = (line2[2],line2[3])
    ccw1 = isClockWise(A,B,C)*isClockWise(A,B,D)
    ccw2 = isClockWise(C,D,A)*isClockWise(C,D,B)
    # 두 직선이 일직선일 때
    if ccw1 == 0 and ccw2 == 0:
        if A>B:
            A, B = B, A
        if C>D:
            C, D = D, C
        if B<C or D<A:
            return False
        else:
            return True
    if ccw1<=0 and ccw2<=0:
        return True
    else:
        return False

check = []
for i in range(N):
    check.append(i)

def find(node):
    # 유니온파인드
    if check[node] == node:
        return node
    # 시간초과의 원인?
    check[node] = find(check[node])
    return check[node]

for i in range(N):
    for j in range(i+1,N):
        if isCross(lines[i],lines[j]):
            group1 = find(check[i])
            group2 = find(check[j])
            group = min(group1, group2)
            
            # 중요! 부모노드를 최신화
            check[group1] = group
            check[group2] = group

answer = 0
number = [0]*N
numberMax = 0
for i in range(N):
    if check[i]==i:
        answer = answer+1
    parentNode = find(i)
    number[parentNode] = number[parentNode] + 1
    numberMax = max(numberMax,number[parentNode])
print(answer)
print(numberMax)
    