# 토너먼트 몇라운드에 대결하는지?
# 이진트리로 찾기 (2개씩 묶는 바텀업과정)

N, a, b = map(int, input().split())
if a>b:
    (a, b) = (b, a)
round = 1

while True:
    flag = 0
    for i in range(1, N+1, 2):
        if i == a and i + 1 == b:
            flag = 1
    if flag:
        break
    a = (a+1)//2
    b = (b+1)//2
    N = (N+1)//2
    round += 1
print(round)