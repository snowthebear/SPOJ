def total_trees(mid, arr):
    total = 0
    for tree in arr:
        if tree > mid:
            total += tree - mid

    return total


def binary_search(low, high, arr, num):
    result = 0
    while low <= high:
        mid = (high + low) // 2
        total_wood = total_trees(mid, arr)

        if total_wood == num:
            result = mid
            return result
        
        if total_wood > num:
            result = max(result, mid)
            low = mid + 1
        else:
            high = mid - 1

    return result

        
def main():
    n, m = input().split()
    n, m = int(n), int(m)

    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    result = binary_search(0, arr[0], arr, m)

    print(result)

    

if __name__ == "__main__":
    main()

