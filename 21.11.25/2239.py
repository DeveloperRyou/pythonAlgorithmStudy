# pypy로 통과

arr = [ [0]*9 for row in range(9) ]
for i in range(9):
    row = list(input())
    for j in range(9):
        arr[i][j] = int(row[j])

cord_space = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            cord_space.append((i,j))

idx_check = 0
def suitable(cord, num):
    for x in range(9):
        if arr[cord[0]][x] == num:
            return False
    for y in range(9):
        if arr[y][cord[1]] == num:
            return False
    
    for x in range(3):
        for y in range(3):
            if arr[(cord[0]//3)*3+y][(cord[1]//3)*3+x] == num:
                return False
    return True
while idx_check < len(cord_space):
    cord_current = cord_space[idx_check]
    num = arr[cord_current[0]][cord_current[1]]

    hasNextNum = False
    for nextNum in range(num+1,10):
        if suitable(cord_current,nextNum):
            arr[cord_current[0]][cord_current[1]] = nextNum
            hasNextNum = True
            break
    
    if hasNextNum:
        idx_check = idx_check + 1
    else:
        arr[cord_current[0]][cord_current[1]] = 0
        idx_check = idx_check - 1


for i in range(9):
    for j in range(9):
        print(arr[i][j],end='')
    print()