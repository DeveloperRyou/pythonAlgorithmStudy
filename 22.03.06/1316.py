# 단순구현 문제
# 알파벳 배열 만들어서 카운트, 2이상인데 연결되어있지 않으면 False

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
for _ in range(N):
    string = input()
    dic = {}
    for idx in range(len(string)):
        if string[idx] in dic:
            if string[idx - 1] != string[idx]:
                cnt -= 1
                break
        else:
            dic[string[idx]] = 1
    cnt += 1
print(cnt)