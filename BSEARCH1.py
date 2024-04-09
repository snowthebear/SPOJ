def binary_search(low, high, arr, num):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == num:
            if arr[mid-1] == num:
                return binary_search(low, mid-1, arr, num)
            else:
                return mid
            
        elif arr[mid] < num:
            return binary_search(mid + 1, high, arr, num)
        
        elif arr[mid] >= num:
            return binary_search(low, mid - 1, arr, num)
        
    return -1


def main():
    n, q = input().split()
    n , q = int(n), int(q)
    
    arr = list(map(int, input().split()))

    for i in range (q):
        num = int(input())
        result = binary_search(0, len(arr)-1, arr, num)
        print(result)

if __name__ == "__main__":
    main()