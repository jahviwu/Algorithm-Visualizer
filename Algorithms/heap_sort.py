def heapify(arr, n, i, steps):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Compare parent with left child
    if left < n:
        steps.append((arr.copy(), i, left))
        if arr[left] > arr[largest]:
            largest = left

    # Compare parent with right child
    if right < n:
        steps.append((arr.copy(), i, right))
        if arr[right] > arr[largest]:
            largest = right

    # Swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps.append((arr.copy(), i, largest))
        heapify(arr, n, largest, steps)


def heap_sort(arr):
    steps = []
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, steps)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append((arr.copy(), i, 0))
        heapify(arr, i, 0, steps)

    return arr, steps
