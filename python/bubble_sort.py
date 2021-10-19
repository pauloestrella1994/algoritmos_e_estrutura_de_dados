def bubble_sort(n, a):
    numSwaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
    firstElement = a[0]
    lastElement = a[n-1]
    return f"Array is sorted in {numSwaps} swaps.\nFirst Element: {firstElement}\nLast Element: {lastElement}"


if __name__ == '__main__':
    n = int(input("Number of elements in array: ").strip())

    a = list(map(int, input("Elements to be sorted (separated by space): ").rstrip().split()))

    bubble_sort = bubble_sort(n,a)
    print(bubble_sort)