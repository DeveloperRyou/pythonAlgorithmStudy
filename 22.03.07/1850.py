# 최대공약수 구해서 그만큼 1 출력

from math import gcd
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = gcd(N, M)
for _ in range(res):
    print(1, end='')