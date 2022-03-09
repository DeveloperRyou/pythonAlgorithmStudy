# 오름차순, 내림차순 수열중 가장 긴 길이 찾기
# N 이 10만이니 한번 긁는 알고리즘으로 해결 O(N)
# 오름, 내림 변수에 각각 저장

N = int(input())
arr = list(map(int, input().split()))

max_ascend = 1
max_decend = 1
temp_ascend = 1
temp_decend = 1
for idx in range(1, len(arr)):
    if arr[idx - 1] <= arr[idx]: # 오름차순 확인
        temp_ascend += 1
    else: # 오름차순이 아니라면 max값 갱신
        max_ascend = max(max_ascend, temp_ascend)
        temp_ascend = 1
    if arr[idx - 1] >= arr[idx]: # 내림차순 확인
        temp_decend += 1
    else: # 내름차순이 아니라면 max값 갱신
        max_decend = max(max_decend, temp_decend)
        temp_decend = 1

# 마지막 갱신
max_ascend = max(max_ascend, temp_ascend)
max_decend = max(max_decend, temp_decend)

print(max(max_ascend, max_decend))