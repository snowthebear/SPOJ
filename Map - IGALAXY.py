def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


t = int(input())

planet = {} #dictionary

lst = []
for i in range (t):
    planet1, planet2 = input().split()
    
    if planet1 not in lst:
        lst.append(planet1)

        if planet2 not in lst:
            lst.append(planet2)

    elif planet2 not in lst:
            lst.append(planet2)



if is_prime(len(lst) / 2):
    print(lst[len(lst)//2 -1], "-", lst[len(lst)-1])
else:
    print(lst[len(lst)//2 -1], "-", lst[0])

    

    