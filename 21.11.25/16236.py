import copy
import queue
from queue import Queue
from types import CodeType
N = int(input())

MAX = 99999
map = [[0]*20 for row in range(20)]
distance_map = [[MAX]*20 for row in range(20)]

# 입력처리
for i in range(N):
    row = input().split()
    for j in range(N):
        map[i][j] = int(row[j])

size_shark = 2
eat_shark = 0
cord_shark = (0,0)
for i in range(N):
    for j in range(N):
        if map[i][j] == 9:
            cord_shark = (i,j)
            map[i][j] = -1

# distance_map으로 최단거리 먹이 찾기, 먹이를 바로 안찾으면 시간초과
def distance(): #BFS
    distance_map = [[MAX]*20 for row in range(20)]
    distance_map[cord_shark[0]][cord_shark[1]] = 0
    que = Queue()
    que.put(cord_shark)

    feed = []
    distance_break = MAX
    vector = [[0,-1],[0,1],[1,0],[-1,0]] # 상하좌우 벡터
    while not que.empty():
        cord_bfs = que.get()
        distance_bfs = distance_map[cord_bfs[0]][cord_bfs[1]] + 1
        if distance_bfs>distance_break:
            break
        for v in vector:
            cord_next = (cord_bfs[0]+v[0],cord_bfs[1]+v[1])
            # 적합한 좌표인지, 방문하지 않은 곳인지, 지나갈 수 있는 곳인지
            if suitableCord(cord_next) and distance_map[cord_next[0]][cord_next[1]] == MAX and map[cord_next[0]][cord_next[1]]<=size_shark:
                if map[cord_next[0]][cord_next[1]]>0 and map[cord_next[0]][cord_next[1]]<size_shark:
                    feed.append([cord_next,distance_bfs])
                    distance_break = distance_bfs
                else:
                    distance_map[cord_next[0]][cord_next[1]] = distance_bfs
                    que.put(cord_next)
    return feed

def suitableCord(cord):
    y=cord[0]
    x=cord[1]
    if y<0 or y>=N or x<0 or x>=N:
        return False
    return True

eatable_fish_list = distance()
time = 0
while len(eatable_fish_list) != 0:
    fish_to_eat = -1
    distance_to_eat = MAX

    for i in range(len(eatable_fish_list)):
        cord_fish = eatable_fish_list[i][0]
        d = eatable_fish_list[i][1]
        # 거리가 작을 때
        if d<distance_to_eat:
            fish_to_eat = i
            distance_to_eat = d
        # 거리가 같을 때 
        elif d == distance_to_eat:
            cord_fish_to_eat = eatable_fish_list[fish_to_eat][0]
            if cord_fish[0]<cord_fish_to_eat[0]:
                fish_to_eat = i
                distance_to_eat = d
            elif cord_fish[0] == cord_fish_to_eat[0]:
                if cord_fish[1]<cord_fish_to_eat[1]:
                    fish_to_eat = i
                    distance_to_eat = d
                
    if fish_to_eat == -1:
        break
    time = time + distance_to_eat
    map[cord_shark[0]][cord_shark[1]] = 0
    cord_fish_to_eat = eatable_fish_list[fish_to_eat][0]
    map[cord_fish_to_eat[0]][cord_fish_to_eat[1]] = -1
    cord_shark = cord_fish_to_eat
    eat_shark = eat_shark + 1
    if eat_shark == size_shark:
        size_shark = size_shark + 1
        eat_shark = 0
    

    eatable_fish_list = distance()

print(time)