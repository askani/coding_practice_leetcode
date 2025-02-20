def heap_sort(arr):
    n = len(arr)

    print("temp arr 0 : ", arr)
    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("temp arr 1 : ", arr)
    # Extract elements one by one
    # for i in range(n - 1, 0, -1):
    #     arr[i], arr[0] = arr[0], arr[i]  # Swap root with last element
    #     heapify(arr, i, 0)  # Restore heap property

    arr[4], arr[0] = arr[0], arr[4]# Swap root with last element
    print(arr)
    heapify(arr, 4, 0)
    print("temp arr 2 : ", arr)

    arr[3], arr[0] = arr[0], arr[3]  # Swap root with last element
    print(arr)
    heapify(arr, 3, 0)
    print("temp arr 3 : ", arr)

    arr[2], arr[0] = arr[0], arr[2]  # Swap root with last element
    print(arr)
    heapify(arr, 2, 0)
    print("temp arr 4 : ", arr)

    arr[1], arr[0] = arr[0], arr[1]  # Swap root with last element
    print(arr)
    heapify(arr, 1, 0)
    print("temp arr 5 : ", arr)

def heapify(arr, n, i):
    largest = i  # Assume root is largest
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap and continue heapifying if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(arr)
        heapify(arr, n, largest)

# Example Usage
arr = [25, 64, 12, 11, 22]
heap_sort(arr)
print("Sorted array (Heap Sort):", arr)