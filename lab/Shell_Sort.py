def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Start with a large gap and reduce it in each iteration

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Move elements that are gap positions apart
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2  # Reduce the gap size

# Example usage:
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)

    shell_sort(arr)
    print("Sorted array:", arr)
