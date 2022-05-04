# System Engineer
# 이분매칭
# 호프크로프트 카프 알고리즘
# 왜 O(E루트V)인지는 아직 잘 모르겠다..

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)

T = None
graph = None
match_job = None
match_server = None

"""
def dfs(job, visit):
	visit[job] = True
	for server in graph[job]:
		# 매칭 안 되어있을 경우 or
		# 매칭 되어있지만 바꿀 수 있는 경우
		if match_server[server] == -1 or \
			(visit[match_server[server]] == False and dfs(match_server[server], visit)): 

			match_server[server] = job
			match_job[job] = server
			return True
	return False
"""
def dfs_hop(job):
	# 증가경로 있다면 true
	for server in graph[job]:
		# 매칭 안 되어있을 경우 or
		# 매칭 되어있지만 다음 노드가 증가경로 일때 계속 탐색 & 바꿀 수 있는 경우
		if match_server[server] == -1 or \
			(level_job[job] + 1 == level_server[server] and level_server[server] + 1 == level_job[match_server[server]] \
				and dfs_hop(match_server[server])):

			match_server[server] = job
			match_job[job] = server
			return True
	return False

def bfs_level(level_job, level_server):
	que = deque()
	for t in range(T):
		if match_job[t] == -1:
			que.append((t, 0)) # 매칭 안된 job 노드 넣기
	while len(que)>0:
		job, level = que.popleft() 
		level_job[job] = level # 레벨링
		for server in graph[job]:
			if level_server[server] == -1: # server 노드 레벨링 안 되어 있을 때 
				level_server[server] = level + 1
				if match_server[server] != -1: # server 노드가 job 노드랑 매칭 되어있다면
					que.append((match_server[server], level+2)) # job 노드 넣기

while True:
	try:
		T = int(input())
		graph = []
		for _ in range(T):
			graph.append([])
		match_job = [-1] * T
		match_server = [-1] * T
		
		for _ in range(T):
			line = input().split()
			job = int(line[0][0:-1])
			servers = int(line[1][1:-1])
			for server in line[2:2+servers]:
				graph[job].append(int(server)-T)
		
		# 일단 dfs 이분매칭으로 풀어보자
		# 정점마다 dfs : O(V(V+E))
		"""
		테스트케이스 극한상황에서 E : 30000, V : 10000 확인
		E만큼 dfs재귀를 탐색하니 재귀오류발생 & 시간초과
		answer = 0
		for i in range(T):
			visit = [False] * T
			if match_job[i] == -1 and dfs(i, visit):
				answer += 1
		print(answer)
		"""

		# 호프 어쩌고 카프 알고리즘
		# 매칭 안되어있는 노드 level 0, bfs로 레벨 초기화 O(V+E)
		answer = 0
		while True:
			level_job = [-1] * T
			level_server = [-1] * T
			bfs_level(level_job, level_server)
			

			# dfs로 증가 경로 찾고 있다면 경로 1 증가
			# 증가경로 찾을거니까 visit 필요없음 
			# dfs 탐색의 깊이 제한하는 효과 (가지치기 같은 느낌?) -> 시간복잡도 개선
			flow = 0
			for i in range(T):
				if match_job[i] == -1 and dfs_hop(i):
					flow += 1
			# 증가 경로 없으면 종료
			if flow == 0:
				break
			answer += flow
		print(answer)
	except:
		break