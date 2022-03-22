# 리조트
# 리조트 가는날 = min(
# 하루이용권 + 하루전, 3일이용권 + 3일전, 5일이용권 + 5일전) or 쿠폰3장 사용 + 전날
# 쿠폰을 쓸지 안쓸지도 따로 저장

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
if M != 0:
    arr = list(map(int, input().split()))
DP = [[99999999]*101 for _ in range(44)] #세로는 쿠폰, 가로는 날짜

DP[0][0] = 0 # init
idx = 0
for date in range(1, 101):
    if M==0 or arr[idx] != date:
        for coupon in range(41):
            DP[coupon][date] = min(DP[coupon][date], DP[coupon][date-1] + 10000, DP[coupon+3][date-1]) # 하루전 가격 + 이용권 / 쿠폰
            DP[coupon+1][date] = min(DP[coupon+1][date], DP[coupon][date-3 if date-3>=0 else 0] + 25000) # 3일전 가격 + 3일권
            DP[coupon+2][date] = min(DP[coupon+2][date], DP[coupon][date-5 if date-5>=0 else 0] + 37000) # 5일전 가격 + 5일권
    else:
        for coupon in range(44):
            DP[coupon][date] = DP[coupon][date - 1]
        idx += 1
        if idx == M:
            idx = 0
answer = 99999999
for coupon in range(44):
    answer = min(answer, DP[coupon][N])
print(answer)
