# 색종이 자르기
# 분할정복
# N * log(N)의 복잡도
# 색종이를 쪼개면서 계속 확인하자

N = int(input())
mp = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def rec(y, x, n):
    global white
    global blue
    paper = mp[y][x]
    for i in range(n):
        for j in range(n):
            if mp[y+i][x+j] != paper:
                n = n // 2
                rec(y, x, n)
                rec(y+n, x, n)
                rec(y, x+n, n)
                rec(y+n, x+n, n)
                return
    if paper:
        blue += 1
    else:
        white += 1

rec(0,0,N)
print(white)
print(blue)