def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def check_offside(attackers, defenders):
    bubble_sort(attackers)
    bubble_sort(defenders)
    
    second_last_defender = defenders[1]

    return attackers[0] < second_last_defender


def main():
    while True:
        a,d = input().split()   
        a = int(a)
        d = int(d)

        if a == 0 and d == 0:
            break;

        attackers = list(map(int, input().split()))
        defenders = list(map(int, input().split()))

        check = check_offside(attackers, defenders)

        if check == True:
            print('Y') 
        else:
            print('N')

if __name__ == "__main__":
    main()