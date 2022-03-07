# 모든 N에 대해 2-친구를 구하기
# 1-친구를 구하는과정 : N
# 2-친구를 구하는과정 : 1-친구의 1-친구 : N^2
# 모든 N에 대해 : N^3

import sys
input = sys.stdin.readline

N = int(input())
mp = []
for _ in range(N):
    mp.append(input())

def friend_1(count_mp, person):
    for friend in range(N):
        if mp[person][friend] == 'Y':
            count_mp[friend] = 1

def friend_2(person):
    count_mp = [0] * N
    for friend in range(N):
        if mp[person][friend] == 'Y':
            count_mp[friend] = 1
            friend_1(count_mp, friend)
    cnt = 0
    for i in range(N):
        if count_mp[i] and i != person:
            cnt += 1
    return cnt

answer = 0
for person in range(N):
    answer = max(answer, friend_2(person))
print(answer)