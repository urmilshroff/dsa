def max_subarray_sum(arr):
    global_max = arr[0]

    for i in range(len(arr) - 1):
        local_max = arr[i]

        for j in range(i + 1, len(arr)):
            if local_max < local_max + arr[j]:
                local_max += arr[j]
            else:
                break

        if global_max < local_max:
            global_max = local_max

    return global_max


arr = [-4, -3, 0, 1, 3, 4, -1, 5]
print(f'Maximum subarray sum is {max_subarray_sum(arr)}')
