n = int(input()) #length list
array = (input()).split() # numbers for the array separated by space

if (len(array)) != n:
    array = (input()).split() # numbers for the array separated by space

memo = []

for i in range (len(array)):
    array[i] = int(array[i])
    memo.append(1)

for i in range (1,n):
    for j in range (0,n):
        if array[j] < array[i]:
            memo[i] = max(memo[i], memo[j]+1)


print (memo)
print (max(memo))

    