def helper(arr, left_pos, mid_pos, right_pos):
    sum1 = sum2 = 0
    left_sum = right_sum = -9999

    for i in range(mid_pos, left_pos - 1, -1):
        sum1 += arr[i]

        if sum1 > left_sum:
            left_sum = sum1

    for i in range(mid_pos + 1, right_pos + 1):
        sum2 += arr[i]

        if sum2 > right_sum:
            right_sum = sum2

    maximum = max(left_sum, right_sum, left_sum + right_sum)

    return maximum


def max_subarray_sum(arr, left_pos, right_pos):
    if left_pos == right_pos:
        return arr[0]

    else:
        mid_pos = (left_pos + right_pos) // 2

        left_arr = max_subarray_sum(arr, left_pos, mid_pos)
        right_arr = max_subarray_sum(arr, mid_pos + 1, right_pos)
        helper_arr = helper(arr, left_pos, mid_pos, right_pos)

        maximum = max(left_arr, right_arr, helper_arr)

        return maximum


arr = [2, 3, 4, -100, 5, 7, -4]
print(f'Maximum subarray sum is {max_subarray_sum(arr, 0, len(arr) - 1)}')
