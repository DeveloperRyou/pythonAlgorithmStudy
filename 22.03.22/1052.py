# 물병
# 2개 -> 1개, 3개 -> 1 + 1개, 4개 -> 2개 -> 1개, 5개-> 1 + 2개 -> 1 + 1개
# logn으로 절반으로 쪼개면서 구현
# 통안에 들어올 때 까지 새 물병 구입 

# 으로 시도했지만 시간초과 
# (1000000, 1) 일때 문제

# 2 = 10, 3 = 11, 4 = 100, 5 = 101-> 10-> 1
# 2진수로 표현하고 1의 갯수가 필요한 물병의 갯수
# 필요 물통이 2개라면 현재 물통 파악 이후 (예 : 1100011101, 6개)
# 오른쪽부터 물통 5개 지우기 -> 지운만큼 왼쪽으로 시프트
# 1 -> 10 -> 10000000000

N, K = map(int, input().split())

def length(n):
    res = 1
    while n!=1:
        if n%2 == 1:
            res += 1
        n = n>>1
    return res

def answer(n, len):
    k = 0
    shift = 0
    while k < len-K+1:
        if n%2 == 1:
            k+=1
        n = n>>1
        shift += 1
    return (n+1)<<shift

len = length(N)
if len <= K:
    print(0)
else:
    print(answer(N, len)-N)