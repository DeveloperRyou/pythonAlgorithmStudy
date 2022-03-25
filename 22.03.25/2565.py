# 전봇대
# 전봇대에 줄이 안꼬이게끔 하려면 최소 몇개 전선을 없애야하는가?
# 양 A, B가 오름차순이면 안꼬임
# 오름차순으로 만들 수 있는 가장 긴 리스트를 구하자

from re import X


N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]

line.sort()

# line[?][1]의 최대길이 오름차순 부분수열을 구하자
# 5 4 6 10 8 9 11 5 12 1
# 1 1 2 3  3 4 5  2 6  1

mx_len = [1]*N

for idx in range(1, N):
	for j in range(idx):
		if line[j][1] < line[idx][1]:
			mx_len[idx] = max(mx_len[idx], mx_len[j]+1)

#print(line)
#print(mx_len)
print(N - max(mx_len))
