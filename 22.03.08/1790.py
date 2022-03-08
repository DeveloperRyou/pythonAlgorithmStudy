# N = 1억이라서 1부터 N까지 숫자를 반복 (pypy 필요)
# k 값과 비교하면서 변수값 조절, 답 출력

N, k = map(int, input().split())
count_len = 1
flag = 1
for i in range(1, N+1):
    if i >= pow(10, count_len):
        count_len += 1
    if k <= count_len:
        print(i // pow(10, count_len-k) % 10)
        flag = 0
        break
    k -= count_len
if flag:
    print(-1)