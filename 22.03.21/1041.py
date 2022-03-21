# 주사위
# N 크기의 주사위일 경우
# 꼭짓점 : 4
# 모서리 : 4 + (N-2) * 8
# 면 : (N-2)**2 * 5 + (N-2) * 4
# 꼭짓점 : 8개중 최소
# 모서리 : 12개중 최소
# 면 : 6개 중 최소

N = int(input())
planes = list(map(int, input().split()))

lines = [planes[0]+planes[1], planes[0]+planes[2], planes[0]+planes[3], planes[0]+planes[4]
, planes[5]+planes[1], planes[5]+planes[2], planes[5]+planes[3], planes[5]+planes[4]
, planes[1]+planes[2], planes[2]+planes[4], planes[4]+planes[3], planes[3]+planes[1]]

corners = [planes[0]+planes[1]+planes[2], planes[0]+planes[2]+planes[4]
, planes[0]+planes[4]+planes[3], planes[0]+planes[3]+planes[1]
, planes[5]+planes[1]+planes[2], planes[5]+planes[2]+planes[4]
, planes[5]+planes[4]+planes[3], planes[5]+planes[3]+planes[1]]

plane = min(planes) * ((N-2)**2*5 + (N-2)*4)
line = min(lines) * ((N-2)*8 + 4)
corner = min(corners) * 4

if N > 1:
    print(plane+line+corner)
else:
    print(sum(planes) - max(planes))