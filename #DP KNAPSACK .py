cash, item = input("enter: ").split()
cash = int(cash)
item = int(item)

price = []
fun = []
memo = []

for i in range (item+1):
    temp = []
    price.append(0)
    fun.append(0)
    for j in range (cash+1):
        temp.append(0)

    memo.append(temp)

# for elem in memo:
#     print (elem)

for i in range (1, item+1):
    money, value = input(f"Item {i+1} = ").split()
    money = int(money)
    value = int(value)

    price[i] = money
    fun[i] = value


for i in range (1, item+1): # i / item = baris
    for j in range (cash+1): # j / uang = kolom
        if j < price[i]: # g pny uang
            memo[i][j] = memo[i-1][j]
        else:
            skip = memo[i-1][j]
            sisa = j - price[i]
            buy = fun[i] + memo[i-1][sisa]

            memo[i][j] = max(skip, buy)

print (memo[item][cash])


 


