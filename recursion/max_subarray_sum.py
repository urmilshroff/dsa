def max_crossing_sum(arr, low, mid, high):
    pass


def max_subarray_sum(arr, low, high):
    if low == high:
        return arr[1]

    else:
        mid = (low + high) // 2
        return max(max_subarray_sum(arr, low, mid), max_subarray_sum(arr, mid + 1, high), max_crossing_sum(arr, low, mid, high))


arr = [-4, -3, 0, 1, 2, 4, 5]
print(f'Maximum subarray sum is {max_subarray_sum(arr, 0, len(arr)-1)}')
