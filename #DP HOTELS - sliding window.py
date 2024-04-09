# n: total hotel
# budget

n, budget = input("Enter number : ").split(" ")
array = input("Enter numbers ").split()

n = int(n)
budget = int(budget)

for i in range (len(array)):
    array[i] = (int)(array[i])

total = 0
answer = 0
c = 0

for i in range (len(array)):
    total += array[i]

    while (total > budget):
        total -= array[c]
        c += 1

    answer = max(total,answer)

# print (total)
print (answer)