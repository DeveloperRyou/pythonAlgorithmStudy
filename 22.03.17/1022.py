# 행렬이 -5000 부터 5000까지 가능
# 길이 10001인 이차원배열로 접근못함 (1억배열 선언 불가)
# 수학적인 접근 필요
# 좌표를 이용하여 값을 그때그때 계산

r1, c1, r2, c2 = map(int, input().split())

def find_num(y, x):
    mx_len = max(abs(y), abs(x))
    mx = (2*mx_len+1)**2
    if y == mx_len:
        return mx - mx_len + x
    if -x == mx_len:
        return mx - 3*mx_len + y
    if -y == mx_len:
        return mx - 5*mx_len - x
    return mx - 7*mx_len - y

mx_num = max(find_num(r1, c1), find_num(r1, c2), find_num(r2, c1), find_num(r2, c2))
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        num = find_num(i, j)
        sep = len(str(mx_num)) - len(str(num))
        for _ in range(sep):
            print(end=' ')
        print(num, end=' ')
    print()