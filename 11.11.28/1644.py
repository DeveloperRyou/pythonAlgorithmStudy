# 입력
N = int(input())

# 소수 - 체를 이용해 확인
MAXNUM = 4000001
check_primenum = [True for _ in range(MAXNUM)]
check_primenum[0] = False
check_primenum[1] = False
for i in range(2, 2001): # 중요
    if check_primenum[i] == True:
        for j in range(i*i, MAXNUM, i):
            check_primenum[j] = False
# 소수를 담을 리스트
primenum = []
for i in range(2, MAXNUM):
    if check_primenum[i]:
        primenum.append(i)

# 인덱스 2개
idx_start = 0
idx_end = 0
sum_primenum = primenum[0]
answer = 0
# 끝 인덱스가 범위 초과시, 처음 인덱스가 끝 인덱스를 오버하면 종료
while idx_start < len(primenum) and idx_end < len(primenum) and idx_start<=idx_end:
    # 작거나 같으면 끝 인덱스를 증가, 소수를 더함
    if sum_primenum<=N:
        if sum_primenum == N:
            answer = answer + 1
        idx_end = idx_end + 1
        # 중요 : 증가시켰을 때 범위 넘어가는거 고려
        if idx_end < len(primenum):
            sum_primenum = sum_primenum + primenum[idx_end]
    # 크면 처음 인덱스를 증가, 소수를 뺌
    else:
        sum_primenum = sum_primenum - primenum[idx_start]
        idx_start = idx_start + 1
print(answer)