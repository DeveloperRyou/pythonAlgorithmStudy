# 피보나치 3
# N이 엄청 클때?
# logN 방법이 필요함

# N 짝수일때
# F(N) = F(N/2 + 1)**2 + F(N/2)**2

N = int(input())
FIBO = {0:0, 1:1, 2:1, 3:2, 4:3, 5:5}

def fibo(n):
	if n in FIBO:
		return FIBO[n]
	if n%2 == 1:
		FIBO[n] = (fibo(n//2)**2 + fibo(n//2 + 1)**2)%1000000
		return FIBO[n]
	else:
		FIBO[n] = (fibo(n+1) - fibo(n-1))%1000000
		return FIBO[n]
print(fibo(N))