
n = int(input("Enter a number: "))

array = []

for i in range (n):
    q = input().split()
    array.append(q)
    
for i in range (len(array)):
    for j in range (len(array[i])):
        array[i][j] = (int)(array[i][j])

for a in array:
    print (a)

query = int(input("query: "))

for i in range (query):
    q = input().split()
    # print (q)

    for a in range (len(q)):
        q[a] = (int)(q[a])

    black = 0
    white = 0
    for x in range (q[0]-1, q[2]): #baris
       
        for y in range (q[1]-1, q[3]): #kolom
            if y == x or (x % 2 == 0 and y % 2 == 0):
                white += array[x][y]
            else:
                black += array[x][y]

    # print (max(black,white) - min(black,white))
    print (abs(black-white))
    
            
