#BYTESM2 SPOJ

testcase = int(input())

for tc in range(1, testcase+1):
    row, col = input().split()
    row = int(row)
    col = int(col)

    arr = []
    memo = []
    for x in range(0, row + 1):
        temp = []
        temp2 = []
        for y in range(0, col + 1):
            temp.append(0)
            temp2.append(0)
        arr.append(temp)
        memo.append(temp2)

    for x in range(1, row + 1):
        temp=[]
        temp = input().split()
        for y in range(1, col + 1):
            arr[x][y] = int(temp[y-1])

    for y in range(1, col + 1):
        memo[1][y] = arr[1][y]

    for b in range(1, row):
        for k in range(1, col + 1):
            # bawah
            memo[b + 1][k] = max(memo[b + 1][k], memo[b][k] + arr[b + 1][k])
            # bawah kanan
            if (k < col):
                memo[b + 1][k + 1] = max(memo[b + 1][k + 1], memo[b][k] + arr[b + 1][k + 1])
            # bawah kiri
            if (k > 1):
                memo[b + 1][k - 1] = max(memo[b + 1][k - 1], memo[b][k] + arr[b + 1][k - 1])
    '''
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            print('%d' % arr[i][j], end="")
            if (j < col):
                print(" ", end="")
        print()
    '''
    mini = 0
    for j in range(1,col+1):
        mini = max (mini, memo[row][j])
    print(mini)