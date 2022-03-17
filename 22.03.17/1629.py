# A을 B번 곱한뒤 C로 나눈 나머지
# 최대 2억번 곱할 수 있으니 그냥 곱할 수 없음
# 분할정복
# 인데 2개로 쪼개지면 시간초과라서 짝수 홀수로 구분

A, B, C = map(int, input().split())

def rec(N):
    if N == 1:
        return A % C
    if N % 2 == 0:
        return (rec(N//2)**2)%C
    return (rec(N//2)**2 * A)%C

print(rec(B))