# nCr 이항계수 구하기
# 파이썬이니 그냥 구해보자
# N, R이 최대 천이니 1000!으로

N, R = map(int, input().split())

def pec(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print((pec(N)//(pec(R)*pec(N-R)))%10007)