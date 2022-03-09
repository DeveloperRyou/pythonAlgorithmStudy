# 1부터 N까지 자연수의 약수의 합을 더해서 출력
# N이 백만이므로 약수의 합을 구하는게 빨라야함
# 단순히 약수를 다 구하면 안될듯 (100만의 제곱근인 1000까지 돌아야 하는데 이걸 100만번 하면 10억)
# 소인수분해로 접근 (2^2 * 3^1 -> (1+2+4)*(1+3)이 약수의 합)...을 하려 했으나 시간초과
# 한번에 합을 구하는 방법이 있다는 말인거 같음
# 2의 배수가 3개 있다면 2가 약수인 수가 3개라는 말이니 배수를 세리는 방향으로 선회

N = int(input())
"""
def sum_divisor(n):
    if n == 1:
        return 1
    primes = [] # 소인수 저장되는 리스트
    idx = 2
    while n != 1:
        if n % idx == 0:
            n /= idx
            primes.append(idx)
            idx = 2
        else:
            idx += 1
    # 소인수로 소수의 합 계산
    before_prime = 1
    res = 1
    temp = 1
    idx = 1
    for prime in primes:
        if before_prime != prime:
            before_prime = prime
            res *= temp # (1+2+4) 같은걸 곱해준다
            temp = 1
            idx = 1
        temp += pow(prime, idx) 
        idx += 1
    res *= temp
    return res

answer = 0
for i in range(1, N+1):
    answer += sum_divisor(i)
print(answer)
"""
answer = 0
for i in range(1,N+1):
    answer += i * (N//i)
print(answer)