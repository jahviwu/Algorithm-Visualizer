def selection_sort(arr):
    steps = []

    for i in range(len(arr)):
        min_idx = i

        for j in range(i + 1, len(arr)):
            # Highlight comparison between j and min_idx
            steps.append((arr.copy(), j, min_idx))

            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append((arr.copy(), i, min_idx))

    return arr, steps
