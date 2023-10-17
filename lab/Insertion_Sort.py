def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be inserted at the right position
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Example usage:
if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]
    print("Original array:", arr)

    insertion_sort(arr)
    print("Sorted array:", arr)
