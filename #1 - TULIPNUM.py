testcase = int(input("Enter a number: "))
print ()

tc = 1

while tc <= testcase:
    n, q = input("").split()
    n = int(n)
    q = int(q)
    array = input("").split()

    for i in range (len(array)):
        array[i] = (int)(array[i])

    output_list = []
    
    print (f"Case {tc}:")
    for a in range (q):
        query1, query2 = input(f"enter q{a+1}: ").split()
        query1 = int(query1)
        query2 = int(query2)

        ans = 0
        for i in range (query1-1, query2):
            if ( i == query1-1):
                ans = 1
            elif ( array[i] != array[i-1]):
                ans += 1
        print (ans)
    tc +=1