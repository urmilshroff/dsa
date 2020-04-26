def kadane(list):
    local_max = global_max = list[0]

    for i in range(1, len(list) - 1):
        local_max = max(list[i], local_max + list[i])
        if local_max > global_max:
            global_max = local_max
            
    return global_max

list = [2, 3, 4, -100, 5, 7, -4]
print(f'Maximum subarray sum is {kadane(list)}')