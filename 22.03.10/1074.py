# Z로 탐색하는데 몇번째로 탐색하는지?
# 4분탐색같은 느낌

N, r, c = map(int, input().split())

answer = 0

def rec(N, r, c):
    global answer
    if N == 1:
        answer += 2*r+c
    else:
        if r < 2**(N-1):
            if c < 2**(N-1):
                rec(N-1, r, c)
            else:
                answer += (2**(N-1))**2
                rec(N-1, r, c - 2**(N-1))
        else:
            if c < 2**(N-1):
                answer += ((2**(N-1))**2)*2
                rec(N-1, r - 2**(N-1), c)
            else:
                answer += ((2**(N-1))**2)*3
                rec(N-1, r - 2**(N-1), c - 2**(N-1))

rec(N, r, c)
print(answer)
