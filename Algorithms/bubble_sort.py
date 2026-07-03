def bubble_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n):
        for j in range(0, n - i - 1):
            # Record comparison (highlight j and j+1)
            steps.append((arr.copy(), j, j+1))

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Record swap
                steps.append((arr.copy(), j, j+1))

    return arr, steps