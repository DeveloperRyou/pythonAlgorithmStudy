# 카드게임
# 카드가 A : 3 2 5 / B : 2 4 1 순서로 있다면 
# A 한장 빼기, A,B 동시에 한장 빼기, B가 작다면 B 빼고 점수 더하기
# 이차원 DP

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
DP = [[0] * 2001 for _ in range(2001)] # 세로 A, 가로 B
# DP[A에서 뺀 카드수][B에서 뺀 카드수] = 그 상태의 최대 점수

for Bcard in range(N-1,-1,-1): # N-1장 뺐을때 부터 안뺐을때
    for Acard in range(N-1,-1,-1): # N-1장 뺐을때 부터 안뺐을때 
        if A[Acard] > B[Bcard]: 
            DP[Acard][Bcard] = max(DP[Acard][Bcard], B[Bcard] + DP[Acard][Bcard+1]) # B 뺀상태의 최대값이랑 더하기
        else:
            DP[Acard][Bcard] = max(DP[Acard][Bcard], DP[Acard+1][Bcard]) # A뺀상태의 최대
            DP[Acard][Bcard] = max(DP[Acard][Bcard], DP[Acard+1][Bcard+1]) # AB뺀상태의 최대
      
print(DP[0][0])