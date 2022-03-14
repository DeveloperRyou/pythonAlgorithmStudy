# N이 20 이하니까 무지성 구현 가능
# 뺄때 N만큼 탐색후에 제거할 요소 선택
# 1000번 반복하면 최대 20000 연산
# 딕셔너리로 구현

N = int(input())
T = int(input())
arr = list(map(int, input().split()))
dic = {}

def delete():
    mn = 10000
    idx = 0
    for i in dic:
        if mn > dic[i]:
            mn = dic[i]
            idx = i
    del(dic[idx])

for t in range(T):
    if len(dic) < N:
        try:
            dic[arr[t]] += 1
        except:
            dic[arr[t]] = 0
    else:
        try:
            dic[arr[t]] += 1
        except:
            delete()
            dic[arr[t]] = 0

L = sorted(dic)
for item in L:
    print(item, end=' ')
