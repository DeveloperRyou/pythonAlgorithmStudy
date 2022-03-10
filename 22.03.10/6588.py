# 골드바흐의 추측
# 에라토스 체로 소수 잡고
# 계속 검사하기
# 소수이면 멈추기

arr_input = []
while True:
    arr_input.append(int(input()))
    if arr_input[-1] == 0:
        arr_input.pop()
        break

arr = [0]*1000001
for prime in range(2, 1001):
    if arr[prime] == 0:
        idx = 2
        while prime*idx <= 1000000:
            arr[prime*idx] = 1
            idx+=1

def prime(num):
    return not arr[num]

for n in arr_input:
    for gold in range(3, n+1, 2):
        if prime(gold) and prime(n-gold):
            print("{} = {} + {}".format(n, gold, n-gold)) # 왜 그냥 print로 하면 안됨?
            break
